"""Crie um script que jogue o jogo.

Quando você ganhar o script deve parar de ser executado
"""
from browser import document, html
from random import randint
from browser.local_storage import storage


storage['esperado'] = str(randint(1, 10))
storage['ganhou'] = '0'


def sorteia_numero(_):
    """Função que faz o sorteio do número."""
    numero = str(randint(1, 10))
    if storage['ganhou'] == '1':
        document <= html.P('você está fazendo algo errado', error='error')
        return

    if numero == storage['esperado']:
        document <= html.P(f'Você ganhou: {numero}')
        storage['ganhou'] = '1'
        return

    document <= html.P(numero)


document <= html.H1('Joguinho maneiro')
document <= html.H2('Regras')
document <= html.P(
    '''Você tem um "número esperado", e deve clicar em "clique aqui"
até o resultado ser igual ao número esperado'''
)
document <= html.P(f'Numero esperado: {storage["esperado"]}')


document <= html.A('clique aqui', id='ancora', href='#')


document['ancora'].bind('click', sorteia_numero)
