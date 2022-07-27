#!/usr/bin/python3
"""A module containing a function that indents at special characters.

>>> text_indentation('''Lorem ipsum dolor sit amet, consectetur adipiscing el.
... Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere?
... Non autem hoc:''')
Lorem ipsum dolor sit amet, consectetur adipiscing el.
<BLANKLINE>
Quonam modo?
<BLANKLINE>
Utrum igitur tibi litteram videor an totas paginas commovere?
<BLANKLINE>
Non autem hoc:
<BLANKLINE>

"""


def text_indentation(text):
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == " " and flag == 1:
            continue
        flag = 0
        print(char, end="")
        if char == ":" or char == "." or char == "?":
            flag = 1
            print("\n")
