#!/bin/env python3

import tomllib
import sys
import logging
from argparse import ArgumentParser
import difflib
from difflib import Differ
from pprint import pprint

DESCRIPTION = """Generate a detailed list of the differences between two TOML
files with an understanding of their structure"""

PARSER = ArgumentParser(
    prog='toml-diff.py',
    description=DESCRIPTION,
)

PARSER.add_argument(
    "lhfile",
    help="Path to an file to analyze.",
)

PARSER.add_argument(
    "rhfile",
    help="Path to an file to analyze.",
)

PARSER.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Toggle verbose output",
)


# From a tree of dicts, we create a dict of depth one. Recursive function, the
# top level should be called with prefix ""
def flatten(prefix: str, data: dict) -> dict[str, str]:
    out = {}

    for (k, v) in data.items():
        if isinstance(v, dict):
            out.update(flatten(k, v))
        else:
            out.update({f"{prefix}.{k}": str(v)})

    return out


# Prepare a dict for diffing by formatting its items and sorting the resulting
# list
def prepare(data: dict[str, str]) -> list[str]:
    format_ = lambda t: f"{t[0]}: {t[1]}\n"

    out = list(map(format_, data.items()))
    out.sort()

    return out


def main():
    args = PARSER.parse_args()

    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(message)s",
        )

    with open(args.lhfile, 'rb') as lstream:
        ldata = tomllib.load(lstream)
        lblock = prepare(flatten("", ldata))

    with open(args.rhfile, 'rb') as rstream:
        rdata = tomllib.load(rstream)
        rblock = prepare(flatten("", rdata))

    diff = list(
        difflib.unified_diff(lblock,
                             rblock,
                             fromfile=args.lhfile,
                             tofile=args.rhfile))
    sys.stdout.writelines(diff)

    sys.exit(0)


main()
