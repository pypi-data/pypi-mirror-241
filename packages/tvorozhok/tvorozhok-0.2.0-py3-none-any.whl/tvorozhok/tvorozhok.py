from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
import os
import openai
from openai.error import OpenAIError
import subprocess
import inquirer
from enum import Enum, auto
import json
from datetime import datetime
from prompt_toolkit import PromptSession
import shutil
import re
import tempfile


HOME_DIR = os.path.expanduser("~")
DIALOGUES_DIR = os.path.join(HOME_DIR, ".tvorozhok", "saved_dialogues")

if not os.path.exists(DIALOGUES_DIR):
    os.makedirs(DIALOGUES_DIR)

GIT_REPOS_DIR = os.path.join(HOME_DIR, ".tvorozhok", "git_repos")
GIT_REPOS_FILE = os.path.join(HOME_DIR, ".tvorozhok", "git_repos.txt")
MODELS_LOG = os.path.join(HOME_DIR, ".tvorozhok", "models_log.json")
LAST_MODEL_FILE = os.path.join(HOME_DIR, ".tvorozhok", "last_model.json")


def print_green(text):
    green_start = "\033[92m"
    green_end = "\033[0m"
    print(green_start + text + green_end)


def print_light_blue(text):
    light_blue_start = "\033[94m"
    color_end = "\033[0m"
    print(light_blue_start + text + color_end)


class State(Enum):
    INIT = auto()
    AWAITING_COMMAND = auto()
    CLONING_REPO = auto()
    STARTING_DIALOGUE = auto()
    CONTINUE_DIALOGUE = auto()
    IN_DIALOGUE = auto()
    EXIT = auto()
    REMOVING_REPO = auto()
    LISTING_REPOS = auto()
    PULLING_REPO = auto()


