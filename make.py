from pathlib import Path
import click
import string


@click.command()
@click.argument("q_type")
@click.argument("name")
@click.option("--num", default=4)
def cmd(q_type, name, num):
    p = Path(".")
    if q_type == "abc":
        p = p / "atcoder-beginner-contest" / name
    elif q_type == "other":
        p = p / "other" / name
    try:
        p.mkdir()
    except FileExistsError:
        pass

    for i, file_name in enumerate(string.ascii_uppercase):
        if not i < num:
            break
        q = p / f"{file_name}.py"
        q.touch()


if __name__ == "__main__":
    cmd()
