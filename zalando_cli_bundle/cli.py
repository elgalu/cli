import sys

import click


def main():
    click.secho(
        """Zalando CLI Bundle - bundle of command line tools for Zalando developers""",
        bold=True,
    )

    do_configure = len(sys.argv) > 1 and "configure".startswith(sys.argv[1])
    if do_configure or click.confirm(
        "Do you want to configure the Zalando CLI tools now?", default=True
    ):
        import stups_cli.config

        domain = None
        if len(sys.argv) > 2:
            domain = sys.argv[2]
        else:
            domain = "stups.zalan.do"
        stups_cli.config.configure(domain)
