FROM python:{{ cookiecutter.python_version }}-stretch AS base
WORKDIR /workspace
RUN pip install pipenv==2018.11.26

FROM base as runtime
COPY Pipfile* ./
RUN pipenv install --system --deploy \
    && rm Pipfile*

FROM runtime AS dev
COPY Pipfile* ./
RUN pipenv install --system --deploy --dev \
    && rm Pipfile*
{%- if cookiecutter.use_db|int %}
RUN apt-get update && apt-get install -y --no-install-recommends mysql-client
{%- endif %}

FROM runtime AS prod
COPY . ./
RUN ln -s /workspace/{{ cookiecutter.cli_name }} /usr/local/bin/{{ cookiecutter.cli_name }}
