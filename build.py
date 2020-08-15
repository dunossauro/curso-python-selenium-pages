"""Script de build, para montar o site."""
from template_engine import build_path, clean_and_copy

clean_and_copy()

page_paths = ['paginas/aulas', 'paginas/stuff_pages', 'paginas/exercicios']

for path in page_paths:
    build_path(path)
