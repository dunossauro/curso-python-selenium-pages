from scripts.form import form
from scripts.query import get_query_string

login_form = {
    'form': {'action': '#', 'method': 'get'},
    'legend': 'Faça seu cadastro',
    'inputs': [
        {'name': 'nome', 'type': 'text', 'label': 'nome'},
        {'name': 'email', 'type': 'email', 'label': 'email'},
        {'name': 'senha', 'type': 'password', 'label': 'senha'},
        {
            'name': 'a',
            'type': 'submit',
            'Class': 'btn btn-primary btn-block',
            'value': 'Enviar!',
        },
    ],
}

get_query_string(['nome', 'email', 'senha'])
form(login_form)
