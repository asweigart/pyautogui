# NOTE - It is a known issue that the keyboard-related functions don't work on Ubuntu VMs in Virtualbox.

import pyautogui
import sys
import os
from pyautogui import LEFT, MIDDLE, RIGHT

from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
import Xlib.XK

BUTTON_NAME_MAPPING = {LEFT: 1, MIDDLE: 2, RIGHT: 3, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}


if sys.platform in ('java', 'darwin', 'win32'):
    raise Exception('The pyautogui_x11 module should only be loaded on a Unix system that supports X11.')

#from pyautogui import *

"""
Much of this code is based on information gleaned from Paul Barton's PyKeyboard in PyUserInput from 2013, itself derived from Akkana Peck's pykey in 2008 ( http://www.shallowsky.com/software/crikey/pykey-0.1 ), itself derived from her "Crikey" lib.
"""

def _position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    coord = _display.screen().root.query_pointer()._data
    return coord["root_x"], coord["root_y"]


def _size():
    return _display.screen().width_in_pixels, _display.screen().height_in_pixels



def _vscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return
    elif clicks > 0:
        button = 4 # scroll up
    else:
        button = 5 # scroll down

    for i in range(abs(clicks)):
        _click(x, y, button=button)


def _hscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return
    elif clicks > 0:
        button = 7 # scroll right
    else:
        button = 6 # scroll left

    for i in range(abs(clicks)):
        _click(x, y, button=button)


def _scroll(clicks, x=None, y=None):
    return _vscroll(clicks, x, y)


def _click(x, y, button):
    assert button in BUTTON_NAME_MAPPING.keys(), "button argument not in ('left', 'middle', 'right', 4, 5, 6, 7)"
    button = BUTTON_NAME_MAPPING[button]

    _mouseDown(x, y, button)
    _mouseUp(x, y, button)


def _moveTo(x, y):
    fake_input(_display, X.MotionNotify, x=x, y=y)
    _display.sync()


def _mouseDown(x, y, button):
    _moveTo(x, y)
    assert button in BUTTON_NAME_MAPPING.keys(), "button argument not in ('left', 'middle', 'right', 4, 5, 6, 7)"
    button = BUTTON_NAME_MAPPING[button]
    fake_input(_display, X.ButtonPress, button)
    _display.sync()


def _mouseUp(x, y, button):
    _moveTo(x, y)
    assert button in BUTTON_NAME_MAPPING.keys(), "button argument not in ('left', 'middle', 'right', 4, 5, 6, 7)"
    button = BUTTON_NAME_MAPPING[button]
    fake_input(_display, X.ButtonRelease, button)
    _display.sync()


def _keyDown(key):
    """Performs a keyboard key press without the release. This will put that
    key in a held down state.

    NOTE: For some reason, this does not seem to cause key repeats like would
    happen if a keyboard key was held down on a text field.

    Args:
      key (str): The key to be pressed down. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if type(key) == int:
        fake_input(_display, X.KeyPress, key)
        _display.sync()
        return

    if type(keyboardMapping[key]) == int:
        keycode = keyboardMapping[key]
        needsShift = False
    else:
        keycode, needsShift = keyboardMapping[key]
    if needsShift:
        fake_input(_display, X.KeyPress, keyboardMapping['shift'][0])

    fake_input(_display, X.KeyPress, keycode)

    if needsShift:
        fake_input(_display, X.KeyRelease, keyboardMapping['shift'][0])
    _display.sync()


def _keyUp(key):
    """Performs a keyboard key release (without the press down beforehand).

    Args:
      key (str): The key to be released up. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """

    """
    Release a given character key. Also works with character keycodes as
    integers, but not keysyms.
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if type(key) == int:
        keycode = key
    else:
        if type(keyboardMapping[key]) == int:
            keycode = keyboardMapping[key]
            needsShift = False
        else:
            keycode, needsShift = keyboardMapping[key]

    fake_input(_display, X.KeyRelease, keycode)
    _display.sync()


# Taken from PyKeyboard's ctor function.
_display = Display(os.environ['DISPLAY'])


