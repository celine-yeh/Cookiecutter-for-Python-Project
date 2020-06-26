import click

from .facade import greeting{% if cookiecutter.use_db|int %}, list_all_user{% endif %}


@click.group()
def main():
    pass

@main.command()
@click.argument('name')
def greet(name):
    click.echo(greeting(name))

{%- if cookiecutter.use_db|int %}

@main.command()
def list_user():
    click.echo(list_all_user())
{%- endif %}