from browser import document
from browser.html import (
    HEADER, FOOTER, MAIN, ASIDE,
    NAV, DIV,
    P, A, UL, LI
)

def page_structure():
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
    container = DIV(Class='container')
    terminal_nav = DIV(Class='terminal-nav')
    header = DIV(Class='terminal-logo', id='header')
    terminal_menu = NAV(Class='terminal-menu')
    logo = DIV(Class='logo terminal-prompt')
    link_logo = A('Olar jovis :)', Class='no-style')
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
    document['footer'] <= P('footer')

def page_load():
    page_structure()
    header()
    aside()
    main()
    footer()
    
def nav_element(name, link):
    li_element = LI()

    element = A(name, Class='menu-item')
    element.target = '_blank'
    element.href = link

    li_element <= element
    return li_element