""" Information for keyboardMapping derived from PyKeyboard's special_key_assignment() function.

The *KB dictionaries in pyautogui map a string that can be passed to keyDown(),
keyUp(), or press() into the code used for the OS-specific keyboard function.

They should always be lowercase, and the same keys should be used across all OSes."""
keyboardMapping = dict([(key, None) for key in pyautogui.KEY_NAMES])
keyboardMapping.update({
    'backspace':         _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('BackSpace'))[0],
    '\b':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('BackSpace'))[0],
    'tab':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Tab'))[0],
    'enter':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Return'))[0],
    'return':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Return'))[0],
    'shift':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Shift_L'))[0],
    'ctrl':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Control_L'))[0],
    'alt':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Alt_L'))[0],
    'pause':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Pause'))[0],
    'capslock':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Caps_Lock'))[0],
    'esc':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Escape'))[0],
    'escape':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Escape'))[0],
    'pgup':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Page_Up'))[0],
    'pgdn':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Page_Down'))[0],
    'pageup':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Page_Up'))[0],
    'pagedown':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Page_Down'))[0],
    'end':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('End'))[0],
    'home':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Home'))[0],
    'left':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Left'))[0],
    'up':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Up'))[0],
    'right':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Right'))[0],
    'down':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Down'))[0],
    'select':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Select')),
    'print':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Print'))[0],
    'execute':           _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Execute')),
    'prtsc':             _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Print'))[0],
    'prtscr':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Print'))[0],
    'prntscrn':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Print'))[0],
    'printscreen':       _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Print'))[0],
    'insert':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Insert'))[0],
    'del':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Delete'))[0],
    'delete':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Delete'))[0],
    'help':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Help'))[0],
    'winleft':           _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Super_L'))[0],
    'winright':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Super_R'))[0],
    'apps':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Menu'))[0],
    'num0':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_0'))[0],
    'num1':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_1'))[0],
    'num2':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_2'))[0],
    'num3':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_3'))[0],
    'num4':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_4'))[0],
    'num5':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_5'))[0],
    'num6':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_6'))[0],
    'num7':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_7'))[0],
    'num8':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_8'))[0],
    'num9':              _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_9'))[0],
    'multiply':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Multiply'))[0],
    'add':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Add'))[0],
    'separator':         _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Separator'))[0],
    'subtract':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Subtract'))[0],
    'decimal':           _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Decimal'))[0],
    'divide':            _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('KP_Divide'))[0],
    'f1':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F1'))[0],
    'f2':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F2'))[0],
    'f3':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F3'))[0],
    'f4':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F4'))[0],
    'f5':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F5'))[0],
    'f6':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F6'))[0],
    'f7':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F7'))[0],
    'f8':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F8'))[0],
    'f9':                _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F9'))[0],
    'f10':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F10'))[0],
    'f11':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F11'))[0],
    'f12':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F12'))[0],
    'f13':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F13')),
    'f14':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F14')),
    'f15':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F15')),
    'f16':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F16')),
    'f17':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F17')),
    'f18':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F18')),
    'f19':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F19')),
    'f20':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F20')),
    'f21':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F21')),
    'f22':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F22')),
    'f23':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F23')),
    'f24':               _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('F24')),
    'numlock':           _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Num_Lock'))[0],
    'scrolllock':        _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Scroll_Lock'))[0],
    'shiftleft':         _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Shift_L'))[0],
    'shiftright':        _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Shift_R'))[0],
    'ctrlleft':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Control_L'))[0],
    'ctrlright':         _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Control_R'))[0],
    'altleft':           _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Alt_L'))[0],
    'altright':          _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Alt_R')),
    # These are added because unlike a-zA-Z0-9, the single characters do not have a
    ' ': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('space'))[0],
    'space': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('space'))[0],
    '\t': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Tab'))[0],
    '\n': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Return'))[0],  # for some reason this needs to be cr, not lf
    '\r': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Return'))[0],
    '\e': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('Escape'))[0],
    '!': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('exclam'))[0],
    '#': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('numbersign'))[0],
    '%': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('percent'))[0],
    '$': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('dollar'))[0],
    '&': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('ampersand'))[0],
    '"': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('quotedbl'))[0],
    "'": _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('apostrophe'))[0],
    '(': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('parenleft'))[0],
    ')': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('parenright'))[0],
    '*': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('asterisk'))[0],
    '=': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('equal'))[0],
    '+': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('plus'))[0],
    ',': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('comma'))[0],
    '-': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('minus'))[0],
    '.': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('period'))[0],
    '/': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('slash'))[0],
    ':': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('colon'))[0],
    ';': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('semicolon'))[0],
    '<': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('less'))[0],
    '>': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('greater'))[0],
    '?': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('question'))[0],
    '@': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('at'))[0],
    '[': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('bracketleft'))[0],
    ']': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('bracketright'))[0],
    '\\': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('backslash'))[0],
    '^': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('asciicircum'))[0],
    '_': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('underscore'))[0],
    '`': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('grave'))[0],
    '{': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('braceleft'))[0],
    '|': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('bar'))[0],
    '}': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('braceright'))[0],
    '~': _display.keysym_to_keycodes(Xlib.XK.string_to_keysym('asciitilde'))[0],
})

# Trading memory for time" populate winKB so we don't have to call VkKeyScanA each time.
for c in """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890""":
    keyboardMapping[c] = _display.keysym_to_keycodes(Xlib.XK.string_to_keysym(c))[0]
