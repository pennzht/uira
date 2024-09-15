Uira
===

__Uira__ is a text editor by [Tianguang](https://github.com/pennzht) as a hobby project.

The editor was used to create __n2__ (see `./n2/n2`) during a demo. The branch `demo` contains the __exact version__ of Uira and n2 by the end of the presentation (identical); Uira was written in less than one month, and n2 in one hour.

The branch `main` contains improvements after the demo.

Usage
---

1. Clone the project.
2. Ensure the file `uira` is executable.
3. Add the project directory to `$PATH`
4. Run `uira <file_name_1> ... <file_name_n>`
5. Use Ctrl+Q to quit.

Python is required (3.10.4 is sufficient).

You might need to adjust certain parts of the code to run it on your machine.

Disclaimer
---

This is a personal project, licensed under GPL. The source code is presented here in full. While this software is made without any malice (and I run it on my own machine), it is prone to bugs like almost every piece of software. __Use at your own risk.__

Issues and Pull requests
---

Bug reports are welcome! Please include relevant information such as OS, Python version, and the mode the editor was in when the bug happened.

Unfortunately, I cannot accept pull requests, at least for now.

Roadmap
---

Due to personal plans,
- Development will be paused from 2024-09-12 to 2024-09-23.
- Development may be continued from 2024-09-24 to 2024-12-31, but very slowly.
- Development may continue normally starting 2025-01-01.

Next plans:

1. Important basic features
    - Add testing
    - Replace
    - Open files while in editor
    - Suspending the editor (to use the shell)
    - Directory/project navigation
    - Save as copy
    - Ask to save on quit
2. Fixes
    - Support large files
    - Better support for multiple windows
    - Better clipboard info
3. Productivity features
    - Projects
    - Trailing space removal
    - Multiple cursors
    - Regex search/replace
    - Text transformation (e.g. capitalize)
    - Undo tree
    - Native clipboard interop
    - Spellcheck
    - Extensibility (e.g. macros)
    - Wrap by word
    - Code folding
    - Parentheses matching
    - Stats (e.g. word count)
    - More syntax highlighting
    - Organizer mode (similar to: Org mode)

Name
---

[Uira](https://en.wiktionary.org/wiki/uira) means __lightning, electricity__ in Maori and Tahitian.

