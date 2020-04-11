# Páginas do curso de python com selenium

site: https://curso-python-selenium.netlify.com/


#### Páginas feitas usando
terminal CSS: http://terminalcss.xyz/

Brython: https://brython.info/

Jinja2: https://jinja.palletsprojects.com/


## Estrutura do projeto
| Path            | o que tem dentro | observação                               |
| --------------- | ---------------- | ---------------------------------------- |
| css             | Arquivos .css    |                                          |
| js              | Arquivos .js     |                                          |
| scripts         | Arquivos .py     | código bryhton                           |
| templates       | Arquivos .html   | templates do jinja                       |
| template_engine | Arquivos .py     | código python para gerar templates       |
| aulas           | Arquivos .py     | código usado para gerar a página da aula |


## como buildar o projeto

```sh
python -m venv venv
./venv/bin/activate

pip install -r requirements.txt

python build.py
```
