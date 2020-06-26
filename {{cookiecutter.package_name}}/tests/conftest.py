{%- if cookiecutter.use_db|int %}
import pytest

from {{ cookiecutter.package_name }}.db import get_engine
from {{ cookiecutter.package_name }}.model import Base


@pytest.fixture
def clean_db():
    engine = get_engine()
    for table in Base.metadata.sorted_tables:
        engine.execute('TRUNCATE TABLE %s;' % table)

    return engine
{%- endif %}