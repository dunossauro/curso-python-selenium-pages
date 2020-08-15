from browser import document
from browser.html import DIV, FIELDSET, LEGEND, TEXTAREA


def result():
    result_fildset = FIELDSET(Class='result')
    result_fildset <= LEGEND('Resultado')
    result_fildset <= DIV(id='result')

    document['grid'] <= result_fildset


def get_query_string(fields: list, where='result') -> dict:
    fields = {field: document.query.getvalue(field) for field in fields}
    if any(fields.values()):
        textarea = TEXTAREA()
        textarea.text = fields
        if where == 'result':
            result()
        document[where] <= textarea
