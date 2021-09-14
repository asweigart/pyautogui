PyAutoGUI
=========

PyAutoGUI is a  cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

`pip install pyautogui`

Full documentation available at https://pyautogui.readthedocs.org

Simplified Chinese documentation available at https://github.com/asweigart/pyautogui/blob/master/docs/simplified-chinese.ipynb

Source code available at https://github.com/asweigart/pyautogui

If you need help installing Python, visit https://installpython3.com/

Dependencies
============

PyAutoGUI supports Python 2 and 3. If you are installing PyAutoGUI from PyPI using pip:

Windows has no dependencies. The Win32 extensions do not need to be installed.

macOS needs the pyobjc-core and pyobjc module installed (in that order).

Linux needs the python3-xlib (or python-xlib for Python 2) module installed.

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

The x, y coordinates used by PyAutoGUI has the 0, 0 origin coordinates in the top left corner of the screen. The x coordinates increase going to the right (just as in mathematics) but the y coordinates increase going down (the opposite of mathematics). On a screen that is 1920 x 1080 pixels in size, coordinates 0, 0 are for the top left while 1919, 1079 is for the bottom right.

Currently, PyAutoGUI only works on the primary monitor. PyAutoGUI isn't reliable for the screen of a second monitor (the mouse functions may or may not work on multi-monitor setups depending on your operating system and version).

All keyboard presses done by PyAutoGUI are sent to the window that currently has focus, as if you had pressed the physical keyboard key.

```python
    >>> import pyautogui
    >>> screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    >>> currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    >>> pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    >>> pyautogui.click() # Click the mouse at its current location.
    >>> pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    >>> pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    >>> pyautogui.doubleClick() # Double click the mouse at the
    >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    >>> pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    >>> pyautogui.press('esc') # Simulate pressing the Escape key.
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
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

How Does PyAutoGUI Work?
========================

The three major operating systems (Windows, macOS, and Linux) each have different ways to programmatically control the mouse and keyboard. This can often involve confusing, obscure, and deeply technical details. The job of PyAutoGUI is to hide all of this complexity behind a simple API.

* On Windows, PyAutoGUI accesses the Windows API (also called the WinAPI or win32 API) through the built-in `ctypes` module. The `nicewin` module at https://github.com/asweigart/nicewin provides a demonstration for how Windows API calls can be made through Python.

* On macOS, PyAutoGUI uses the `rubicon-objc` module to access the Cocoa API.

* On Linux, PyAutoGUI uses the `Xlib` module to access the X11 or X Window System.


Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
