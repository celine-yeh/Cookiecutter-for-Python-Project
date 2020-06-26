{%- if cookiecutter.use_db|int -%}
from .db import transaction
from .repo import user_repo


@transaction()
def list_all_user():
    users = user_repo.list()
    return [(user.id, user.username, user.display_name) for user in users]

{% endif -%}
def greeting(name):
    return f'Hello, {name}'
