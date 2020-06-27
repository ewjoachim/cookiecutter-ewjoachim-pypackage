import contextlib
import logging
import os

import click

from {{ cookiecutter.package_name }} import __version__, exceptions, utils

logger = logging.getLogger(__name__)

PROGRAM_NAME = "{{ cookiecutter.cli_name }}"
ENV_PREFIX = PROGRAM_NAME.upper()

CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
    "auto_envvar_prefix": ENV_PREFIX,
}


def get_log_level(verbosity: int) -> int:
    """
    Given the number of repetitions of the flag -v,
    returns the desired log level
    """
    return {0: logging.INFO, 1: logging.DEBUG}.get(min((1, verbosity)), 0)


def click_set_verbosity(ctx: click.Context, param: click.Parameter, value: int) -> int:
    set_verbosity(verbosity=value)
    return value


def set_verbosity(verbosity: int) -> None:
    level = get_log_level(verbosity=verbosity)
    logging.basicConfig(level=level)
    level_name = logging.getLevelName(level)
    logger.debug(
        f"Log level set to {level_name}",
        extra={"action": "set_log_level", "value": level_name},
    )


@contextlib.contextmanager
def handle_errors():
    try:
        yield
    except Exception as exc:
        logger.debug("Exception details:", exc_info=exc)
        messages = [str(e) for e in utils.causes(exc)]
        raise click.ClickException("\n".join(e for e in messages if e))


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.option(
    "-v",
    "--verbose",
    is_eager=True,
    callback=click_set_verbosity,
    count=True,
    help="Use multiple times to increase verbosity",
)
@click.version_option(
    __version__, "-V", "--version", prog_name=PROGRAM_NAME
)
@handle_errors()
def cli(ctx: click.Context, app: str, **kwargs) -> None:
    """
    TODO: write me
    """

    ctx.obj = ...


@cli.command()
@click.pass_obj
@handle_errors()
def foo(main_obj: ...):
    """
    TODO: write me
    """


def main():
    # https://click.palletsprojects.com/en/7.x/python3/
    os.environ.setdefault("LC_ALL", "C.UTF-8")
    os.environ.setdefault("LANG", "C.UTF-8")

    return cli()
