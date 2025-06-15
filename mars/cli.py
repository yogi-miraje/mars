from __future__ import annotations

import asyncio
import click

from .gateway import main as gateway_main


@click.group()
def cli() -> None:
    """mars command line interface."""


@cli.command()
def gateway() -> None:
    """Run the Gateway API."""
    gateway_main()


@cli.command()
@click.argument("user_id")
@click.argument("prompt_id")
@click.argument("text")
def demo(user_id: str, prompt_id: str, text: str) -> None:
    """Run a demo query via Gateway."""
    import requests

    resp = requests.post(
        "http://localhost:8000/query", params={"user_id": user_id, "prompt_id": prompt_id, "text": text}
    )
    print(resp.json())


if __name__ == "__main__":
    cli()
