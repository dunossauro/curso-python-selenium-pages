from browser import document, html
from browser.local_storage import storage

storage['contagem'] = '0'


def increment(_):
    """Pega o valor no storage, incrimenta e adiciona no document."""
    storage['contagem'] = str(int(storage['contagem']) + 1)
    document <= html.P(storage['contagem'])


"""Estrutura inicial da página.

Link + valor inicial em P
"""
document <= html.A('minha ancora', id='ancora', href='#')
document <= html.P(storage['contagem'])
# executa increment quando clicamos no link
document['ancora'].bind('click', increment)
