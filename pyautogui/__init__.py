# PyAutoGUI: Cross-platform GUI automation for human beings.
# BSD license
# Al Sweigart al@inventwithpython.com (Send me feedback & suggestions!)

"""
IMPORTANT NOTE!

To use this module on Mac OS X, you need the PyObjC module installed.
For Python 3, run:
    sudo pip3 install pyobjc-core
    sudo pip3 install pyobjc
For Python 2, run:
    sudo pip install pyobjc-core
    sudo pip install pyobjc
(There's some bug with their installer, so install pyobjc-core first or else
the install takes forever.)

To use this module on Linux, you need Xlib module installed.
For Python 3, run:
    sudo pip3 install python3-Xlib
For Python 2, run:
    sudo pip install Xlib

To use this module on Windows, you do not need anything else.

You will need PIL/Pillow to use the screenshot features.
"""


__version__ = '0.9.26'

import sys
import time

# move these functions into this namespace
from pyscreeze import *
from pymsgbox import *
from pytweening import *

import pyscreeze # used so we can change the RAISE_IF_NOT_FOUND and GRAYSCALE_DEFAULT variables



KEY_NAMES = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
     'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
     'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab',
     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
     'command', 'option', 'optionleft', 'optionright']
KEYBOARD_KEYS = KEY_NAMES   # keeping old KEYBOARD_KEYS for backwards compatibility

def isShiftCharacter(character):
    """Returns True if the key character is uppercase or shifted."""
    return character.isupper() or character in '~!@#$%^&*()_+{}|:"<>?'

# The platformModule is where we reference the platform-specific functions.
if sys.platform.startswith('java'):
    #import pyautogui._pyautogui_java as platformModule
    raise NotImplementedError('Jython is not yet supported by PyAutoGUI.')
elif sys.platform == 'darwin':
    import pyautogui._pyautogui_osx as platformModule
elif sys.platform == 'win32':
    import pyautogui._pyautogui_win as platformModule
else:
    import pyautogui._pyautogui_x11 as platformModule


MINIMUM_DURATION = 0.1 # In seconds. Any duration less than this is rounded to 0.0 to instantly move the mouse.

PAUSE = 0.1 # The number of seconds to pause after EVERY public function call. Useful for debugging.
FAILSAFE = True


# General Functions
# =================

def position(x=None, y=None):
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple.

    Args:
      x (int, None, optional) - If not None, this argument overrides the x in
        the return value.
      y (int, None, optional) - If not None, this argument overrides the y in
        the return value.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    posx, posy = platformModule._position()
    posx = int(posx)
    posy = int(posy)
    if x is not None:
        posx = int(x)
    if y is not None:
        posy = int(y)
    return posx, posy


def size():
    """Returns the width and height of the screen as a two-integer tuple.

    Returns:
      (width, height) tuple of the screen size, in pixels.
    """
    return platformModule._size()


def onScreen(*args):
    """Returns whether the given xy coordinates are on the screen or not.

    Args:
      Either the arguments are two separate values, first arg for x and second
        for y, or there is a single argument of a sequence with two values, the
        first x and the second y.
        Example: onScreen(x, y) or onScreen([x, y])

    Returns:
      bool: True if the xy coordinates are on the screen at its current
        resolution, otherwise False.
    """
    if len(args) == 2:
        # args passed as onScreen(x, y)
        x = int(args[0])
        y = int(args[1])
    else:
        # args pass as onScreen([x, y])
        x = int(args[0][0])
        y = int(args[0][1])

    width, height = platformModule._size()
    return x >= 0 and y >= 0 and x < width and y < height




# Mouse Functions
# ===============

