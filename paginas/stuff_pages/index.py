from browser import html, document
from scripts.links import anchor_in_list


lista_aulas = html.UL()
for n in range(3, 10):
    if n not in [8]:
        lista_aulas <= anchor_in_list(f'Aula {n}', f'aula_0{n}.html')
document['aside'] <= html.H1('Páginas das aulas')
document['aside'] <= lista_aulas
paginas_praticar = html.UL()

document['aside'] <= html.H1('Páginas para praticar')
paginas_praticar <= anchor_in_list('Caixinha', 'caixinha.html')
paginas_praticar <= anchor_in_list('Teclado', 'keyboard.html')
paginas_praticar <= anchor_in_list('Logger', 'logger.html')
paginas_praticar <= anchor_in_list('Drag n Drop', 'drag.html')
paginas_praticar <= anchor_in_list('TODO list', 'todo_list.html')
document['aside'] <= paginas_praticar

lista_explicacoes = html.UL()
document['aside'] <= html.H1('Páginas de explicação')
lista_explicacoes <= anchor_in_list('Aula 4a', 'aula_04_a.html')
lista_explicacoes <= anchor_in_list('Aula 4b', 'aula_04_b.html')
lista_explicacoes <= anchor_in_list('Aula 5a', 'aula_05_a.html')
lista_explicacoes <= anchor_in_list('Aula 5b', 'aula_05_b.html')
lista_explicacoes <= anchor_in_list('Aula 5c', 'aula_05_c.html')
lista_explicacoes <= anchor_in_list('Aula 6a', 'aula_06_a.html')
lista_explicacoes <= anchor_in_list('Aula 7a', 'aula_07_a.html')
lista_explicacoes <= anchor_in_list('Aula 7b', 'aula_07_b.html')
lista_explicacoes <= anchor_in_list('Aula 7c', 'aula_07_c.html')
lista_explicacoes <= anchor_in_list('Aula 7d', 'aula_07_d.html')
lista_explicacoes <= anchor_in_list('Aula 8a', 'aula_08_a.html')
lista_explicacoes <= anchor_in_list('Aula 8b', 'aula_08_b.html')
lista_explicacoes <= anchor_in_list('Aula 9a', 'aula_09_a.html')
lista_explicacoes <= anchor_in_list('Aula 9b', 'aula_09_b.html')
lista_explicacoes <= anchor_in_list('Aula 10a', 'aula_10_a.html')
lista_explicacoes <= anchor_in_list('Aula 10b', 'aula_10_b.html')
lista_explicacoes <= anchor_in_list('Aula 10c', 'aula_10_c.html')
lista_explicacoes <= anchor_in_list('Aula 10d', 'aula_10_d.html')
lista_explicacoes <= anchor_in_list('Aula 11a', 'aula_11_a.html')
document['aside'] <= lista_explicacoes


aulas_youtube = html.UL()
document['main'] <= html.H1('Vídeos das aulas no youtube')
aulas_youtube <= anchor_in_list('Aula 0 - Abertura', 'https://www.youtube.com/watch?v=PHHXksljGNA')
aulas_youtube <= anchor_in_list('Aula 1a - Configurando ambiente (windows)', 'https://youtu.be/rVCKZcFHu4A')
aulas_youtube <= anchor_in_list('Aula 1b - Configurando ambiente (linux)', 'https://youtu.be/XUeu4ZzQNUI')
aulas_youtube <= anchor_in_list('Aula 2 - O que é selenium', 'https://youtu.be/wiA6PBz0Xu0')
aulas_youtube <= anchor_in_list('Aula 3 - Minha primeira automação', 'https://youtu.be/Pax0jiAcTWs')
aulas_youtube <= anchor_in_list('Aula 4 - Navegação e atributos', 'https://youtu.be/H6D8EFSGml0')
aulas_youtube <= anchor_in_list('Aula 5 - Procurando e interagindo com elementos p.I', 'https://youtu.be/KqNTFAgDTrw')
aulas_youtube <= anchor_in_list('Aula 6 - Procurando e interagindo com elementos p.II', 'https://youtu.be/wF3USvFE67Y')
aulas_youtube <= anchor_in_list('Aula 7 - Eventos p.I (EventListener)', 'https://youtu.be/G5xdDPBKzkI')
aulas_youtube <= anchor_in_list('Aula 8 - Eventos p.II (ActionChains)', 'https://youtu.be/xM8sNio2NkA')
aulas_youtube <= anchor_in_list('Aula 9 - Waits p.I', 'https://youtu.be/tMHf6GZ_y2A')
aulas_youtube <= anchor_in_list('Aula 10 - Waits p.II (Expected Conditions)', 'https://youtu.be/aza1vaq0uns')
# aulas_youtube <= anchor_in_list('Aula 11 - ', '')
# aulas_youtube <= anchor_in_list('Aula 12 - ', '')
# aulas_youtube <= anchor_in_list('Aula 13 - ', '')
# aulas_youtube <= anchor_in_list('Aula 14 - ', '')
# aulas_youtube <= anchor_in_list('Aula 15 - ', '')
# aulas_youtube <= anchor_in_list('Aula 16 - ', '')
# aulas_youtube <= anchor_in_list('Aula 17 - ', '')
# aulas_youtube <= anchor_in_list('Aula 18 - ', '')
# aulas_youtube <= anchor_in_list('Aula 19 - ', '')
document['main'] <= aulas_youtube

palestras_youtube = html.UL()
document['main'] <= html.H1('Palestras durante o curso')
palestras_youtube <= anchor_in_list('Vamos falar de QA - Mariana Elisa', 'https://www.youtube.com/watch?v=TOt6YvONKNA')
palestras_youtube <= anchor_in_list('Conhecendo Xpath - Renne Rocha', 'https://youtu.be/vuLNc2yCNYk')
document['main'] <= palestras_youtube


lista_exercicios = html.UL()
for n in range(1, 12):
    formated_n = f'0{n}' if n < 10 else n
    lista_exercicios <= anchor_in_list(
        f'Exercício {formated_n}', f'exercicio_{formated_n}.html'
    )
document['main'] <= html.H1('Lista de exercícios')
document['main'] <= lista_exercicios

resolucao = html.UL()
document['main'] <= html.H1('Resolução dos exercícios')
resolucao <= anchor_in_list('Live de resolução de exercícios 1', 'https://youtu.be/X73Iyq1M688')
resolucao <= anchor_in_list('Live de resolução de exercícios 2', 'https://youtu.be/iLSgkWdepfA')
document['main'] <= resolucao

links = html.UL()
document['main'] <= html.H1('Links legais')
links <= anchor_in_list('Código de conduta', 'https://github.com/dunossauro/curso-python-selenium/blob/master/cdc.md')
links <= anchor_in_list('Slides De todas as aulas', 'https://github.com/dunossauro/curso-python-selenium/tree/master/slides')
links <= anchor_in_list('Repositório do curso', 'https://github.com/dunossauro/curso-python-selenium/')
links <= anchor_in_list('Código das páginas', 'https://github.com/dunossauro/curso-python-selenium-pages/')
document['main'] <= links
