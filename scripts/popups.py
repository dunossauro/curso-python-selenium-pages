from browser import window, document, html


def alerts(event):
    response = False
    name = ''

    window.alert('Isso é um alerta!!')

    while not (response and name):
        name = window.prompt('Digite seu nome')
        msg = 'Seu nome é vazio. Vamos refazer a operação'
        if name:
            msg = 'Esse é mesmo o seu nome?'

        response = window.confirm(msg)

    document.select_one('.body_b') <= html.H1(f'Olar {name}')
    document.select_one('.body_b') <= html.BR()

def popup(event):
    window.open('popup.html', 'popup', 'scrollbars=no')


def tabs(event):
    window.open('#', '_blank')
