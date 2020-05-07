#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

__author__ = "David Ross"
__version__ = "0.1.3"
__license__ = "MIT"

import argparse
import logging
import logzero
from logzero import logger
import os
import essentialmix_repack as repack


def main(args):
    if args.debug:
        logzero.loglevel(logging.INFO)
        logger.info("Debug args: " + str(vars(args)))
    else:
        logzero.loglevel(logging.ERROR)

    if not os.path.isdir(args.dir):
        os.makedirs(args.dir)
        logger.info("Creating directory: " + args.dir)
    os.chdir(args.dir)

    repack.archive(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("-s", "--simulate", action="store_true", default=False)
    parser.add_argument(
        "-n", "--limit", action="store", dest="limit", type=int, default=1
    )

    parser.add_argument(
        "-d",
        "--dir",
        dest="dir",
        type=str,
        default="./output/",
        help="Directory to save to",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__),
    )

    args = parser.parse_args()
    main(args)
