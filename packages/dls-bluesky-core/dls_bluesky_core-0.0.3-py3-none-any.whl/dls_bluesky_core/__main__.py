from argparse import ArgumentParser
from typing import Optional, Sequence

from . import __version__

__all__ = ["main"]


def main(args: Optional[Sequence[str]] = None) -> None:
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.parse_args(args)


# test with: python -m dls_bluesky_core
if __name__ == "__main__":
    main()