def mouseDown(x=None, y=None, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs pressing a mouse button down (but not up).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        mouse down happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        mouse down happens. None by default.
      button (str, int, optional): The mouse button pressed down. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3), not %s" % button)
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)

    _failSafeCheck()
    moveTo(x, y, _pause=False)
    x, y = platformModule._position() # TODO - this isn't right. We need to check the params.
    if button == 1 or str(button).lower() == 'left':
        platformModule._mouseDown(x, y, 'left')
    elif button == 2 or str(button).lower() == 'middle':
        platformModule._mouseDown(x, y, 'middle')
    elif button == 3 or str(button).lower() == 'right':
        platformModule._mouseDown(x, y, 'right')

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def mouseUp(x=None, y=None, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs releasing a mouse button up (but not down beforehand).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        mouse up happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        mouse up happens. None by default.
      button (str, int, optional): The mouse button released. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3), not %s" % button)
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)

    _failSafeCheck()
    moveTo(x, y, _pause=False)
    x, y = platformModule._position()
    if button == 1 or str(button).lower() == 'left':
        platformModule._mouseUp(x, y, 'left')
    elif button == 2 or str(button).lower() == 'middle':
        platformModule._mouseUp(x, y, 'middle')
    elif button == 3 or str(button).lower() == 'right':
        platformModule._mouseUp(x, y, 'right')

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs pressing a mouse button down and then immediately releasing it.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where
        the click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.
      clicks (int, optional): The number of clicks to perform. 1 by default.
        For example, passing 2 would do a doubleclick.
      interval (float, optional): The number of seconds in between each click,
        if the number of clicks is greater than 1. 0.0 by default, for no
        pause in between clicks.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3)")
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)

    _failSafeCheck()
    moveTo(x, y, duration=duration, tween=tween, _pause=False)

    for i in range(clicks):
        _failSafeCheck()
        if button == 1 or str(button).lower() == 'left':
            platformModule._click(x, y, 'left')
        elif button == 2 or str(button).lower() == 'middle':
            platformModule._click(x, y, 'middle')
        elif button == 3 or str(button).lower() == 'right':
            platformModule._click(x, y, 'right')
        else:
            # These mouse buttons for hor. and vert. scrolling only apply to x11:
            platformModule._click(x, y, button)

        time.sleep(interval)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def click_img(image, timeout=5, timeout_interval=0.1, clicks=1, interval=0.0, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Try during timeout passed performs pressing a mouse button down and then immediately releasing it on the set image.

    Args:
      image (file path):image path sought
        None by default.
      timeout (float, optional): Time in secounds that function keep trying. 
        5 by default.
      timeout_interval (float, optional): Interval time in secounds for try click again. 
        For example, passing 0.5 each 0.5 secounds it is tried click again.
      clicks (int, optional): The number of clicks to perform. 1 by default.
        For example, passing 2 would do a doubleclick.
      interval (float, optional): The number of seconds in between each click,
        if the number of clicks is greater than 1. 0.0 by default, for no
        pause in between clicks.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: Timeout. The image can not be found
    """

    k = 0
    # The sleep function is set timeout_interval secouds, so k must be compared with timeout/timeout_interval
    while k<float(timeout)/timeout_interval:
        position = locateCenterOnScreen(image)
        if position:
            click(position[0], position[1], clicks=clicks, interval=interval, button=button, duration=duration, tween=tween, pause=pause, _pause=_pause)
            break
        k += 1
        time.sleep(timeout_interval)
    else:
        raise ValueError('Timeout. The image can not be found')

def rightClick(x=None, y=None, duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs a right mouse button click.

    This is a wrapper function for click('right', x, y).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    click(x, y, 1, 0.0, 'right', _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def middleClick(x=None, y=None, duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs a middle mouse button click.

    This is a wrapper function for click('right', x, y).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    click(x, y, 1, 0.0, 'middle', _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def doubleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs a double click.

    This is a wrapper function for click('left', x, y, 2, interval).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.
      interval (float, optional): The number of seconds in between each click,
        if the number of clicks is greater than 1. 0.0 by default, for no
        pause in between clicks.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3, 4,
        5, 6, or 7
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    click(x, y, 2, interval, button, _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def tripleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=linear, pause=None, _pause=True):
    """Performs a triple click..

    This is a wrapper function for click('left', x, y, 3, interval).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.
      interval (float, optional): The number of seconds in between each click,
        if the number of clicks is greater than 1. 0.0 by default, for no
        pause in between clicks.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3, 4,
        5, 6, or 7
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    click(x, y, 3, interval, button, _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def scroll(clicks, x=None, y=None, pause=None, _pause=True):
    """Performs a scroll of the mouse scroll wheel.

    Whether this is a vertical or horizontal scroll depends on the underlying
    operating system.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)

    platformModule._scroll(clicks, x, y)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def hscroll(clicks, x=None, y=None, pause=None, _pause=True):
    """Performs an explicitly horizontal scroll of the mouse scroll wheel,
    if this is supported by the operating system. (Currently just Linux.)

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)

    platformModule._hscroll(clicks, x, y)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def vscroll(clicks, x=None, y=None, pause=None, _pause=True):
    """Performs an explicitly vertical scroll of the mouse scroll wheel,
    if this is supported by the operating system. (Currently just Linux.)

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)
    platformModule._vscroll(clicks, x, y)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)



def moveTo(x=None, y=None, duration=0.0, tween=linear, pause=None, _pause=True):
    """Moves the mouse cursor to a point on the screen.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): The x position on the screen where the
        click happens. None by default. If tuple, this is used for x and y.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.
      duration (float, optional): The amount of time it takes to move the mouse
        cursor to the xy coordinates. If 0, then the mouse cursor is moved
        instantaneously. 0.0 by default.
      tween (func, optional): The tweening function used if the duration is not
        0. A linear tween is used by default. See the tweens.py file for
        details.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    _mouseMoveDragTo('move', x, y, duration, tween)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)



