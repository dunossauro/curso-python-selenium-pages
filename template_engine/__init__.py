from typing import NoReturn
from jinja2 import FileSystemLoader, Environment
from os.path import abspath, exists
from os import mkdir
from shutil import copytree, rmtree


def _select_template(template):
    temp_path = FileSystemLoader(searchpath=abspath("./templates"))

    j_env = Environment(loader=temp_path)

    return j_env.get_template("{}.html".format(template))


def make_page(page_name, jinja_vars) -> NoReturn:
    """
    Cria uma página usando o template selecionado.

    Os templates selecionados devem estar no path `templates`

    Essa funão retorna a criação de um arquivo no path `site`

    Example:
    -------
    >>> jinja_vars = {'my_jinja_param_1': 'foo', my_jinja_param_2: 'bar'}
    >>> make_page('my_page', jinja_vars)

    """
    template = _select_template('page_template')

    with open(f'site/{page_name}.html', 'w') as f:
        f.write(template.render(jinja_vars))


def clean_and_copy(build_path='site', paths_to_copy=['css', 'js', 'scripts']):
    """Limpa o `build_path` e o cria de novo e adiciona os `paths_to_copy`."""
    if exists(build_path):
        rmtree(build_path)

    mkdir(build_path)

    for path in paths_to_copy:
        copytree(f'{path}', f'./{build_path}/{path}/')
