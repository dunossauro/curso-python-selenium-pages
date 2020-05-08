from browser import bind, document
from scripts.form import form
from scripts.query import get_query_string

inputs = [
    {'name': 'nome', 'type': 'text', 'label': 'Como podemos chamar você'},
    {'name': 'email', 'type': 'email', 'label': 'Email'},
    {'name': 'senha', 'type': 'password', 'label': 'Senha'},
    {'name': 'telefone', 'type': 'text', 'label': 'Telefone'},
    {
        'name': 'btn',
        'type': 'submit',
        'Class': 'btn btn-primary btn-block',
        'value': 'Enviar!',
    },
]


login_form = {
    'form': {'action': '#', 'method': 'get', 'autocomplete': 'off'},
    'legend': 'Formulário',
    'inputs': inputs,
}

get_query_string(
    ['nome', 'email', 'senha', 'telefone']
)
form(login_form)
