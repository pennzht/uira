# Python syntax highlighting

# Default = 0

# Red = 1
keywords_red = set('''
    and as assert async await break class continue def
    del elif else except finally for from global if
    import in is lambda nonlocal not or pass raise return
    try while with yield
'''.split())

# Orange = 2
keywords_orange = set('''
    True False None self __init__ __name__
'''.split())

# Purple = 3
keywords_purple = set('''
    bool int float complex
    str bytes
    list tuple dict set object range
    min max curses
'''.split())

keywords = {}
for (kwset, number) in [(keywords_red, 1), (keywords_orange, 2), (keywords_purple, 3)]:
    for elem in kwset:
        keywords[elem] = number

# Digits: blue = 4
# Strings: green = 5
# Comments: gray = 6

import curses
from colors import *

import re

def show_coloring (text, filename):
    if not (text.startswith('#!') or filename.endswith('.py')):
        finds = list(re.finditer ("[A-Za-z0-9_]+", text))
        return [0] * len(text), finds

    ans = [0] * len (text)
    finds = list(re.finditer ("""'[^']*'|"[^"]*"|[#][^\n]*|[A-Za-z0-9_]+""", text))

    for find in finds:
        (start, stop) = find.span()
        word = find.group(0)

        color = 0

        if '0' <= word[0] <= '9':
            # Digit
            color = 4  # Digits
        elif word[0] in ['"', "'"]:
            # String
            color = 5  # Strings
        elif word[0] == '#':
            color = 6
        else:
            color = keywords.get(word, 0)

        if color:
            for i in range (start, stop):
                ans[i] = color

    return ans, finds
