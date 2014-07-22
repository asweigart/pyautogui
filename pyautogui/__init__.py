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

position = platformModule.position
size     = platformModule.size


# Mouse Functions
# ===============

def mouseDown(button='left', x=None, y=None):
    """Simulates pressing a mouse button down (but not up).

    The button parameter should be one of 'left', 'middle', 'right' (or 1, 2, or 3) respectively.
    The x and y parameters specify where the mouse down should take place. A None values
    means the current mouse x/y position will be used."""
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
    """Simulates pressing a mouse button up (but not down before it).

    The button parameter should be one of 'left', 'middle', 'right' (or 1, 2, or 3) respectively.
    The x and y parameters specify where the mouse down should take place. A None values
    means the current mouse x/y position will be used."""
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
    """Simulates pressing a mouse button down and then up at the same location.

    The button parameter should be one of 'left', 'middle', 'right' (or 1, 2, or 3) respectively.
    The x and y parameters specify where the mouse down should take place. A None values
    means the current mouse x/y position will be used.
    The clicks parameter specifies how many clicks should be done.
    The interval parameter specifies the pause (in seconds) in between clicks."""
    if button not in ('left', 'middle', 'right', 1, 2, 3, 4, 5, 6, 7):
        raise ValueError("button argument must be one of ('left', 'middle', 'right', 1, 2, 3, 4, 5, 6, 7)")

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
            # These mouse buttons only apply to x11:
            platformModule._click(button, x, y)

        time.sleep(interval)

def rightClick(x=None, y=None):
    """Simulates pressing the right mouse button down and then up at the same location.

    This is a wrapper function for click('right', x, y)."""
    click('right', x, y, 1, interval)

def doubleClick(button='left', x=None, y=None, interval=0):
    """Simulates a double click of the left mouse button.

    This is a wrapper function for click('left', x, y, 2, interval).

    The x and y parameters specify where the mouse down should take place. A
    None values means the current mouse x/y position will be used.
    The interval parameter specifies the pause (in seconds) in between clicks."""

    click(button, x, y, 2, interval)


def tripleClick(button='left', x=None, y=None, interval=0):
    """Simulates pressing the right mouse button down and then up at the same location.

    This is a wrapper function for click('left', x, y, 1, interval).

    The x and y parameters specify where the mouse down should take place. A
    None values means the current mouse x/y position will be used."""
    click(button, x, y, 3, interval)

# platform-specific imports:
scroll = platformModule.scroll
hscroll = platformModule.hscroll
vscroll = platformModule.vscroll



def moveTo(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween):
    """Moves the mouse cursor to a point on the screen.

    The x and y parameters specify where the cursor should move to. A
    None values means the current mouse x/y position will be used.
    The duration parameter specifies how long (in seconds) it should take the
    mouse cursor to move to this position. A duration of 0.0 means that the
    mouse cursor will move to the new position instantaneously.
    The tween parameter specifies the tweening function to use for the
    movement. See the tweens.py file for more details."""
    _mouseMoveDragTo('move', x, y, duration, tween)



def moveRel(x=0, y=0, duration=0.0, tween=pyautogui.tweens.linearTween):
    """Moves the mouse cursor to a point on the screen, relative to its current
    position.

    The x and y parameters specify how far from the current position the mouse
    cursor should move.
    The duration parameter specifies how long (in seconds) it should take the
    mouse cursor to move to this position. A duration of 0.0 means that the
    mouse cursor will move to the new position instantaneously.
    The tween parameter specifies the tweening function to use for the
    movement. See the tweens.py file for more details."""
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
    """Simulate a mouse drag (mouse movement while a button is held down) to a
    point on the screen.

    The x and y parameters specify where the cursor should move to. A
    None values means the current mouse x/y position will be used.
    The duration parameter specifies how long (in seconds) it should take the
    mouse cursor to move to this position. A duration of 0.0 means that the
    mouse cursor will move to the new position instantaneously.
    The tween parameter specifies the tweening function to use for the
    movement. See the tweens.py file for more details.
    The button parameter should be one of 'left', 'middle', 'right' (or 1, 2, or
    3) respectively."""
    mouseDown(button)
    _mouseMoveDragTo('drag', x, y, duration, tween)
    mouseUp(button)


def dragRel(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween, button='left'):
    """Simulate a mouse drag (mouse movement while a button is held down) to a
    point on the screen, relative to its current position.

    The x and y parameters specify where the cursor should move to. A
    None values means the current mouse x/y position will be used.
    The duration parameter specifies how long (in seconds) it should take the
    mouse cursor to move to this position. A duration of 0.0 means that the
    mouse cursor will move to the new position instantaneously.
    The tween parameter specifies the tweening function to use for the
    movement. See the tweens.py file for more details.
    The button parameter should be one of 'left', 'middle', 'right' (or 1, 2, or
    3) respectively."""
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

def keyDown(character):
    if len(character) > 1:
        character = character.lower()
    platformModule._keyDown(character)

def keyUp(character):
    if len(character) > 1:
        character = character.lower()
    platformModule._keyUp(character)

def press(character):
    if len(character) > 1:
        character = character.lower()
    platformModule._keyDown(character)
    platformModule._keyUp(character)

def typewrite(message, interval=0.0):
    message = str(message)
    interval = float(interval)


    for c in message:
        if len(c) > 1:
            c = c.lower()
        press(c)
        time.sleep(interval)

def hotkey(*args, **kwargs):
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




