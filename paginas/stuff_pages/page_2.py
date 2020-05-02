from browser import html, document
from scripts.links import anchor_in_list


document['main'] <= html.H1('Você está na página 2')
document['main'] <= html.P('Responda ao certo ou o diabão vai te pegar')
document['main'] <= html.P('Qual o título dessa página?')
document['main'] <= anchor_in_list('page_2.html', 'page_3.html', 'certo')
document['main'] <= anchor_in_list('Exercício 3.html', 'diabao.html', 'errado')
