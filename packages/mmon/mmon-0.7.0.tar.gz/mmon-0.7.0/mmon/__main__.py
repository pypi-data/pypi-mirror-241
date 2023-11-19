import argparse
import atexit
import logging
import readline
import sys
from os import environ, path

from langchain.chat_models import AzureChatOpenAI, ChatOpenAI
from loguru import logger

from mmon.__about__ import __version__
from mmon.engine import Engine


def setup_readline():
    histfile = path.join(path.expanduser("~"), ".mmon_history")
    try:
        readline.read_history_file(histfile)
        # default history len is -1 (infinite), which may grow unruly
        readline.set_history_length(1000)
    except FileNotFoundError:
        pass

    atexit.register(readline.write_history_file, histfile)


def get_input() -> str:
    try:
        return input("> ")
    except EOFError:
        return ""


def main():
    parser = argparse.ArgumentParser(description="mmon v" + __version__)
    parser.add_argument(
        "question",
        default="",
        nargs="?",
        type=str,
        help="Initial prompt to start the conversation.",
    )
    parser.add_argument("-v", action="count", default=0, help="verbose level")
    args = parser.parse_args()

    logger.remove()
    log_format = "{message}"
    if args.v > 2:
        logger.add(sys.stderr, level="DEBUG", format=log_format)
    elif args.v > 0:
        logger.add(sys.stderr, level="INFO", format=log_format)
    else:
        logger.add(sys.stderr, level="WARNING", format=log_format)

    if args.v <= 2:
        # avoid "WARNING! deployment_id is not default parameter."
        langchain_logger = logging.getLogger("langchain.chat_models.openai")
        langchain_logger.disabled = True

    if "MMON_DEPLOYMENT" in environ:
        llm = ChatOpenAI(temperature=0, deployment_id=environ["MMON_DEPLOYMENT"])
    else:
        llm = ChatOpenAI(
            temperature=0, model=environ.get("MMON_MODEL", "gpt-3.5-turbo")
        )

    engine = engine = Engine(llm, args.v)
    setup_readline()
    p = args.question or get_input()
    while len(p) > 0:
        response = engine.run(p)
        print(response + "\n")
        p = get_input()


if __name__ == "__main__":
    main()
