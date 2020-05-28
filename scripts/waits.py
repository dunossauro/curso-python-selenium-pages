from browser import document, bind, html, timer
from functools import partial

def wait_load(aula):
    document.select_one('#request').bind('click', create_progress_bar)
    document.select_one('br').remove()
    document.select_one('.terminal-alert-error').remove()
    if aula == '09b':
        document.select_one('#request').style.pointerEvents = 'visible'
        document.select_one('#request').classList.remove('btn-error')
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
            'class': "progress-bar-filled",
            'style': {'width': '0%'},
            'data-filled': 'Loading 0%',
            'id': 'bar',
            }
        progress = html.DIV(Class="progress-bar progress-bar-show-percent")
        progress <= html.DIV(**bar_attrs)
        document.select_one('#progress-bar') <= progress

        for value in range(0, 101):
          timer.set_timeout(partial(manage_progress, '#bar', value), value * 50)
