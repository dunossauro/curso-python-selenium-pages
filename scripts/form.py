"""
Módulo para gerenciar coisas relativas a forms.

Example:
-------
>>> form_spec = {
    'legend': 'sua legenda',
    'inputs': [
        {'name': 'nome', 'type': 'text', 'label': 'nome'},
        {'name': 'email', 'type': 'email', 'label': 'email'},
        {'name': 'senha', 'type': 'password', 'label': 'senha'},
    ],
    'button': {'text': 'enviar', 'Class': 'btn btn-primary btn-block'},
}

>>> form(form_spec)

"""
from browser import document
from browser.html import DIV, FIELDSET, FORM, INPUT, LABEL, LEGEND


def _create_input(
    name, type, label='', Class='', text='', value='', required=False,
):
    """
    Cria um input completo.

    Baseados nas implementações do CSS, insere uma div `form-group`
    um input e um label

    Args:
    ----
        name: id do input
        type: tipo do input
        label: texto do label
        Class: classe CSS
        text: texto do componente
        value: valur do componente
        required: input validator required

    Retorna uma div do grupo com o elemto inserido na div.

    Example:
    -------
    >>> _create_input('nome', 'text', 'Seu nome')

    <div class="form-group">
        <label for="nome"> Seu nome </label>
        <input id="nome", type="text">
    </div>

    """
    d = DIV(Class='form-group')
    d <= LABEL(f'{label}: ' if label else '', For=name, id=f'l{name}')
    d <= INPUT(
        text,
        id=name,
        name=name,
        type=type,
        Class=Class,
        value=value,
        required=required,
    )
    return d


def _create_form(things: dict):
    """Cria um form basead em uma especificação de dicionário."""
    fieldset = FIELDSET()
    fieldset <= LEGEND(things['legend'])
    form = FORM(**things['form'])

    for input_ in things['inputs']:
        form <= _create_input(**input_)

    fieldset <= form
    return fieldset


def form(form_spec: dict):
    """
    Isere o dict recebido e inserir no main.

    Example:
    -------
    >>> d = {'legend': 'Faça seu cadastro'}
    >>> form(d)

    """
    document['main'] <= _create_form(form_spec)
