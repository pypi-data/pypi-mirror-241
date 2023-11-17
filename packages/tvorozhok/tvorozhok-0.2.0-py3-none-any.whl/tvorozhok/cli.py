from tvorozhok import TvorozhokFSM, print_green
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        logger.info("The OPENAI_API_KEY environment variable is not set.")
        openai_api_key = input("Please enter your OpenAI API key: ").strip()
        if not openai_api_key:
            logger.error("No OpenAI API key provided. Exiting application.")
            return

        os.environ["OPENAI_API_KEY"] = openai_api_key

    ascii_art = """
   _______     _____  ____   ___ ______   _  ___  _  __
  |_   _\ \   / / _ \|  _ \ / _ \__  / | | |/ _ \| |/ /
    | |  \ \ / / | | | |_) | | | |/ /| |_| | | | | ' / 
    | |   \ V /| |_| |  _ <| |_| / /_|  _  | |_| | . \ 
    |_|    \_/  \___/|_| \_\\___/____|_| |_|\___/|_|\_\
    """

    print_green(ascii_art)
    app = TvorozhokFSM()
    app.start()


if __name__ == "__main__":
    main()
