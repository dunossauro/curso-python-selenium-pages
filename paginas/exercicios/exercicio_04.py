from browser import bind, document, html
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

if not document.query.getvalue('nome'):
    document['main'] <= html.P(
        'Você deve preencher o forumlário e enviar'
    )
    form(login_form)
else:
    document['main'] <= html.P(
        'Agora você deve checar se a url bate com o resultado'
    )

    get_query_string(
        ['nome', 'email', 'senha', 'telefone'],
        'main'
    )
