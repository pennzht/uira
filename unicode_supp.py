import unicodedata
import dataclasses
from common import *

@dataclasses.dataclass
class Char:
    ch: str
    pos: int
    ll: int
    lc: int
    y: int
    x: int
    meta: object = None

@dataclasses.dataclass
class ColoredChar:
    ch: str
    meta: object = None

    # Meta is one of:
    # None                         // default, absence of other thing
    # (1, 'type')                  // 1 = insert
    # (1, 'snip')                  // snippet
    # (2,)                         // 2 = comment
    # (3,)                         // 3 = overwrite
    # (4, 'orig', file-name)       // 4 = original
    # (4, 'copy', file-name)       // copied, including from self
    # (4, 'move', file-name)       // moved
    # (5,)                         // end-of-file sentinel

def getkey(sc):
    # Aliases common emacs keys.
    key = getkey_untranslated(sc)
    return {
        ctrl('A'): 'KEY_HOME',
        ctrl('E'): 'KEY_END',
        ctrl('F'): 'KEY_RIGHT',
        ctrl('B'): 'KEY_LEFT',
        ctrl('P'): 'KEY_UP',
        ctrl('N'): 'KEY_DOWN',
        ctrl('H'): 'KEY_BACKSPACE',
        ctrl('D'): 'KEY_DC',
    }.get(key, key)

def getkey_untranslated(sc):
    if 'Yes':
        meta = ''

        key = sc.getkey()

        if key == '\x1B':
            meta = 'Meta+'
            key = sc.getkey()

        if len (key) != 1: return meta+key    # Special keys
        if ord (key) >= 256: return meta+key    # Special key codes

        k1 = ord(key)
        if 0 <= k1 <= 0x7F: return meta+key    # Ascii

        if 0xC0 <= k1 <= 0xDF:
            # 2-byte UTF-8
            k2 = ord(sc.getkey())
            val = k1 & 0x1F
            val <<= 6
            val |= k2 & 0x3F
        elif 0xE0 <= k1 <= 0xEF:
            # 3-byte UTF-8
            k2 = ord(sc.getkey())
            k3 = ord(sc.getkey())
            val = k1 & 0x0F
            val <<= 6
            val |= k2 & 0x3F
            val <<= 6
            val |= k3 & 0x3F
        elif 0xF0 <= k1 <= 0xF7:
            # 4-byte UTF-8
            k2 = ord(sc.getkey())
            k3 = ord(sc.getkey())
            k4 = ord(sc.getkey())
            val = k1 & 0x07
            val <<= 6
            val |= k2 & 0x3F
            val <<= 6
            val |= k3 & 0x3F
            val <<= 6
            val |= k4 & 0x3F
        else:
            return meta+key

        return meta+chr(val)

def is_print_ascii (ch):
    return len (ch) == 1 and (' ' <= ch <= '~' or ch in ['\t', '\n'])

def is_print_char (ch):
    return len (ch) == 1 and (' ' <= ch <= '~' or ch in ['\t', '\n'] or ord (ch) >= 128)

def norm (ch):
    if ch == '': return '#'
    return ch if is_print_ascii (ch) or ord(ch) >= 128 else '?'

def chwidth (ch):
    group = unicodedata.east_asian_width (ch)
    return {'F': 2, 'W': 2, 'N': 1, 'Na': 1, 'H': 1, 'A': 1}[group]

def ctrl (key):
    return chr (ord (key) & 0x1F)

