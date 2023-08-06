from argparse import ArgumentParser

current_version = "1.3.1"

cli = ArgumentParser(
    "templ8", description=f"Templ8 cli version: {current_version}"
)
cli.add_argument("input", help="input file path")

for (short, long, msg) in [
    ("-d", "--dry-run", "don't generate anything"),
    ("-v", "--verbose", "output verbose logs"),
    ("-c", "--schema", "print schema"),
    ("-s", "--silent", "don't output any logs"),
]:
    cli.add_argument(short, long, help=msg, action="store_true")
