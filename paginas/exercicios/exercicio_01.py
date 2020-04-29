"""
Crie um programa com selenium que

- Gere um dicionário, onde a chave é a Tag h1
- O valor deve ser um novo dicionário
-- cada chave do valor deverá ser o valor de 'atributo'
-- cada valor deve ser o texto contído no elemento

"""
from browser import document, html


document <= html.H1('Boas vindas')
document <= html.P('Essa página é top de mais', atributo='texto1')
document <= html.P(
    'E eu vou pegar todos os dados com selenium', atributo='texto2'
)
document <= html.P('Pq aqui não é brincadeira', atributo='texto3')
