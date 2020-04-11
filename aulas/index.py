from scripts.lists import html_nav_list
from browser import document
from browser.html import H2

document['main'] <= H2('Lista de aulas')

html_nav_list('main', ('- Aula 3', '/aula_3.html'))
