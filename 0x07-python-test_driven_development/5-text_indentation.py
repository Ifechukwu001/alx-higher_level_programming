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
    if type(text) is not str:
        raise TypeError("text must be a string")
    words = text.split()
    for word in words:
        print("{}".format(word), end="")
        if word.endswith(":") or word.endswith(".") or word.endswith("?"):
            print("\n")
        elif word is not words[-1]:
            print(end=" ")
