"""Script de build, para montar o site."""

from template_engine import clean_and_copy, make_page, build_path

clean_and_copy()

page_paths = ['paginas/aulas', 'paginas/stuff_pages', 'paginas/exercicios']

for path in page_paths:
    build_path(path)