def moveRel(xOffset=0, yOffset=0, duration=0.0, tween=linear, pause=None, _pause=True):
    """Moves the mouse cursor to a point on the screen, relative to its current
    position.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): How far left (for negative values) or
        right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
      y (int, float, None, optional): How far up (for negative values) or
        down (for positive values) to move the cursor. 0 by default.
      duration (float, optional): The amount of time it takes to move the mouse
        cursor to the new xy coordinates. If 0, then the mouse cursor is moved
        instantaneously. 0.0 by default.
      tween (func, optional): The tweening function used if the duration is not
        0. A linear tween is used by default. See the tweens.py file for
        details.

    Returns:
      None
    """

    # This may seem silly, but I wanted the user to be able to pass None for
    # an argument just so that it is consistent with moveTo().
    if xOffset is None:
        xOffset = 0
    if yOffset is None:
        yOffset = 0

    if type(xOffset) in (tuple, list):
        xOffset, yOffset = xOffset[0], xOffset[1]

    if xOffset == 0 and yOffset == 0:
        return # no-op case

    _failSafeCheck()

    mousex, mousey = platformModule._position()
    moveTo(mousex + xOffset, mousey + yOffset, duration, tween, _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def dragTo(x=None, y=None, duration=0.0, tween=linear, button='left', pause=None, _pause=True):
    """Performs a mouse drag (mouse movement while a button is held down) to a
    point on the screen.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): How far left (for negative values) or
        right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
      y (int, float, None, optional): How far up (for negative values) or
        down (for positive values) to move the cursor. 0 by default.
      duration (float, optional): The amount of time it takes to move the mouse
        cursor to the new xy coordinates. If 0, then the mouse cursor is moved
        instantaneously. 0.0 by default.
      tween (func, optional): The tweening function used if the duration is not
        0. A linear tween is used by default. See the tweens.py file for
        details.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None
    """
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    mouseDown(button=button, _pause=False)
    _mouseMoveDragTo('drag', x, y, duration, tween, button)
    mouseUp(button=button, _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def dragRel(xOffset=0, yOffset=0, duration=0.0, tween=linear, button='left', pause=None, _pause=True):
    """Performs a mouse drag (mouse movement while a button is held down) to a
    point on the screen, relative to its current position.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, tuple, optional): How far left (for negative values) or
        right (for positive values) to move the cursor. 0 by default. If tuple, this is used for xOffset and yOffset.
      y (int, float, None, optional): How far up (for negative values) or
        down (for positive values) to move the cursor. 0 by default.
      duration (float, optional): The amount of time it takes to move the mouse
        cursor to the new xy coordinates. If 0, then the mouse cursor is moved
        instantaneously. 0.0 by default.
      tween (func, optional): The tweening function used if the duration is not
        0. A linear tween is used by default. See the tweens.py file for
        details.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None
    """
    if xOffset is None:
        xOffset = 0
    if yOffset is None:
        yOffset = 0

    if type(xOffset) in (tuple, list):
        xOffset, yOffset = xOffset[0], xOffset[1]

    if xOffset == 0 and yOffset == 0:
        return # no-op case

    _failSafeCheck()

    mousex, mousey = platformModule._position()
    mouseDown(button=button, _pause=False)
    _mouseMoveDragTo('drag', mousex + xOffset, mousey + yOffset, duration, tween, button)
    mouseUp(button=button, _pause=False)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def _mouseMoveDragTo(moveOrDrag, x, y, duration, tween, button=None):
    """Handles the actual move or drag event, since different platforms
    implement them differently.

    On Windows & Linux, a drag is a normal mouse move while a mouse button is
    held down. On OS X, a distinct "drag" event must be used instead.

    The code for moving and dragging the mouse is similar, so this function
    handles both. Users should call the moveTo() or dragTo() functions instead
    of calling _mouseMoveDragTo().

    Args:
      moveOrDrag (str): Either 'move' or 'drag', for the type of action this is.
      x (int, float, None, optional): How far left (for negative values) or
        right (for positive values) to move the cursor. 0 by default.
      y (int, float, None, optional): How far up (for negative values) or
        down (for positive values) to move the cursor. 0 by default.
      duration (float, optional): The amount of time it takes to move the mouse
        cursor to the new xy coordinates. If 0, then the mouse cursor is moved
        instantaneously. 0.0 by default.
      tween (func, optional): The tweening function used if the duration is not
        0. A linear tween is used by default. See the tweens.py file for
        details.
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.

    Returns:
      None
    """

    # The move and drag code is similar, but OS X requires a special drag event instead of just a move event when dragging.
    # See https://stackoverflow.com/a/2696107/1893164

    assert moveOrDrag in ('move', 'drag'), "moveOrDrag must be in ('move', 'drag'), not %s" % (moveOrDrag)

    if sys.platform != 'darwin':
        moveOrDrag = 'move' # only OS X needs to use the drag

    if x is None and y is None:
        return # special case for no mouse movement at all

    x, y = position(x, y)

    width, height = platformModule._size()
    startx, starty = platformModule._position()

    # None values means "use current position". Convert x and y to ints.
    x = startx if x is None else int(x)
    y = starty if y is None else int(y)

    # Make sure x and y are within the screen bounds.
    if x < 0:
        x = 0
    elif x >= width:
        x = width - 1
    if y < 0:
        y = 0
    elif y >= height:
        y = height - 1

    _failSafeCheck()

    # If the duration is small enough, just move the cursor there instantly.
    if duration <= MINIMUM_DURATION:
        if moveOrDrag == 'move':
            platformModule._moveTo(x, y)
        else:
            platformModule._dragTo(x, y, button)
        return

    # Non-instant moving/dragging involves tweening:
    segments = max(width, height)
    timeSegment = float(duration) / segments
    while timeSegment < 0.05: # if timeSegment is too short, let's decrease the amount we divide it by. Otherwise the time.sleep() will be a no-op and the mouse cursor moves there instantly.
        segments = int(segments * 0.9) # decrease segments by 90%.
        timeSegment = float(duration) / segments

    for n in range(segments):
        time.sleep(timeSegment)
        _failSafeCheck()
        pointOnLine = tween(float(n) / segments)
        tweenX, tweenY = getPointOnLine(startx, starty, x, y, pointOnLine)
        tweenX, tweenY = int(tweenX), int(tweenY)
        if moveOrDrag == 'move':
            platformModule._moveTo(tweenX, tweenY)
        else:
            # only OS X needs the drag event specifically
            platformModule._dragTo(tweenX, tweenY, button)

    # Ensure that no matter what the tween function returns, the mouse ends up
    # at the final destination.
    if moveOrDrag == 'move':
        platformModule._moveTo(x, y)
    else:
        platformModule._dragTo(x, y, button)

    _failSafeCheck()

# Keyboard Functions
# ==================


def isValidKey(key):
    """Returns a Boolean value if the given key is a valid value to pass to
    PyAutoGUI's keyboard-related functions for the current platform.

    This function is here because passing an invalid value to the PyAutoGUI
    keyboard functions currently is a no-op that does not raise an exception.

    Some keys are only valid on some platforms. For example, while 'esc' is
    valid for the Escape key on all platforms, 'browserback' is only used on
    Windows operating systems.

    Args:
      key (str): The key value.

    Returns:
      bool: True if key is a valid value, False if not.
    """
    return platformModule.keyboardMapping.get(key, None) != None


def keyDown(key, pause=None, _pause=True):
    """Performs a keyboard key press without the release. This will put that
    key in a held down state.

    NOTE: For some reason, this does not seem to cause key repeats like would
    happen if a keyboard key was held down on a text field.

    Args:
      key (str): The key to be pressed down. The valid names are listed in
      KEYBOARD_KEYS.

    Returns:
      None
    """
    if len(key) > 1:
        key = key.lower()

    _failSafeCheck()
    platformModule._keyDown(key)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def keyUp(key, pause=None, _pause=True):
    """Performs a keyboard key release (without the press down beforehand).

    Args:
      key (str): The key to be released up. The valid names are listed in
      KEYBOARD_KEYS.

    Returns:
      None
    """
    if len(key) > 1:
        key = key.lower()

    _failSafeCheck()
    platformModule._keyUp(key)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def press(keys, presses=1, interval=0.0, pause=None, _pause=True):
    """Performs a keyboard key press down, followed by a release.

    Args:
      key (str, list): The key to be pressed. The valid names are listed in
      KEYBOARD_KEYS. Can also be a list of such strings.
      presses (integer, optiional): the number of press repetition
      1 by default, for just one press
      interval (float, optional): How many seconds between each press.
      0.0 by default, for no pause between presses.
      pause (float, optional): How many seconds in the end of function process.
      None by default, for no pause in the end of function process.
    Returns:
      None
    """
    if type(keys) == str:
        keys = [keys] # put string in a list
    else:
        lowerKeys = []
        for s in keys:
            if len(s) > 1:
                lowerKeys.append(s.lower())
            else:
                lowerKeys.append(s)
    interval = float(interval)
    for i in range(presses):
        for k in keys:
            _failSafeCheck()
            platformModule._keyDown(k)
            platformModule._keyUp(k)
        time.sleep(interval)
        
    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def typewrite(message, interval=0.0, pause=None, _pause=True):
    """Performs a keyboard key press down, followed by a release, for each of
    the characters in message.

    The message argument can also be list of strings, in which case any valid
    keyboard name can be used.

    Since this performs a sequence of keyboard presses and does not hold down
    keys, it cannot be used to perform keyboard shortcuts. Use the hotkey()
    function for that.

    Args:
      message (str, list): If a string, then the characters to be pressed. If a
        list, then the key names of the keys to press in order. The valid names
        are listed in KEYBOARD_KEYS.
      interval (float, optional): The number of seconds in between each press.
        0.0 by default, for no pause in between presses.

    Returns:
      None
    """
    interval = float(interval)

    _failSafeCheck()

    for c in message:
        if len(c) > 1:
            c = c.lower()
        press(c, _pause=False)
        time.sleep(interval)
        _failSafeCheck()

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)


def hotkey(*args, **kwargs):
    """Performs key down presses on the arguments passed in order, then performs
    key releases in reverse order.

    The effect is that calling hotkey('ctrl', 'shift', 'c') would perform a
    "Ctrl-Shift-C" hotkey/keyboard shortcut press.

    Args:
      key(s) (str): The series of keys to press, in order. This can also be a
        list of key strings to press.
      interval (float, optional): The number of seconds in between each press.
        0.0 by default, for no pause in between presses.

    Returns:
      None
    """
    interval = float(kwargs.get('interval', 0.0))

    _failSafeCheck()

    for c in args:
        if len(c) > 1:
            c = c.lower()
        platformModule._keyDown(c)
        time.sleep(interval)
    for c in reversed(args):
        if len(c) > 1:
            c = c.lower()
        platformModule._keyUp(c)
        time.sleep(interval)

    if kwargs.get('pause', None) is not None and _pause:
        time.sleep(pause)
    elif kwargs.get('_pause', True) and PAUSE != 0:
        time.sleep(PAUSE)


class FailSafeException(Exception):
    pass

def _failSafeCheck():
    if FAILSAFE and position() == (0, 0):
        raise FailSafeException('PyAutoGUI fail-safe triggered from mouse moving to upper-left corner. To disable this fail-safe, set pyautogui.FAILSAFE to False.')


def displayMousePosition(xOffset=0, yOffset=0):
    """This function is meant to be run from the command line. It will
    automatically display the location and RGB of the mouse cursor."""
    print('Press Ctrl-C to quit.')
    if xOffset != 0 or yOffset != 0:
        print('xOffset: %s yOffset: %s' % (xOffset, yOffset))
    resolution = size()
    try:
        while True:
            # Get and print the mouse coordinates.
            x, y = position()
            positionStr = 'X: ' + str(x - xOffset).rjust(4) + ' Y: ' + str(y - yOffset).rjust(4)
            if (x - xOffset) < 0 or (y - yOffset) < 0 or (x - xOffset) >= resolution[0] or (y - yOffset) >= resolution[1]:
                pixelColor = ('NaN', 'NaN', 'NaN')
            else:
                pixelColor = screenshot().getpixel((x, y))
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
            sys.stdout.write(positionStr)
            sys.stdout.write('\b' * len(positionStr))
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
