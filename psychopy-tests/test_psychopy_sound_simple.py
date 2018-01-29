from psychopy import visual, core, event, sound

win = visual.Window()
text = visual.TextStim(win, text='Hello world!')
text.draw()
win.flip()
core.wait(1.0)

text.setText('Press X to play sound')
text.draw()
win.flip()
event.waitKeys(keyList=['x'])
snd = sound.Sound('telephone-ring.wav')
snd.play()
core.wait(1.0)
