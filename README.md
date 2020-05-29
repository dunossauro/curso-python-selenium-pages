[![Netlify Status](https://api.netlify.com/api/v1/badges/72784331-9ed0-4160-bec3-d5763deb3ce2/deploy-status)](https://app.netlify.com/sites/curso-python-selenium/deploys)

# Páginas do curso de python com selenium

site: https://curso-python-selenium.netlify.com/


#### Páginas feitas usando
terminal CSS: http://terminalcss.xyz/

Brython: https://brython.info/

Jinja2: https://jinja.palletsprojects.com/


## Estrutura do projeto
| Path            | o que tem dentro | observação                                         |
| --------------- | ---------------- | -------------------------------------------------- |
| css             | Arquivos .css    | Estilo das páginas do curso                        |
| js              | Arquivos .js     | Código fonte do brython em JS                      |
| scripts         | Arquivos .py     | código bryhton que é reutilizado nas páginas       |
| raw_pages*      | Arquivos .html   | Arquivos HTML que serão copiados sem processamento |
| templates       | Arquivos .html   | templates do jinja                                 |
| template_engine | Arquivos .py     | código python para gerar templates                 |
| aulas           | Arquivos .py     | código usado para gerar a página da aula           |


> Raw_pages também tem código brython, porém não será reutilizado

## como buildar o projeto

```sh
python -m venv venv
./venv/bin/activate

pip install -r requirements.txt

python build.py
```

## Para servir o código e testar as páginas
```sh
# obs o build deve ter sido feito anteriormente

python -m http.server --directory site/
```


## Lições aprendidas

1. A estrutura deveria ser repensada (o código brython está espalhado pelo projeto)
2. A ideia do template_engine parecia uma boa ideia no início, mas logo ela se tornou cara de mais e ficou tudo muito genérico
3. raw_pages deveriam ser o padrão e todo código brython deveria estar disponível pra elas.
4. Página sempre em html, nunca em full brython (maior erro do projeto até agora)
