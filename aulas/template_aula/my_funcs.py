from browser import document, html

def my_func():
    document['header'] <= html.H3('Header via Brython')
    document['aside'] <= html.P('aside via Brython')
    document['main'] <= html.P('main via Brython')
    document['footer'] <= html.P('footer via Brython')
