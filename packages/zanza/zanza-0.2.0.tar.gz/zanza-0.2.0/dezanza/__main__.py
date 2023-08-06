#!/usr/bin/env python

import argparse
import json
import logging
import sys

from . import dezanza, __doc__ as manual

logger = logging.getLogger(__name__)


def main():
    """Deobfuscator main program.
    """

    parser = argparse.ArgumentParser(
        description="Deobfuscate the given input sequence",
        epilog=manual,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "source",
        help="JSON-encoded input sequence to deobfuscate. If omitted, input\
            is taken from the standard input (stdin)",
        nargs="?"
    )
    args = parser.parse_args()

    if args.source is None:
        source = sys.stdin.read()
    else:
        source = args.source

    try:
        zj = json.loads(source)
        zs = dezanza(zj)
        print(zs)
    except Exception as ex:
        logger.error("ERROR: %s" % ex)


if __name__ == "__main__":
    main()
