=========
PyAutoGUI
=========

PyAutoGUI is a  cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

Full documentation available at https://pyautogui.readthedocs.org

Source code available at https://github.com/asweigart/pyautogui

Dependencies
============

Windows has no dependencies. The Win32 extensions do not need to be installed.

OS X needs the pyobjc-core and pyobjc module installed (in that order).

Linux needs the python3-Xlib (or python-Xlib for Python 2) module installed.

Pillow needs to be installed, and on Linux you may need to install additional libraries to make sure Pillow's PNG/JPEG works correctly. See:

    https://stackoverflow.com/questions/7648200/pip-install-pil-e-tickets-1-no-jpeg-png-support

    http://ubuntuforums.org/showthread.php?t=1751455

Example Usage
=============

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
