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

**NOTE** - PyAutoGUI is not yet ready for deployment. It has only been tested widely on Windows 7 for Python 3.4. Also, this documentation is ugly and incomplete for now.

Dependencies
============

On Windows, PyAutoGUI has no dependencies. It does **not** need the pywin32 module installed since it uses Python's own ctypes module.

On OS X, PyAutoGUI requires [PyObjC](http://pythonhosted.org/pyobjc/install.html) installed for the AppKit and Quartz modules.

On Linux, PyAutoGUI requires python3-Xlib module installed.
