"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Kedro Hyperparam."""


if __name__ == "__main__":
    main(prog_name="kedro-hyperparam")  # pragma: no cover
