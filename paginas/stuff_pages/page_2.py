from string import ascii_lowercase as alpha
from random import choice
from browser import html, document
from scripts.links import anchor_in_list

title = ''.join(choice(alpha) for n in range(10))

document.title = title
document['main'] <= html.H1('Você está na página 2')
document['main'] <= html.P('Responda certo ou o diabão vai te pegar')
document['main'] <= html.P('Qual o título dessa página?')
document['main'] <= anchor_in_list(title, 'page_3.html', 'certo')
document['main'] <= anchor_in_list('page_2.html', 'diabao.html', 'errado')
