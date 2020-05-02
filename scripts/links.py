from browser import html


def anchor_in_list(name, href, attr=''):
    li = html.LI()
    anchor = html.A(name, attr=attr)
    anchor.href = href
    li <= anchor
    return li
