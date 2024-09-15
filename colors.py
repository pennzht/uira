# DARK, light

import curses

colors = {
    'BLACK': 0x000000,
    'white': 0xffffff,

    'RED': 0x831a2a,
    'GREEN': 0x1b4b00,
    'BLUE': 0x004662,
    'PURPLE': 0x511f83,
    'GRAY': 0x3f3f3f,

    'orange': 0xff956f,
    'yellow': 0xe4c800,
    'green': 0x06c000,
    'blue': 0x5ee3f7,
    'purple': 0xdacaf8,
    'gray': 0x9d9d9d,

    'default': -1,
}

col = {}    # color-pair-name to color-pair-index correspondences
syntax_colors = []
db_colors = []

def init_colors ():
    color_list = list(colors)
    next_pair = 0
    default_color = None

    for i, c in enumerate(color_list):
        if c == 'default':
            default_color = i;
            continue

        hex = colors[c]
        curses.init_color (i,
                           (hex >> 16) * 1000 // 255,
                           ((hex >> 8) & 255) * 1000 // 255,
                           (hex & 255) * 1000 // 255,
                           )

    for i, fg in enumerate(color_list):
        for j, bg in enumerate(color_list):
            name = fg + '/' + bg
            idef = i if fg != 'default' else -1
            jdef = j if bg != 'default' else -1
            curses.init_pair (next_pair, idef, jdef)
            col[name] = next_pair
            next_pair += 1

    curses.init_pair (next_pair, -1, -1)  # default
    col['default'] = next_pair
    syntax_colors.extend([
        C('default'),
        C('orange/default') | curses.A_BOLD,
        C('yellow/default'),
        C('purple/default'),
        C('blue/default'),
        C('green/default'),
        C('gray/default') | curses.A_ITALIC,
    ])
    db_colors.extend([
        C('white/GRAY'),
        C('orange/GRAY') | curses.A_BOLD,
        C('yellow/GRAY'),
        C('purple/GRAY'),
        C('blue/GRAY'),
        C('green/GRAY'),
        C('gray/GRAY') | curses.A_ITALIC,
    ])

def C(name):
    return curses.color_pair(col[name])

