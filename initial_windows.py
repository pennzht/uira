# Initial windows for helper display.

helper = '''\
⚡ Welcome to Uira ⚡

0 = black, 1 = red, 2 = green, 3 = yellow, 4 = blue, 5 = magenta, 6 = cyan, 7 = white

              ==== Navigation ====
^Q            quit
↑ / ^P        move up
↓ / ^N        move down
← / ^B        move left
→ / ^F        move right
:b            move left one word
:f            move right one word
Home / ^A     beginning of line
End / ^E      end of line
PageUp        move one screen up
PageDown      move one screen down
:<            beginning of file
:>            end of file
:t            bring cursor to top
:m            bring cursor to middle
:8            move to next comment/bookmark
^G            find mode
    → / ↓ / Tab    ⇒ find next
    ^G / :. / Ret  ⇒ exit find mode
^L            go to line
    ^L             ⇒ exit gotoline mode
:l            de Bruijn leap mode

              ==== Multi-window ====
:R            new window on right
:D            new window below
:!            close other windows
:)            close this window
:n            next window
:N            previous window
:y            next buffer
:Y            previous buffer

              ==== Editing ====
^@            set mark for region
Backsp / ^H   delete char behind, or region
Del / ^D      delete char in front
:Backsp / :h  delete word behind
:d            delete word in front
^X            cut
^C            copy
^V            paste
:v            paste without deleting from clipboard
^U            undo
^Y            redo
:*            move to next ✷ and remove it
:c            comment mode
:C            insert ✷
Ret           new line and indent
:Ret          ≡ End + Ret
:o / :]       indent
:u / :[       dedent
:i            insert shortcut
^S            save
'''

