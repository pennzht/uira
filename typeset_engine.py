from unicode_supp import *
from common import *
from py_syntax import *

def typeset (window):
    lines = [[]]
    chars = []

    # Keep track of logical line:column too.
    ll, lc = 1, 1  # 1-based, from tradition
    y, x = 0, 0

    data = window.text_file.entire_colored_text()
    height = window.height
    width = window.width

    # '' is a sentinel value.
    for pos, colorchar in enumerate([*data, ColoredChar('', (5,))]):
        ch = colorchar.ch
        char_width = (1 if ch == '\n' else
                      1 if ch == '' else
                      chwidth (ch))

        # Break line if too wide
        if len (lines[-1]) + char_width > width:
            lines.append([])
            y += 1
            x = 0

        char = Char (ch, pos, ll, lc, y, x, colorchar.meta)
        chars.append(char)

        # Advance logical line:column
        if ch == '\n':
            ll += 1
            lc = 1
        else:
            lc += 1

        # Append to line.
        lines[-1].append (char)
        x += char_width

        # Break line if needed
        if ch == '\n':
            lines.append([])
            y += 1
            x = 0

    # Coloring info
    text = ''.join (char.ch for char in data)
    coloring, word_matches = show_coloring (text, window.text_file.id)

    window.chars = chars
    window.text_file.coloring = coloring

    # Set word matches to window, to help with suggestion
    window.word_matches = word_matches
