pyautogui
=========

A cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse &amp; keyboard.

THIS MODULE IS UNDER DEVELOPMENT NOT YET IN A USABLE STATE.

This module seeks to replace PyUserInput, PyKeyboard, PyMouse, pykey, and pyhook. See the roadmap in the documentation.

NOTE - It is a known issue that the keyboard-related functions don't work on Ubuntu VMs in Virtualbox.


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

    >>> pyautogui.press('left', 'left', 'left', 'left', 'left', 'left')

    >>> pyautogui.keyUp('shift')

    >>> pyautogui.hotkey('ctrl', 'c')


