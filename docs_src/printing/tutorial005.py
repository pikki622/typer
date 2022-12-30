import typer


def main(good: bool = True):
    if good:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
    message = f"everything is {ending}"
    typer.echo(message)


if __name__ == "__main__":
    typer.run(main)
