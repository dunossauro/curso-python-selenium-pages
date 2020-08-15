from browser import document, html
from scripts.links import anchor_in_list

document['main'] <= html.H1('Você está no exercício 3')
document['main'] <= anchor_in_list('Começar por aqui', 'page_1.html')
