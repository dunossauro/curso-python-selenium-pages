from browser import document, html
from browser.local_storage import storage
from scripts.links import anchor_in_list

storage['local'] = 'Página 3'


document['main'] <= html.H1('Você está na página 3')
document['main'] <= html.P('Responda certo ou o diabão vai te pegar')
document['main'] <= html.P('Qual o final da URL dessa página?')
document['main'] <= anchor_in_list('page_3.html', 'page_4.html')
document['main'] <= anchor_in_list('bage_3.html', 'diabao.html')
