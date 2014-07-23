# PyAutoGUI: Cross-platform GUI automation for human beings.
# BSD license
# Al Sweigart al@inventwithpython.com

import sys
import time
import pyautogui.tweens
import pyautogui.util

# The platformModule is where we reference the platform-specific functions.
if sys.platform.startswith('java'):
    import pyautogui.pyautogui_java as platformModule
elif sys.platform == 'darwin':
    import pyautogui.pyautogui_osx as platformModule
elif sys.platform == 'win32':
    import pyautogui.pyautogui_win as platformModule
else:
    import pyautogui.pyautogui_x11 as platformModule


MINIMUM_DURATION = 0.1 # In seconds. Any duration less than this is rounded to 0.0 to instantly move the mouse.

# General Functions
# =================

def position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    return platformModule._position()


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

    width, height = platformModule.size()
    return x >= 0 and y >= 0 and x < width and y < height




# Mouse Functions
# ===============

def mouseDown(button='left', x=None, y=None):
    """Performs pressing a mouse button down (but not up).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      button (str, int, optional): The mouse button pressed down. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.
      x (int, float, None, optional): The x position on the screen where the
        mouse down happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        mouse down happens. None by default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3), not %s" % button)

    moveTo(x, y)
    x, y = platformModule.position() # TODO - this isn't right. We need to check the params.
    if button == 1 or str(button).lower() == 'left':
        platformModule._mouseDown('left', x, y)
    elif button == 2 or str(button).lower() == 'middle':
        platformModule._mouseDown('middle', x, y)
    elif button == 3 or str(button).lower() == 'right':
        platformModule._mouseDown('right', x, y)


def mouseUp(button='left', x=None, y=None):
    """Performs releasing a mouse button up (but not down beforehand).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      button (str, int, optional): The mouse button released. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.
      x (int, float, None, optional): The x position on the screen where the
        mouse up happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        mouse up happens. None by default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3), not %s" % button)

    moveTo(x, y)
    x, y = platformModule.position()
    if button == 1 or str(button).lower() == 'left':
        platformModule._mouseUp('left', x, y)
    elif button == 2 or str(button).lower() == 'middle':
        platformModule._mouseUp('middle', x, y)
    elif button == 3 or str(button).lower() == 'right':
        platformModule._mouseUp('right', x, y)

def click(button='left', x=None, y=None, clicks=1, interval=0.0):
    """Performs pressing a mouse button down and then immediately releasing it.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      button (str, int, optional): The mouse button clicked. Must be one of
        'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
        default.
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.
      clicks (int, optional): The number of clicks to perform. 1 by default.
        For example, passing 2 would do a doubleclick.
      interval (float, optional): The number of seconds in between each click,
        if the number of clicks is greater than 1. 0.0 by default, for no
        pause in between clicks.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3, 4,
        5, 6, or 7
    """
    if button not in ('left', 'middle', 'right', 1, 2, 3, 4, 5, 6, 7):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3)")

    moveTo(x, y)
    x, y = platformModule.position()
    for i in range(clicks):
        if button == 1 or str(button).lower() == 'left':
            platformModule._click('left', x, y)
        elif button == 2 or str(button).lower() == 'middle':
            platformModule._click('middle', x, y)
        elif button == 3 or str(button).lower() == 'right':
            platformModule._click('right', x, y)
        else:
            # These mouse buttons for hor. and vert. scrolling only apply to x11:
            platformModule._click(button, x, y)

        time.sleep(interval)

def rightClick(x=None, y=None):
    """Performs a right mouse button click.

    This is a wrapper function for click('right', x, y).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None

    Raises:
      ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3, 4,
        5, 6, or 7
    """
    click('right', x, y, 1, interval)

def doubleClick(x=None, y=None, interval=0.0, button='left'):
    """Performs a double click.

    This is a wrapper function for click('left', x, y, 2, interval).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
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

    click(button, x, y, 2, interval)


def tripleClick(x=None, y=None, interval=0.0, button='left'):
    """Performs a triple click..

    This is a wrapper function for click('left', x, y, 3, interval).

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
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
    click(button, x, y, 3, interval)


def scroll(clicks, x=None, y=None):
    """Performs a scroll of the mouse scroll wheel.

    Whether this is a vertical or horizontal scroll depends on the underlying
    operating system.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    return platformModule.scroll(clicks, x, y)

def hscroll(clicks, x=None, y=None):
    """Performs an explicitly horizontal scroll of the mouse scroll wheel,
    if this is supported by the operating system. (Currently just Linux.)

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    return platformModule.hscroll(clicks, x, y)

