from template_engine import clean_and_copy, make_page

clean_and_copy()

form_aula_1 = {
    'legend': 'Faça seu cadastro',
    'inputs': [
        {'name': 'nome', 'type': 'text', 'label': 'nome'},
        {'name': 'email', 'type': 'email', 'label': 'email'},
        {'name': 'senha', 'type': 'password', 'label': 'senha'},
    ],
    'button': {'text': 'enviar', 'Class': 'btn btn-primary btn-block'},
}

aula_1 = f'''
from scripts.form import form

form({form_aula_1})
'''


make_page('index', {'title': 'Olar'})
make_page('aula_1', {'title': 'Olar', 'brython': aula_1})
