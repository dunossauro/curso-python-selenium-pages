from browser import html, document
from browser.local_storage import storage
from scripts.links import anchor_in_list


if storage['local'] != 'fim':
    storage['local'] = 'fim'
    document['main'] <= html.P(
        'O diabão vai te pegar, dê refresh para pedir ajuda'
    )
    document['main'] <= html.PRE(r'''

    Sou o Diabão e você perdeu

       ,    ,    /\   /\
      /( /\ )\  _\ \_/ /_
      |\_||_/| < \_   _/ >
      \______/  \|0   0|/
        _\/_   _(_  ^  _)_
       ( () ) /`\|V"""V|/`\
         {}   \  \_____/  /
         ()   /\   )=(   /\
         {}  /  \_/\=/\_/  \

    ''')
else:
    document['main'] <= html.PRE(r'''

    Sou o unicórnio da salvação

                   \
                    \\
                     \%,     ,'     , ,.
                      \%\,';/J,";";";;,,.
         ~.------------\%;((`);)));`;;,.,-----------,~
        ~~:           ,`;@)((;`,`((;(;;);;,`         :~~
       ~~ :           ;`(@```))`~ ``; );(;));;,      : ~~
      ~~  :            `X `(( `),    (;;);;;;`       :  ~~
     ~~~~ :            / `) `` /;~   `;;;;;;;);,     :  ~~~~
    ~~~~  :           / , ` ,/` /     (`;;(;;;;,     : ~~~~
      ~~~ :          (o  /]_/` /     ,);;;`;;;;;`,,  : ~~~
       ~~ :           `~` `~`  `      ``;,  ``;" ';, : ~~
        ~~:                             `'   `'  `'  :~~
         ~`-----------------------------------------`~


    E você ganhou esse jogo
    ''')
