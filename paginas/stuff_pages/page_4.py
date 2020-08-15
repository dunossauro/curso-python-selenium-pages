from browser import document, html
from browser.local_storage import storage
from scripts.arts import art

if storage['local'] != 'fim':
    storage['local'] = 'fim'
    document['main'] <= html.P(
        'O diabão vai te pegar, dê refresh para pedir ajuda'
    )
    document['main'] <= art('diabo', 'Sou o Diabão e você perdeu', '')
else:
    document['main'] <= art(
        'unicornio', 'Sou o unicórnio da salvação', 'E você ganhou esse jogo'
    )