def clone_repository(repo_url, branch=None):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(GIT_REPOS_DIR, repo_name)
    if os.path.exists(repo_path):
        print(f"Repository '{repo_name}' already exists.")
        return

    clone_cmd = ["git", "clone", repo_url, repo_path]
    if branch:
        clone_cmd += ["-b", branch]

    try:
        _ = subprocess.run(
            clone_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        print(f"Repository '{repo_name}' cloned successfully.")

        if branch:
            subprocess.run(["git", "-C", repo_path, "checkout", branch], check=True)

        with open(GIT_REPOS_FILE, "a") as file:
            file.write(repo_name + "\n")

    except subprocess.CalledProcessError as e:
        print(f"Failed to clone '{repo_name}'. Error: {e.stderr.decode()}")


def fetch_models(api_key):
    openai.api_key = api_key
    return openai.Model.list()


class TvorozhokFSM:
    def __init__(self):
        self.state = State.INIT
        self.prompt_session = PromptSession()
        self.context = {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model_name": None,
            "system_context": None,
            "messages": [],
            "saved_dialogue_name": None,
        }
        self.pretty_naming = {
            "start_dialogue": "Start a new dialogue [start_dialogue]",
            "continue_dialogue": "Continue dialogue [continue_dialogue]",
            "clone": "Clone repository [clone <repo_url> -b <branch>]",
            "remove_repo": "Remove repository [remove_repo]",
            "list_repos": "List repositories [list_repos]",
            "pull_repo": "Pull repository changes [pull_repo]",
            "q": "Quit [q]",
        }

    def process_input(self, user_message):
        self.context["messages"].append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model=self.context["model_name"], messages=self.context["messages"]
        )
        chatgpt_message = response["choices"][0]["message"]["content"]
        self.context["messages"].append(
            {"role": "assistant", "content": chatgpt_message}
        )
        return chatgpt_message

    def make_green(self, text):
        green_start = "\033[92m"
        green_end = "\033[0m"
        return green_start + text + green_end

    def make_light_blue(self, text):
        light_blue_start = "\033[94m"
        color_end = "\033[0m"
        return light_blue_start + text + color_end

    def show_menu(self, commands):
        menu_items = [
            str(i + 1) + ". " + self.pretty_naming[command_str]
            for i, command_str in enumerate(commands)
        ]
        print("\n")
        for item in menu_items:
            print_light_blue(item)

    def highlight_code(self, code, language=None):
        try:
            if language:
                lexer = get_lexer_by_name(language)
            else:
                lexer = guess_lexer(code)
        except Exception:
            lexer = get_lexer_by_name("text")

        formatter = TerminalFormatter()
        return highlight(code, lexer, formatter)

    def parse_and_print_response(self, response):
        code_pattern = re.compile(r"```(\w+)?\n(.*?)\n```", re.DOTALL)
        parts = code_pattern.split(response)
        highlighted_response = ""
        for i, part in enumerate(parts):
            if i % 3 == 0:
                highlighted_response += part
            elif i % 3 == 1 and part:
                language = part
            elif i % 3 == 2:
                highlighted_response += self.highlight_code(part, language)
        print("[ChatGPT]:" + f" {highlighted_response}")

    def pulling_repo(self):
        try:
            repo_name = self.prompt_session.prompt(
                "Enter the name of the repository to pull changes: "
            )
        except KeyboardInterrupt:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        except EOFError:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        repo_path = os.path.join(GIT_REPOS_DIR, repo_name)

        if not os.path.isdir(repo_path):
            print(f"The repository '{repo_name}' does not exist.")
        else:
            try:
                result = subprocess.run(
                    ["git", "pull"],
                    cwd=repo_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=True,
                )
                print(result.stdout)
                print(f"Successfully pulled changes for '{repo_name}'.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to pull changes for '{repo_name}'. Error: {e.stderr}")

        self.transition(State.AWAITING_COMMAND)

    def removing_repo(self):
        try:
            repo_name = self.prompt_session.prompt(
                "Enter the name of the repository to remove: "
            )
        except KeyboardInterrupt:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        except EOFError:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        repo_path = os.path.join(GIT_REPOS_DIR, repo_name)

        if not os.path.isdir(repo_path):
            print(f"The repository '{repo_name}' does not exist.")
            self.transition(State.AWAITING_COMMAND)
            return

        try:
            confirm = self.prompt_session.prompt(
                f"Are you sure you want to delete the repository '{repo_name}'? [y/N]: "
            )
        except KeyboardInterrupt:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        except EOFError:
            print("Quit from current section")
            self.transition(State.AWAITING_COMMAND)
        if confirm.lower() == "y":
            try:
                shutil.rmtree(repo_path)
                print(f"Repository '{repo_name}' has been removed.")

                self.remove_repo_from_list(repo_name)

            except Exception as e:
                print(f"An error occurred while removing the repository: {e}")
        else:
            print("Repository removal cancelled.")
        self.transition(State.AWAITING_COMMAND)

    def remove_repo_from_list(self, repo_name):
        with open(GIT_REPOS_FILE, "r") as file:
            repos = file.readlines()

        repos = [line for line in repos if line.strip("\n") != repo_name]

        with open(GIT_REPOS_FILE, "w") as file:
            file.writelines(repos)

    def listing_repos(self):
        print("Cloned repositories:")
        try:
            with open(GIT_REPOS_FILE, "r") as file:
                for line in file:
                    print("- " + line.strip())
        except FileNotFoundError:
            print("No repositories have been cloned yet.")

        self.transition(State.AWAITING_COMMAND)

    def start(self):
        self.transition(State.AWAITING_COMMAND)
        while self.state != State.EXIT:
            self.run_state()

    def run_state(self):
        if self.state == State.AWAITING_COMMAND:
            self.awaiting_command()
        elif self.state == State.CLONING_REPO:
            self.cloning_repo()
        elif self.state == State.STARTING_DIALOGUE:
            self.starting_dialogue()
        elif self.state == State.CONTINUE_DIALOGUE:
            self.continue_dialogue()
        elif self.state == State.IN_DIALOGUE:
            self.in_dialogue()
        if self.state == State.REMOVING_REPO:
            self.removing_repo()
        if self.state == State.LISTING_REPOS:
            self.listing_repos()
        if self.state == State.PULLING_REPO:
            self.pulling_repo()
        elif self.state == State.EXIT:
            self.exit()

    def transition(self, new_state):
        self.state = new_state

    def get_api_key(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            try:
                api_key = self.prompt_session.prompt("Enter your OpenAI API key: ")
            except KeyboardInterrupt:
                print("Quit from current section")
                self.transition(State.AWAITING_COMMAND)
            except EOFError:
                print("Quit from current section")
                self.transition(State.AWAITING_COMMAND)
            os.environ["api_key"] = api_key
        else:
            openai.api_key = api_key
            self.context["api_key"] = api_key
        return api_key

    def get_last_used_model(self):
        try:
            with open(LAST_MODEL_FILE, "r") as f:
                last_model = json.load(f)
                return last_model["model_name"]
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def set_last_used_model(self, model_name):
        with open(LAST_MODEL_FILE, "w") as f:
            json.dump({"model_name": model_name}, f)

    def has_saved_dialogues(self, model_name):
        model_dir = os.path.join(DIALOGUES_DIR, model_name)
        return os.path.exists(model_dir) and len(os.listdir(model_dir)) > 0

    def awaiting_command(self):
        last_model = self.get_last_used_model()
        if last_model and self.has_saved_dialogues(last_model):
            commands = [
                "start_dialogue",
                "continue_dialogue",
                "clone",
                "remove_repo",
                "pull_repo",
                "list_repos",
                "q",
            ]
        else:
            commands = [
                "start_dialogue",
                "clone",
                "remove_repo",
                "pull_repo",
                "list_repos",
                "q",
            ]

        self.show_menu(commands)

        command = self.prompt_session.prompt("").strip().lower()
        if command == "q":
            self.transition(State.EXIT)
        elif command.startswith("clone"):
            self.context["repo_url"] = command.split()[1]
            self.transition(State.CLONING_REPO)
        elif command == "start_dialogue":
            self.transition(State.STARTING_DIALOGUE)
        elif command == "remove_repo":
            self.transition(State.REMOVING_REPO)
        elif command == "pull_repo":
            self.transition(State.PULLING_REPO)
        elif command == "list_repos":
            self.transition(State.LISTING_REPOS)
        elif command == "continue_dialogue":
            self.transition(State.CONTINUE_DIALOGUE)
        else:
            print("Unknown command.")

    def cloning_repo(self):
        clone_repository(self.context["repo_url"])
        self.transition(State.AWAITING_COMMAND)

    def continue_dialogue(self):
        model_name = self.get_last_used_model()
        existing_dialogues = (
            self.list_model_saved_dialogues(model_name) if model_name else []
        )

        if not existing_dialogues:
            print("No saved dialogues are available to continue.")
            self.transition(State.AWAITING_COMMAND)
            return

        dialogue_options = existing_dialogues + ["Start a new dialogue"]
        questions = [
            inquirer.List(
                "dialogue",
                message="Choose a dialogue to continue or start new",
                choices=dialogue_options,
            )
        ]
        try:
            selected_option = inquirer.prompt(questions)["dialogue"]
        except Exception as e:
            print(f"An error occurred: {e}")

        if selected_option == "Start a new dialogue":
            self.get_system_context()
            self.transition(State.IN_DIALOGUE)
        else:
            self.context["model_name"] = model_name
            self.load_saved_dialogue(selected_option)
            self.transition(State.IN_DIALOGUE)

    def starting_dialogue(self):
        self.get_api_key()
        self.context["model_name"] = self.select_model()
        self.log_model_choice(self.context["model_name"])
        existing_dialogues = self.list_model_saved_dialogues(self.context["model_name"])

        if existing_dialogues:
            print(
                "Found saved dialogues for this model. Would you like to continue an existing dialogue?"
            )
            dialogue_options = existing_dialogues + ["Start a new dialogue"]
            questions = [
                inquirer.List(
                    "dialogue", message="Choose an option", choices=dialogue_options
                )
            ]
            selected_option = inquirer.prompt(questions)["dialogue"]

            if selected_option in existing_dialogues:
                self.load_saved_dialogue(selected_option)
                self.transition(State.IN_DIALOGUE)
            else:
                system_context = self.get_system_context()
                if system_context is None:
                    self.transition(State.AWAITING_COMMAND)
                else:
                    self.context["system_context"] = system_context
                    self.transition(State.IN_DIALOGUE)
        else:
            system_context = self.get_system_context()
            if system_context is None:
                self.context["system_context"] = system_context
                self.transition(State.AWAITING_COMMAND)
            else:
                self.context["system_context"] = system_context
                self.transition(State.IN_DIALOGUE)

    def select_model(self):
        models_response = fetch_models(self.context["api_key"])
        if "data" not in models_response:
            self.report_error(
                "Failed to fetch models. Please check your OpenAI API key and try again."
            )
            return None
        models = models_response["data"]
        questions = [
            inquirer.List(
                "model",
                message="Select a model",
                choices=[model["id"] for model in models],
                carousel=True,
            )
        ]
        selected_model = inquirer.prompt(questions)
        if selected_model:
            self.set_last_used_model(selected_model["model"])
            return selected_model["model"]
        else:
            self.report_error("No model selected. Please try again.")
            return None

    @staticmethod
    def read_repository_files(repo_name, file_names=None):
        if file_names is None:
            file_names = []
        repo_path = os.path.join(GIT_REPOS_DIR, repo_name)
        files_content = ""
        if not os.path.exists(repo_path):
            print(f"The repository path {repo_path} does not exist.")
            return files_content
        for root, _, files in os.walk(repo_path):
            for file in files:
                if (file.endswith(".py") and file in file_names) or (
                    (file_names is None or "all" in file_names) and file.endswith(".py")
                ):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r") as file_content:
                            prepend = (
                                "### BELOW IS THE CONTENT OF FILE "
                                + file_path
                                + "#### \n"
                            )
                            files_content += prepend + file_content.read() + "\n"
                    except IOError as e:
                        print(f"An error occurred while reading file {file_path}: {e}")

        return files_content

    def get_system_context(self):
        while True:
            context_input = self.prompt_session.prompt(
                'Enter the context for the dialogue, or "repo_context -r <repo_name>" to use repository files: '
            )
            if context_input.lower() in ["q", "quit"]:
                return None

            if context_input.startswith("repo_context"):
                parts = context_input.split()
                if "-r" in parts:
                    repo_index = parts.index("-r") + 1
                    if repo_index < len(parts):
                        repo_name = parts[repo_index]
                        if repo_name in open(GIT_REPOS_FILE).read():
                            file_names = None
                            if "-f" in parts:
                                file_index = parts.index("-f") + 1
                                file_names = parts[file_index:]
                            system_context = self.read_repository_files(
                                repo_name, file_names
                            )
                            return system_context
                        else:
                            self.report_error(
                                f"Repository '{repo_name}' not found in 'git_repos.txt'."
                            )
                    else:
                        self.report_error(
                            "The '-r' flag must be followed by the name of the repository."
                        )
                else:
                    self.report_error(
                        "The 'repo_context' command requires the '-r' flag to specify the repository name."
                    )
            elif context_input.strip():
                return context_input
            else:
                self.report_error("Invalid input. Please provide a valid context.")

    def edit_context_with_vim(self):
        with tempfile.NamedTemporaryFile(
            suffix=".md", mode="w+", delete=False
        ) as temp_file:
            temp_file.write(self.context["system_context"])
            temp_file.flush()
            subprocess.run(["vim", temp_file.name])
            temp_file.seek(0)
            modified_context = temp_file.read()

        self.context["system_context"] = modified_context
        idx_of_last_system_message = [
            i
            for i in range(len(self.context["messages"]))
            if self.context["messages"][i]["role"] == "system"
        ][0]
        self.context["messages"][idx_of_last_system_message] = {
            "role": "system",
            "content": modified_context,
        }

    def dialogue_interaction(self):
        openai.api_key = self.context["api_key"]
        if not self.context["messages"]:
            self.context["messages"] = [
                {"role": "system", "content": self.context["system_context"]}
            ]

        print("Enter your message for ChatGPT (type 'quit' to end the dialogue):")
        while True:
            user_message = self.prompt_session.prompt("[USER]: ")
            if user_message.lower() in ["quit", "q"]:
                if self.context["messages"]:
                    if input("Do you want to save this dialogue? [Y/n] ").lower() in [
                        "y",
                        "yes",
                        "",
                    ]:
                        dialogue_name = self.prompt_session.prompt(
                            "Enter a name for this dialogue: "
                        )
                        self.save_dialogue(dialogue_name)
                self.transition(State.AWAITING_COMMAND)
                break

            if user_message == "__change_context__":
                self.edit_context_with_vim()
                print("System context updated. You may continue the dialogue.")
                continue

            self.context["messages"].append({"role": "user", "content": user_message})
            try:
                response = openai.ChatCompletion.create(
                    model=self.context["model_name"], messages=self.context["messages"]
                )
                chatgpt_message = response["choices"][0]["message"]["content"]
                self.parse_and_print_response(chatgpt_message)

                self.context["messages"].append(
                    {"role": "assistant", "content": chatgpt_message}
                )
            except OpenAIError as e:
                self.report_error(f"An OpenAI API error occurred: {str(e)}")
            except Exception as e:
                self.report_error(f"An unexpected error occurred: {str(e)}")

    def report_error(self, message):
        print(message)

    def in_dialogue(self):
        self.dialogue_interaction()
        self.transition(State.AWAITING_COMMAND)

    def exit(self):
        print("Exiting application.")

    def log_model_choice(self, model_name):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {"model_name": model_name, "timestamp": timestamp}
        try:
            with open(MODELS_LOG, "a") as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"An error occurred while logging the model choice: {e}")

    def save_dialogue(self, dialogue_name):
        if self.context["messages"]:
            model_dir = os.path.join(DIALOGUES_DIR, self.context["model_name"])
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)

            dialogue_path = os.path.join(model_dir, f"{dialogue_name}.json")
            try:
                with open(dialogue_path, "w") as dialogue_file:
                    json.dump(self.context["messages"], dialogue_file, indent=4)
                print(
                    f"Dialogue '{dialogue_name}' has been saved under model '{self.context['model_name']}'."
                )
            except IOError as e:
                print(f"An error occurred while saving the dialogue: {e}")
            self.transition(State.AWAITING_COMMAND)
        else:
            print("No dialogue to save.")
            self.transition(State.AWAITING_COMMAND)

    def list_saved_dialogues(self):
        dialogue_files = [f for f in os.listdir(DIALOGUES_DIR) if f.endswith(".json")]
        dialogue_names = [os.path.splitext(f)[0] for f in dialogue_files]
        return dialogue_names

    def list_model_saved_dialogues(self, model_name):
        model_dir = os.path.join(DIALOGUES_DIR, model_name)
        if not os.path.exists(model_dir):
            return []

        dialogue_files = [f for f in os.listdir(model_dir) if f.endswith(".json")]
        dialogue_names = [os.path.splitext(f)[0] for f in dialogue_files]
        return dialogue_names

    def select_saved_dialogue(self):
        dialogues = self.list_saved_dialogues()
        if dialogues:
            questions = [
                inquirer.List(
                    "dialogue",
                    message="Select a saved dialogue to continue",
                    choices=dialogues,
                    carousel=True,
                )
            ]
            selected_dialogue_name = inquirer.prompt(questions)["dialogue"]
            self.context["saved_dialogue_name"] = selected_dialogue_name
            self.load_saved_dialogue(selected_dialogue_name)
            self.transition(State.IN_DIALOGUE)
        else:
            print("No saved dialogues are available.")
            self.transition(State.AWAITING_COMMAND)

    def load_saved_dialogue(self, dialogue_name):
        model_dir = os.path.join(DIALOGUES_DIR, self.context["model_name"])
        dialogue_path = os.path.join(model_dir, f"{dialogue_name}.json")
        try:
            with open(dialogue_path, "r") as dialogue_file:
                dialogue_data = json.load(dialogue_file)
            if isinstance(dialogue_data, list):
                self.context["messages"] = dialogue_data
                last_system_message = [
                    message for message in dialogue_data if message["role"] == "system"
                ][-1]
                self.context["system_context"] = last_system_message["content"]
            else:
                raise ValueError(
                    "Invalid dialogue format: expected a list of messages."
                )
            print(f"Dialogue '{dialogue_name}' has been loaded successfully.")
        except (IOError, ValueError) as e:
            self.report_error(f"An error occurred while loading the dialogue: {e}")
