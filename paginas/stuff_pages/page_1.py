from browser import html, document
from random import randint
from scripts.links import anchor_in_list

val_a = randint(1, 10)
val_b = randint(1, 10)
val_c = val_a * val_b
val_d = val_a-2 * val_b + 1

document['main'] <= html.H1('Você está na página 1')
document['main'] <= html.P('Responda ao contrário ou o diabão vai te pegar')
document['main'] <= html.P(f'{val_a} * {val_b} = ')
if val_c % 2:
    document['main'] <= anchor_in_list(f'{val_c}', 'diabao.html', 'certo')
    document['main'] <= anchor_in_list(f'{val_d}', 'page_2.html', 'errado')
else:
    document['main'] <= anchor_in_list(f'{val_d}', 'page_2.html', 'errado')
    document['main'] <= anchor_in_list(f'{val_c}', 'diabao.html', 'certo')
