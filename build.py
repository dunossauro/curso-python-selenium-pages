from template_engine import clean_and_copy, make_page

clean_and_copy()

make_page('index', {'title': 'Olar', 'brython_file': 'index'})
make_page('aula_3', {'title': 'Olar', 'brython_file': 'aula_3'})
