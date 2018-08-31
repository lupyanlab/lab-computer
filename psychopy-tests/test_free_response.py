#!/usr/bin/env python
import string
from psychopy import visual, event, core

win = visual.Window(units='pix')
text_box = visual.TextStim(win, text='', pos=(-100, 0), alignHoriz='left', wrapWidth=200)

typing = True
is_cap = False
message = ''
while typing:
    keys = event.getKeys()
    if keys:
        key = keys[0]

        if key == 'return':  # bit.ly/pyglet-key-names
            typing = False
            continue
        elif key in ['lshift', 'rshift']:
            is_cap = True
            continue
        elif key == 'space':
            key = ' '
        elif key == 'backspace':
            message = message[:-1]
            key = ''
        elif key not in string.letters:
            continue

        if is_cap:
            key = key.upper()
            is_cap = False

        message += key
        text_box.setText(message)

    text_box.draw()
    win.flip()

core.quit()
