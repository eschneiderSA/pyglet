#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: window_test.py 26 2006-09-17 04:06:25Z Alex.Holkner $'

import pyglet.window
from pyglet.window.event import *
import time

from pyglet.GL.VERSION_1_1 import *

factory = pyglet.window.WindowFactory()
factory.config._attributes['doublebuffer'] = 1
w1 = factory.create(width=120, height=120)
glClearColor(1, 0, 1, 1)
glClear(GL_COLOR_BUFFER_BIT)
w1.flip()

w1.push_handlers(DebugEventHandler())

while True:
    w1.dispatch_events()
