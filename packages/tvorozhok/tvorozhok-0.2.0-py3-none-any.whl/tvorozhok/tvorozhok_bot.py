import telebot
from tvorozhok import TvorozhokFSM  # import your TvorozhokFSM class
import threading

from enum import Enum


# Define your FSM States, if not already defined
class State(Enum):
    INIT = 1
    AWAITING_COMMAND = 2
    CLONING_REPO = 3


# Load your Telegram API key and the OpenAI API key
TELEGRAM_API_KEY = "your_telegram_bot_api_token"
openai_api_key = "your_openai_api_key"
os.environ["OPENAI_API_KEY"] = openai_api_key

bot = telebot.TeleBot(TELEGRAM_API_KEY)
app = TvorozhokFSM()


class UserSession:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.state = State.INIT
        self.context = {
            "api_key": None,
            "repo_url": None,  # You can add more context variables as needed
        }

    def update_state(self, new_state):
        self.state = new_state

    # Define methods to handle different actions
    def clone_repo(self, repo_url):
        # Here you would put the actual cloning logic.
        # This is a placeholder for the actual functionality.
        print(f"Cloning the repository {repo_url} for chat_id {self.chat_id}")
        # Remember to update the state as necessary

    # Add more handlers for other actions like 'list_repos', 'remove_repo', etc.


# A dictionary to keep track of user sessions by chat ID
user_sessions = {}


# Example usage within your Telegram bot handlers:


@bot.message_handler(commands=["clone"])
def handle_clone(message):
    chat_id = message.chat.id
    if chat_id not in user_sessions:
        user_sessions[chat_id] = UserSession(chat_id)
    user_session = user_sessions[chat_id]
    user_session.update_state(State.CLONING_REPO)
    bot.send_message(
        chat_id, "Please send me the URL of the repository you want to clone."
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id not in user_sessions:
        bot.send_message(chat_id, "Please use /start to initiate the Tvorozhok bot.")
        return

    user_session = user_sessions[chat_id]
    if user_session.state == State.CLONING_REPO:
        repo_url = message.text  # Assuming the message text is the repo URL
        user_session.clone_repo(repo_url)
        # Update the state or respond as necessary after cloning
        bot.send_message(chat_id, "Repository cloning initiated. Please wait...")
        user_session.update_state(State.AWAITING_COMMAND)
    # Add handling for other states and their corresponding logic


def execute_clone_repo(user_session, repo_url):
    # Perform the clone operation in a separate thread
    thread = threading.Thread(target=clone_repository, args=(repo_url,))
    thread.start()
    thread.join()  # You may handle this asynchronously as well, depending on your requirements
    user_session.update_state(State.AWAITING_COMMAND)


# A simple command to start the bot
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hello! I am Tvorozhok, your AI friend. Just start typing to talk to me.",
    )


# Process text messages from users
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Run Tvorozhok processing with the message text and get the response
    response_text = app.process_input(
        message.text
    )  # Assume such a method exists in TvorozhokFSM
    bot.send_message(message.chat.id, response_text)


# Start the bot
bot.polling()
