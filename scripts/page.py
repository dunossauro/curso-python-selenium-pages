"""
Módulo repsonsáve pela implementação default de todas as páginas.

As funções, footer, header, aside e main são carregas por padrão em
todas as páginas do projeto, baseado na implementação do componente
`templates/components/bryhton.html`

Example:
-------
>>> from scripts.page import page_load
>>> page_load()  # carrega todos os elementos

"""
from browser import document
from browser.html import NAV, DIV, A, UL, LI


def page_load():
    """Agrupa todos os elementos em uma única chamada do brython."""
    header()
    aside()
    main()
    footer()


def footer():
    """Footer que será usado em todas as páginas."""
    ...


def aside():
    """Aside que será usado em todas as páginas."""
    ...


def main():
    """Main que será usado em todas as páginas."""  # NOQA
    ...


def header():
    """
    Footer que será usado em todas as páginas.

    A implementação desse header está baseada na implementação do terminal CSS

    Foi feita uma cópia do header princial e resontruíuda em bryhton.
    link: https://terminalcss.xyz/dark/#Navigation
    """
    div_container = DIV(Class='container')
    terminal_nav = DIV(Class='terminal-nav')
    header = DIV(Class='terminal-logo', id='header')
    terminal_menu = NAV(Class='terminal-menu')
    logo = DIV(Class='logo terminal-prompt')
    link_logo = A('Olar Jovis :)', Class='no-style')
    link_logo.link = '#'

    ul = UL()
    youtube = nav_element('Youtube', 'https://www.youtube.com/eduardomendes')
    apoiase = nav_element('Apoia.se', 'https://apoia.se/livedepython')
    curso = nav_element(
        'Curso', 'https://dunossauro.github.io/curso-python-selenium'
    )
    cdc = nav_element(
        'CDC',
        'https://github.com/dunossauro/curso-python-selenium/blob/master/cdc.md', # NOQA
    )

    logo <= link_logo
    header <= logo
    ul <= youtube + apoiase + curso + cdc
    terminal_menu <= ul
    terminal_nav <= header
    terminal_nav <= terminal_menu
    div_container <= terminal_nav
    document['header'] <= div_container


def nav_element(text, link):
    """
    Cria links para uma lista.

    Parans:
       - text: texto que aparecerá no link
       - link: href
    """
    li_element = LI()

    element = A(text, Class='menu-item')
    element.target = '_blank'
    element.href = link

    li_element <= element
    return li_element
