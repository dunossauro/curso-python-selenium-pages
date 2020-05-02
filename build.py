from template_engine import clean_and_copy, make_page

clean_and_copy()

make_page(
    'index', {'title': 'Olar', 'path': 'paginas', 'brython_file': 'index'}
)

make_page(
    'aula_03',
    {
        'raw': True,
        'title': 'Aula 03',
        'type': 'aulas',
        'path': 'aulas',
        'brython_file': 'aula_03',
    },
)

make_page(
    'exercicio_01',
    {
        'raw': True,
        'title': 'Exercício 01',
        'type': 'exercicios',
        'path': 'exercicios',
        'brython_file': 'exercicio_01',
    },
)


make_page(
    'exercicio_02',
    {
        'raw': True,
        'title': 'Exercício 02',
        'type': 'exercicios',
        'path': 'exercicios',
        'brython_file': 'exercicio_02',
    },
)

make_page(
    'exercicio_03',
    {
        'title': 'Exercício 03',
        'type': 'exercicios',
        'path': 'exercicios',
        'brython_file': 'exercicio_03',
    },
)


make_page(
    'aula_04',
    {
        'title': 'Aula 04',
        'type': 'aulas',
        'path': 'aulas',
        'brython_file': 'aula_04',
    },
)

# stuff pages
from os import listdir
path = 'paginas/stuff_pages'
for page in listdir(path):
    make_page(page.replace('.py', ''), {
        'title': page.replace('py', 'html'),
        'type': page,
        'path': 'stuff_pages',
        'brython_file': page.replace('.py', ''),
        }
    )

# make_page(
#     'aula_05',
#     {
#         'title': 'Aula 05',
#         'type': 'aulas',
#         'path': 'aulas',
#         'brython_file': 'aula_05',
#     },
# )
