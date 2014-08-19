.. default-role:: code
============
Introduction
============

Purpose
=======

The purpose of PyAutoGUI is to provide a cross-platform Python module for GUI automation *for human beings*. The API is designed to be as simple as possible with sensible defaults.

For example, here is the complete code to move the mouse to the middle of the screen on Windows, OS X, and Linux:

.. code:: python

    import pyautogui
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

And that is all.

PyAutoGUI can simulate moving the mouse, clicking the mouse, dragging with the mouse, pressing keys, pressing and holding keys, and pressing keyboard hotkey combinations.

Dependencies
============

On Windows, PyAutoGUI has no dependencies. It does **not** need the ``pywin32`` module installed since it uses Python's own ``ctypes`` module.

On OS X, PyAutoGUI requires `PyObjC<http://pythonhosted.org/pyobjc/install.html>`_ installed for the AppKit and Quartz modules. The module names on PyPI to install are ``pyobjc-core`` and ``pyobjc`` (in that order).

On Linux, PyAutoGUI requires ``python-xlib`` (for Python 2) or ``python3-Xlib`` (for Python 3) module installed.
