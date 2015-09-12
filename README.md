PyAutoGUI
=========

PyAutoGUI is a  cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

Full documentation available at https://pyautogui.readthedocs.org

Source code available at https://github.com/asweigart/pyautogui

Dependencies
============

If you are installing PyAutoGUI from PyPI using pip:

Windows has no dependencies. The Win32 extensions do not need to be installed.

OS X needs the pyobjc-core and pyobjc module installed (in that order).

Linux needs the python3-Xlib (or python-Xlib for Python 2) module installed.

Pillow needs to be installed, and on Linux you may need to install additional libraries to make sure Pillow's PNG/JPEG works correctly. See:

    https://stackoverflow.com/questions/7648200/pip-install-pil-e-tickets-1-no-jpeg-png-support

    http://ubuntuforums.org/showthread.php?t=1751455

If you want to do development and contribute to PyAutoGUI, you will need to install these modules from PyPI:

* pyscreeze
* pymsgbox
* pytweening

Example Usage
=============

Keyboard and Mouse Control
--------------------------
```python
    >>> import pyautogui
    >>> screenWidth, screenHeight = pyautogui.size()
    >>> currentMouseX, currentMouseY = pyautogui.position()
    >>> pyautogui.moveTo(100, 150)
    >>> pyautogui.click()
    >>> pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
    >>> pyautogui.doubleClick()
    >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
    >>> pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    >>> pyautogui.press('esc')
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
    >>> pyautogui.keyUp('shift')
    >>> pyautogui.hotkey('ctrl', 'c')
```

Display Message Boxes
---------------------
```python
    >>> import pyautogui
    >>> pyautogui.alert('This is an alert box.')
    'OK'
    >>> pyautogui.confirm('Shall I proceed?')
    'Cancel'
    >>> pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
    'B'
    >>> pyautogui.prompt('What is your name?')
    'Al'
    >>> pyautogui.password('Enter password (text will be hidden)')
    'swordfish'
```
Screenshot Functions
--------------------

(PyAutoGUI uses Pillow for image-related features.)
```python
    >>> import pyautogui
    >>> im1 = pyautogui.screenshot()
    >>> im1.save('my_screenshot.png')
    >>> im2 = pyautogui.screenshot('my_screenshot2.png')
```
You can also locate where an image is on the screen:
```python
    >>> import pyautogui
    >>> button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    >>> button7location
    (1416, 562, 50, 41)
    >>> buttonx, buttony = pyautogui.center(button7location)
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
```
The locateCenterOnScreen() function returns the center of this match region:
```python
    >>> import pyautogui
    >>> buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
```