def vscroll(clicks, x=None, y=None):
    """Performs an explicitly vertical scroll of the mouse scroll wheel,
    if this is supported by the operating system. (Currently just Linux.)

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      clicks (int, float): The amount of scrolling to perform.
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
      y (int, float, None, optional): The y position on the screen where the
        click happens. None by default.

    Returns:
      None
    """
    return platformModule.vscroll(clicks, x, y)



def moveTo(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween):
    """Moves the mouse cursor to a point on the screen.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
      x (int, float, None, optional): The x position on the screen where the
        click happens. None by default.
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
    _mouseMoveDragTo('move', x, y, duration, tween)



def moveRel(x=0, y=0, duration=0.0, tween=pyautogui.tweens.linearTween):
    """Moves the mouse cursor to a point on the screen, relative to its current
    position.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
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

    Returns:
      None
    """

    # This may seem silly, but I wanted the user to be able to pass None for
    # an argument just so that it is consistent with moveTo().
    if x is None:
        x = 0
    if y is None:
        y = 0

    if x == 0 and y == 0:
        return # no-op case

    mousex, mousey = platformModule.position()
    moveTo(mousex + x, mousey + y, duration, tween)




def dragTo(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween, button='left'):
    """Performs a mouse drag (mouse movement while a button is held down) to a
    point on the screen.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
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
    mouseDown(button)
    _mouseMoveDragTo('drag', x, y, duration, tween)
    mouseUp(button)


def dragRel(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween, button='left'):
    """Performs a mouse drag (mouse movement while a button is held down) to a
    point on the screen, relative to its current position.

    The x and y parameters detail where the mouse event happens. If None, the
    current mouse position is used. If a float value, it is rounded down. If
    outside the boundaries of the screen, the event happens at edge of the
    screen.

    Args:
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
    mouseDown(button)
    _mouseMoveDragTo('drag', x, y, duration, tween, button)
    mouseUp(button)


def _mouseMoveDragTo(moveOrDrag, x, y, duration, tween, button=None):
    # The move and drag code is similar, but OS X requires a special drag event instead of just a move event when dragging.
    # See https://stackoverflow.com/a/2696107/1893164

    assert moveOrDrag in ('move', 'drag'), "moveOrDrag must be in ('move', 'drag'), not %s" % (moveOrDrag)

    if x is None and y is None:
        return # special case for no mouse movement at all

    width, height = platformModule.size()
    startx, starty = platformModule.position()

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

    # If the duration is small enough, just move the cursor there instantly.
    if duration <= MINIMUM_DURATION:
        if moveOrDrag == 'move':
            platformModule._moveTo(x, y)
        else:
            platformModule._dragTo(x, y, button)
        return

    # Non-instant moving/dragging involves tweening:
    linePoints = pyautogui.tweens.getLine(startx, starty, x, y)
    timeSegment = duration / len(linePoints)
    for n in range(len(linePoints)):
        time.sleep(timeSegment)
        tweenedN = int(tween(n / len(linePoints)) * len(linePoints))
        if moveOrDrag == 'move':
            platformModule._moveTo(linePoints[tweenedN][0], linePoints[tweenedN][1])
        else:
            platformModule._dragTo(linePoints[tweenedN][0], linePoints[tweenedN][1], button)


# Keyboard Functions
# ==================

KEYBOARD_KEYS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'winleft', 'winright']

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


def keyDown(key):
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
    platformModule._keyDown(key)

def keyUp(key):
    """Performs a keyboard key release (without the press down beforehand).

    Args:
      key (str): The key to be released up. The valid names are listed in
      KEYBOARD_KEYS.

    Returns:
      None
    """
    if len(key) > 1:
        key = key.lower()
    platformModule._keyUp(key)

def press(key):
    """Performs a keyboard key press down, followed by a release.

    NOTE: For some reason, this does not seem to cause key repeats like would
    happen if a keyboard key was held down on a text field.

    Args:
      key (str): The key to be pressed.

    Returns:
      None
    """
    if len(key) > 1:
        key = key.lower()
    platformModule._keyDown(key)
    platformModule._keyUp(key)

def typewrite(message, interval=0.0):
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
    message = str(message)
    interval = float(interval)


    for c in message:
        if len(c) > 1:
            c = c.lower()
        press(c)
        time.sleep(interval)


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

    for c in args:
        if len(c) > 1:
            c = c.lower()
        keyDown(c)
        time.sleep(interval)
    for c in reversed(args):
        if len(c) > 1:
            c = c.lower()
        keyUp(c)
        time.sleep(interval)




