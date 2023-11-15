# clgen.py
import click
import sys

sys.path.insert(0, "./config")

from clgen.config import (
    configure_profile,
    add_cv,
    delete_cv,
    display_cv,
    generate_cover_letter,
)


@click.group()
def clgen():
    """Cover Letter Generator CLI."""
    pass


@clgen.command()
def configure():
    """Configure user profile."""
    configure_profile()


@clgen.command()
def cv_add():
    """Add a new CV."""
    add_cv()


@clgen.command()
def cv_delete():
    """Delete an existing CV."""
    delete_cv()


@clgen.command()
def cv_display():
    """Display an existing CV."""
    display_cv()


@clgen.command()
@click.option(
    "--model",
    default="gpt-4-1106-preview",
    show_default=True,
    help="The model to use for generation.",
)
def generate(model):
    """Generate a cover letter."""
    generate_cover_letter(model)


if __name__ == "__main__":
    clgen()
