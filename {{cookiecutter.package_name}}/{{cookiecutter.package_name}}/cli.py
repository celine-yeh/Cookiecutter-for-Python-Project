import click

from .facade import greeting


@click.group()
def main():
    pass

@main.command()
@click.argument('name')
def greet(name):
    click.echo(greeting(name))
