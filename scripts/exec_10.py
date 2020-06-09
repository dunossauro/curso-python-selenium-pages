from browser import document, html, timer
from random import randint
from functools import partial

def error_message():
    if not document.select('.terminal-alert-error'):
        error_div = html.DIV(
            'Preencha corretamente',
            Class='terminal-alert terminal-alert-error',
        )
        form_field = document.select_one('fieldset')
        form_field.insertBefore(error_div, form_field.firstChild)


def clear_error_messages():
    for error in document.select('.terminal-alert-error'):
        error.remove()


def card_elements(event):
    card = event.target.parentNode.parentNode
    error = card.select_one('.btn-error')
    primary = card.select_one('.btn-primary')
    return card, primary, error


def read_form():
    name = document.select_one('#todo-name').value,
    description = document.select_one('#todo-desc').value,
    check = document.select_one('#todo-next').checked
    valid = bool(name[0])

    if not valid:
        error_message()
    else:
        clear_error_messages()

    return name, description, check, valid

def create_card_timer(checked, todo, card):
    if checked:
        todo.insertBefore(card, todo.firstChild)
    else:
        todo <= card

def create_card(event):
    name, desc, checked, valid = read_form()
    if valid:
        todo = document.select_one('#todo')
        card = html.DIV(Class='terminal-card')
        card <= html.HEADER(name)
        card <= html.DIV(desc)
        buttons = html.DIV(Class='buttons')
        do = html.BUTTON('Fazer', Class='btn btn-primary btn-ghost do')
        cancel = html.BUTTON('Cancelar', Class='btn btn-error btn-ghost cancel')

        do.bind('click', doing_card)
        cancel.bind('click', cancel_card)

        buttons <= do
        buttons <= cancel
        card <= buttons

        timer.set_timeout(
            partial(create_card_timer, checked, todo, card),
            randint(1, 3000)
        )


def doing_card_timer(card):
    document.select_one('#doing') <= card


def doing_card(event):
    card, primary, error = card_elements(event)
    primary.text = 'Pronto'
    error.text = 'Voltar'

    primary.unbind('click', doing_card)
    primary.bind('click', done_card)

    error.unbind('click', cancel_card)
    error.bind('click', back_card)

    timer.set_timeout(partial(doing_card_timer, card), randint(1, 3000))


def cancel_card(event):
    card = event.target.parentNode.parentNode
    card.remove()


def back_card(event):
    card, primary, error = card_elements(event)
    primary.text = 'Fazer'
    error.text = 'Cancelar'

    primary.unbind('click', done_card)
    primary.bind('click', doing_card)

    error.unbind('click', back_card)
    error.bind('click', cancel_card)

    document.select_one('#todo') <= card



def done_card(event):
    card, primary, error = card_elements(event)
    error.remove()
    primary.text = 'Refazer'
    primary.bind('click', redo)
    primary.unbind('click', done_card)
    document.select_one('#done') <= card


def redo(event):
    card, primary, error = card_elements(event)
    iternal_div = card.select('div')[1]

    error = html.BUTTON(
        'Cancelar', Class='btn btn-error btn-ghost cancel'
    )
    error.bind('click', cancel_card)
    iternal_div <= error

    primary.text = 'Fazer'
    primary.unbind('click', redo)
    primary.bind('click', doing_card)

    document.select_one('#todo') <= card
