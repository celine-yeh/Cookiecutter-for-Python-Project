import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

def remove_db_file():
    filenames = [
        'db.py',
        'model.py',
        'repo.py',
    ]
    for fn in filenames:
        remove(os.path.join('{{ cookiecutter.package_name }}', fn))

    filenames = [
        'test_repo.py',
    ]
    for fn in filenames:
        remove(os.path.join('tests', fn))

    remove(os.path.join('initdb.d'))

if __name__ == "__main__":
    if  "{{ cookiecutter.use_db }}" == "0":
        remove_db_file()