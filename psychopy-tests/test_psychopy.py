from psychopy import visual, core, event

win = visual.Window()
text = visual.TextStim(win, text='Hello world!')
text.draw()
win.flip()
core.wait(1.0)

text.setText('Press X to quit')
text.draw()
win.flip()
event.waitKeys(keyList=['x'])
