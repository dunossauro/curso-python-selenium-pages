from browser import html, document
from scripts.links import anchor_in_list


lista_exercicios = html.UL()
for n in range(1, 8):
    lista_exercicios <= anchor_in_list(
        f'Exercício {n}', f'exercicio_0{n}.html'
    )


lista_aulas = html.UL()
for n in range(3, 8):
    lista_aulas <= anchor_in_list(f'Aula {n}', f'aula_0{n}.html')

document['aside'] <= html.H1('Lista de Aulas')
document['aside'] <= lista_aulas
paginas_praticar = html.UL()

document['aside'] <= html.H1('Páginas para praticar')
paginas_praticar <= anchor_in_list('Caixinha', 'caixinha.html')
paginas_praticar <= anchor_in_list('Teclado', 'keyboard.html')
paginas_praticar <= anchor_in_list('Logger', 'logger.html')
paginas_praticar <= anchor_in_list('Drag n Drop', 'drag.html')
document['aside'] <= paginas_praticar

document['main'] <= html.H1('Lista de exercícios')
document['main'] <= lista_exercicios

lista_explicacoes = html.UL()
document['main'] <= html.H1('Páginas de explicação')
lista_explicacoes <= anchor_in_list('Aula 4a', 'aula_04_a.html')
lista_explicacoes <= anchor_in_list('Aula 4b', 'aula_04_b.html')
lista_explicacoes <= anchor_in_list('Aula 5a', 'aula_05_a.html')
lista_explicacoes <= anchor_in_list('Aula 5b', 'aula_04_b.html')
lista_explicacoes <= anchor_in_list('Aula 5c', 'aula_04_c.html')
lista_explicacoes <= anchor_in_list('Aula 6a', 'aula_06_a.html')
lista_explicacoes <= anchor_in_list('Aula 7a', 'aula_07_a.html')
lista_explicacoes <= anchor_in_list('Aula 7b', 'aula_07_b.html')
lista_explicacoes <= anchor_in_list('Aula 7c', 'aula_07_c.html')
lista_explicacoes <= anchor_in_list('Aula 7d', 'aula_07_d.html')
lista_explicacoes <= anchor_in_list('Aula 8a', 'aula_08_a.html')
lista_explicacoes <= anchor_in_list('Aula 8b', 'aula_08_b.html')
lista_explicacoes <= anchor_in_list('Aula 9a', 'aula_09_a.html')
lista_explicacoes <= anchor_in_list('Aula 9b', 'aula_09_b.html')
document['main'] <= lista_explicacoes
