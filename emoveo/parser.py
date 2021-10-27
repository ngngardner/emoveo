"""Parser module for emoveo."""

import argparse

parser = argparse.ArgumentParser(
    description='Remove duplicate pages from a .pdf file.'
)
parser.add_argument(
    '-i',
    '--input',
    help='Input file',
    required=True,
    type=str,
)
