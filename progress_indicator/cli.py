# -*- coding: utf-8 -*-

"""Console script for progress_indicator."""

import click


@click.command()
def main(args=None):
    """Console script for progress_indicator."""
    click.echo("Replace this message by putting your code into "
               "progress_indicator.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
