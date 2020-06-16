from browser import window, document, html


def alerts(event):
    response = False
    name = ''

    window.alert('Isso é um alerta!!')

    while not response and not name:
        name = window.prompt('Digite seu nome')
        response = window.confirm('Esse é mesmo o seu nome?')

    document.select_one('.body_b') <= html.H1(f'Olar {name}')
    document.select_one('.body_b') <= html.BR()
