#!/usr/bin/env python

"""
Sound stimuli are currently an area of development in PsychoPy

Previously we used pygame. Now the dpyo library is also supported.
On OSX this is an improvement (using coreaudio rather than SDL).
On windows this should help on systems with good sound cards,
but this is yet to be confirmed.
See the demo hardware>testSoundLatency too

"""
import sys
from psychopy import logging, prefs,event
logging.console.setLevel(logging.DEBUG)#get messages about the sound lib as it loads

prefs.general['audioLib'] = ['pyo']
#prefs.general['audioDriver'] = ['Primary Sound']
print(prefs) #tell me about all current settings
from psychopy import sound,core, visual


if prefs.general['audioLib'][0] == 'pyo':
    print 'initializing pyo'
    #if pyo is the first lib in the list of preferred libs then we could use small buffer
    #pygame sound is very bad with a small buffer though
    sound.init(48000,buffer=128)
print 'Using %s(with %s) for sounds' %(sound.audioLib, sound.audioDriver)

dogSound = sound.Sound('dog-label.wav')
highA = sound.Sound('A',octave=3, sampleRate=44100, secs=1.0, bits=24)
tick = sound.Sound('300',secs=0.01,sampleRate=44100, bits=24)
tock = sound.Sound('3500',secs=0.01, sampleRate=44100, bits=24)

win = visual.Window([200,200], pos=[0,0],color="blue", allowGUI=False, monitor='testingRoom',units='pix',winType='pyglet')
print 'd for dog, i for tick, o for tock, q for quit'
while True:
	key = event.getKeys()
	try:
		if key[0]=='d':
			dogSound.play()
		elif key[0]=='i':
			tick.play()
		elif key[0]=='o':
			tock.play()
		elif key[0]=='q':
			break
	except:
		pass
