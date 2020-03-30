#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

__author__ = "David Ross"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging
import logzero
from logzero import logger


def main(args):
    """ Main entry point of the app """
    if(args.debug):
        logzero.loglevel(logging.INFO)
        logger.info("Debug args: " + str(vars(args)))
    else:
        logzero.loglevel(logging.ERROR)
    print("BBC Essential Mixes archived")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    # parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-d", "--debug", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    # parser.add_argument("-n", "--name", action="store", dest="name")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
