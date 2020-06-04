from browser import document, html


def card_elements(event):
    card = event.target.parentNode.parentNode
    error = card.select_one('.btn-error')
    primary = card.select_one('.btn-primary')
    return card, primary, error


def read_form():
    return (
        document.select_one('#todo-name').value,
        document.select_one('#todo-desc').value,
        document.select_one('#todo-next').checked
    )


def create_card(event):
    name, desc, checked = read_form()
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

    if checked:
        todo.insertBefore(card, todo.firstChild)
    else:
        todo <= card


def doing_card(event):
    card, primary, error = card_elements(event)
    primary.text = 'Pronto'
    error.text = 'Voltar'

    primary.unbind('click', doing_card)
    primary.bind('click', done_card)

    error.unbind('click', cancel_card)
    error.bind('click', back_card)

    document.select_one('#doing') <= card


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
