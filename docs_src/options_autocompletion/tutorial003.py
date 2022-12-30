import typer

valid_names = ["Camila", "Carlos", "Sebastian"]


def complete_name(incomplete: str):
    return [name for name in valid_names if name.startswith(incomplete)]


app = typer.Typer()


@app.command()
def main(
    name: str = typer.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    )
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
