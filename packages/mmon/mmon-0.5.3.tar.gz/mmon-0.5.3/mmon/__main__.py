import argparse
import logging
import sys
from os import environ

from langchain.chat_models import AzureChatOpenAI, ChatOpenAI
from loguru import logger

from mmon.__about__ import __version__
from mmon.engine import Engine


def get_input() -> str:
    return input("> ")


def main():
    parser = argparse.ArgumentParser(
        description="What's wrong with my linux? v" + __version__
    )
    parser.add_argument(
        "question",
        default="",
        nargs="?",
        type=str,
        help="Initial prompt to start the conversation.",
    )
    parser.add_argument("-v", action="count", default=0, help="verbose mode")
    args = parser.parse_args()

    logger.remove()
    log_format = "{message}"
    if args.v > 2:
        logger.add(sys.stderr, level="DEBUG", format=log_format)
    elif args.v > 0:
        logger.add(sys.stderr, level="INFO", format=log_format)
    else:
        logger.add(sys.stderr, level="WARNING", format=log_format)

    # avoid "WARNING! deployment_id is not default parameter."
    langchain_logger = logging.getLogger("langchain.chat_models.openai")
    langchain_logger.disabled = True

    if "MMON_DEPLOYMENT" in environ:
        print(environ["MMON_DEPLOYMENT"])
        llm = ChatOpenAI(temperature=0, deployment_id=environ["MMON_DEPLOYMENT"])
    else:
        llm = ChatOpenAI(
            temperature=0, model=environ.get("MMON_MODEL", "gpt-3.5-turbo")
        )

    engine = engine = Engine(llm, args.v)
    p = args.question or get_input()
    while True:
        response = engine.run(p)
        print(response)
        p = get_input()


if __name__ == "__main__":
    main()
