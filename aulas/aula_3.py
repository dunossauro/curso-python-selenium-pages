from browser import bind, document, console
from scripts.form import form
from scripts.query import get_query_string

login_form = {
    'form': {'action': '#', 'method': 'get', 'autocomplete': 'off'},
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


@bind('#nome', 'focus')
def focus(ev):
    document['lnome'].text = 'Não vale mentir o nome'


@bind('#nome', 'blur')
def focus(ev):
    document['lnome'].text = 'nome:'


@bind('#email', 'focus')
def focus(ev):
    document['lemail'].text = 'Esse email é mesmo válido?'


@bind('#email', 'blur')
def focus(ev):
    document['lemail'].text = 'email:'


@bind('#senha', 'focus')
def focus(ev):
    document['lsenha'].text = 'Já falei pra não colocar 1234'


@bind('#senha', 'blur')
def focus(ev):
    document['lsenha'].text = 'senha:'
