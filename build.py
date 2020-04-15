from template_engine import clean_and_copy, make_page

clean_and_copy()

make_page(
    'index', {'title': 'Olar', 'path': 'paginas', 'brython_file': 'index'}
)

make_page(
    'aula_03', {'title': 'Aula 03', 'type': 'aulas', 'brython_file': 'aula_03'}
)
