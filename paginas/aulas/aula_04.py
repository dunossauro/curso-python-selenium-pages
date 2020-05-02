from browser import html, document
from scripts.links import anchor_in_list


lista_exercicios = html.UL()
for n in range(1, 11):
    lista_exercicios <= anchor_in_list(f'Exercício {n}', f'exercicio_0{n}.html')


lista_aulas = html.UL()
for n in range(3, 10):
    lista_aulas <= anchor_in_list(f'Aula {n}', f'aula_0{n}.html')

document['aside'] <= html.H1('Lista de Aulas')
document['aside'] <= lista_aulas

document['main'] <= html.H1('Lista de exercícios')
document['main'] <= lista_exercicios
