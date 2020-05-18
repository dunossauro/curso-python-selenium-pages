from browser import document, html

events = ['mouseleave', 'mouseenter', 'click', 'dblclick']

colors = ['red', 'yellow', 'blue', 'black']
shift_colors = ['tomato', 'pink', 'aqua', 'darkcyan']
ctrl_colors = ['deeppink', 'greenyellow', 'indigo', 'lightsalmon']
mixed_colors = [
    'mediumorchid',
    'mediumspringgreen',
    'midnightblue',
    'olivedrab',
]

event_color = {key: value for key, value in zip(events, colors)}
event_color_shift = {key: value for key, value in zip(events, shift_colors)}
event_color_crtl = {key: value for key, value in zip(events, ctrl_colors)}
event_color_mixed = {key: value for key, value in zip(events, mixed_colors)}


def box_behavior(event):
    if event.shiftKey and event.ctrlKey:
        color = event_color_mixed[event.type]

    elif event.shiftKey:
        color = event_color_shift[event.type]

    elif event.ctrlKey:
        color = event_color_crtl[event.type]

    else:
        color = event_color[event.type]

    area_output = 'evento:"{}", cor:"{}", shift:{}, ctrl:{}'.format(
        event.type, color, event.shiftKey, event.ctrlKey
    )

    document['caixa'].style.fill = color
    document.select_one('span').text = '{' + area_output + '}'
    try:
        document.select_one('#area').text += '{' + area_output + '}\n'
    except Exception:
        ...


def bind_aula_7():
    document.select_one('#caixa').bind('mouseenter', box_behavior)
    document.select_one('#caixa').bind('mouseleave', box_behavior)
    document.select_one('#caixa').bind('click', box_behavior)
    document.select_one('#caixa').bind('dblclick', box_behavior)
