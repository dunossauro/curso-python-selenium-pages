from browser import document
from browser.html import (
    HEADER, FOOTER, MAIN, ASIDE,
    NAV, DIV,
    P, A, UL, LI
)

def page_structure():
    """Monta a estrutura base da página."""
    page = DIV(Class='components-grid', id='grid')
    page <= HEADER(id='header')
    page <= ASIDE(id='aside')
    page <= MAIN(id='main')
    page <= FOOTER(id='footer')
    document <= page


def aside():
    document['aside'] <= P('aside')

def main():
    document['main'] <= P('main')

def header():
    """Cria navbar no header com o logo e os links."""
    container = DIV(Class='container')
    terminal_nav = DIV(Class='terminal-nav')
    header = DIV(Class='terminal-logo', id='header')
    terminal_menu = NAV(Class='terminal-menu')
    logo = DIV(Class='logo terminal-prompt')
    link_logo = A('Olar Jovis :)', Class='no-style')
    link_logo.link = '#'

    ul = UL()
    youtube = nav_element('Youtube', 'https://www.youtube.com/eduardomendes')
    apoiase = nav_element('Apoia.se', 'https://apoia.se/livedepython')
    curso = nav_element('Curso', 'https://dunossauro.github.io/curso-python-selenium')
    cdc = nav_element('CDC', 'https://github.com/dunossauro/curso-python-selenium/blob/master/cdc.md')

    logo <= link_logo
    header <= logo
    ul <= youtube + apoiase + curso + cdc
    terminal_menu <= ul
    terminal_nav <= header
    terminal_nav <= terminal_menu
    container <= terminal_nav
    document['header'] <= container


def footer():
    ...

def page_load():
    """Monta e estrutura da página."""
    page_structure()
    header()
    aside()
    main()
    footer()


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
