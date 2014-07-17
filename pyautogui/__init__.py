
import sys
import time

from pyautogui.tweens import *
from pyautogui.util import *

if sys.platform.startswith('java'):
    from pyautogui.pyautogui_java import *
elif sys.platform == 'darwin':
    from pyautogui.pyautogui_osx import *
elif sys.platform == 'win32':
    from pyautogui.pyautogui_win import *
else:
    from pyautogui.pyautogui_x11 import *



def moveRel(x=0, y=0, speed=0, tween=linearTween):
    if x == 0 and y == 0:
        return
    mousex, mousey = position()
    moveTo(mousex + x, mousey + y, speed, tween)


def dragTo(button='left', x=None, y=None, speed=0, tween=linearTween):
    mouseDown(button)
    moveTo(x, y, speed, tween)
    mouseUp(button)

def typewrite(*args):
    for c in args:
        if len(c) > 1:
            c = c.lower()
        press(c)


def hotkey(*args):
    for c in args:
        if len(c) > 1:
            c = c.lower()
        keyDown(c)
    for c in reversed(args):
        if len(c) > 1:
            c = c.lower()
        keyUp(c)


def dragRel(x=None, y=None, speed=0, tween=linearTween):
    mouseDown(button)
    moveRel(x, y, speed, tween)
    mouseUp(button)


def keyDown(character):
    if len(character) > 1:
        character = character.lower()
    _keyDown(character)

def keyUp(character):
    if len(character) > 1:
        character = character.lower()
    _keyUp(character)

def press(character):
    if len(character) > 1:
        character = character.lower()
    _keyDown(character)
    _keyUp(character)

def click(button='left', x=None, y=None, clicks=1, interval=0):
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3)")

    moveTo(x, y)
    x, y = position()
    for i in range(clicks):
        if button == 1 or str(button).lower() == 'left':
            _click('left', x, y)
        elif button == 2 or str(button).lower() == 'middle':
            _click('middle', x, y)
        elif button == 3 or str(button).lower() == 'right':
            _click('right', x, y)

        time.sleep(interval)


def doubleclick(button='left', x=None, y=None, interval=0):
    click(button, x, y, 2, interval)


def tripleclick(button='left', x=None, y=None, interval=0):
    click(button, x, y, 3, interval)


def mouseDown(button='left', x=None, y=None):
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3)")

    moveTo(x, y)
    x, y = position()
    if button == 1 or str(button).lower() == 'left':
        _mouseDown('left', x, y)
    elif button == 2 or str(button).lower() == 'middle':
        _mouseDown('middle', x, y)
    elif button == 3 or str(button).lower() == 'right':
        _mouseDown('right', x, y)


def mouseUp(button='left', x=None, y=None):
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3)")

    moveTo(x, y)
    x, y = position()
    if button == 1 or str(button).lower() == 'left':
        _mouseUp('left', x, y)
    elif button == 2 or str(button).lower() == 'middle':
        _mouseUp('middle', x, y)
    elif button == 3 or str(button).lower() == 'right':
        _mouseUp('right', x, y)


def press(character):
    _keyDown(character)
    _keyUp(character)