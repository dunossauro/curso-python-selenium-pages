from browser import document
from browser.html import LI, NAV, UL, A


def list_link(text, link):
    li_element = LI()

    element = A(text)
    element.target = '_blank'
    element.href = link

    li_element <= element
    return li_element


def html_nav_list(where, *elements):
    """
    Cria links para uma lista.

    Parans:
       - text: texto que aparecerá no link
       - link: href
    """
    nav = NAV()
    ul = UL()

    for element in elements:
        ul <= list_link(*element)

    nav <= ul
    document[where] <= nav
