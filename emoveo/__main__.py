"""Main module for emoveo."""


from emoveo.console import console
from emoveo.dedup import dedup
from emoveo.parser import parser


def main():
    """Run main CLI function."""
    args = parser.parse_args()
    dedup(args.input)

    console.log('Done.')


if __name__ == '__main__':
    main()
