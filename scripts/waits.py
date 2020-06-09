from browser import document, bind, html, timer
from functools import partial
from random import randint, choice


def create_btn(where, text, classes):
    document.select_one(where) <= html.BUTTON(
        text,
        Class=classes,
        id='request',
        type='button',
        name='button'
    )


def exercice_08():
    r_value = randint(1, 50)
    def btn_creates(index):
        btn = document.select('#request')
        if btn:
            btn[0].remove()
        classes = f'btn btn-{choice(["default", "primary", "error"])} btn-ghost'
        if index == r_value:
            classes += ' selenium'
            print('selenium')
        create_btn('fieldset', 'Botão', classes)

    document.select_one('.terminal-alert-error').remove()
    fieldset = document.select_one('fieldset')
    fieldset <= html.P(
        'Encontre a classe .selenium no elementos que estão surgindo'
    )
    for index in range(0, 51):
        timer.set_timeout(partial(btn_creates, index), index * 500)

def wait_load(aula):
    document.select_one('#request').bind('click', create_progress_bar)
    document.select_one('br').remove()
    document.select_one('.terminal-alert-error').remove()
    if aula == '09b':
        document.select_one('#request').style.pointerEvents = 'visible'
        document.select_one('#request').classList.remove('btn-error')
        document.select_one('#request').classList.remove('unclick')
        document.select_one('#request').classList.add('btn-primary')

def manage_progress(id, percent):
    bar = document.select_one(id)
    bar.style.width = f'{percent}%'
    bar['data-filled'] = f'Loading {percent}%'

    if percent == 0:
        text = document.select_one('#finished')
        text.remove()

    if percent == 100:
        progress_bar = document.select_one('#progress-bar')
        progress_bar.clear()
        progress_bar <= html.BR()
        alert = html.DIV(
            'Carregamento concluído',
            ID='finished',
            Class='terminal-alert'
        )
        alert.style.color = '#08D10E'
        alert.style.borderColor = '#08D10E'
        progress_bar <= alert


def create_progress_bar(event):
    if not document.select('.progress-bar'):
        bar_attrs = {
            'class': 'progress-bar-filled',
            'style': {'width': '0%'},
            'data-filled': 'Loading 0%',
            'id': 'bar',
            }
        progress = html.DIV(Class='progress-bar progress-bar-show-percent')
        progress <= html.DIV(**bar_attrs)
        document.select_one('#progress-bar') <= progress

        for value in range(0, 101):
          timer.set_timeout(partial(manage_progress, '#bar', value), value * 50)
