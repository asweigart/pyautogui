
=====================
Cookbook and Examples
=====================

TODO - more examples are needed

Start an app and focus on its window (Windows)
----------------------------------------------

This can be used for functional tests of an application with a GUI.

.. code-block:: python

    import subprocess
    import sys
    import pyautogui

    # start the app in a separate process using the same interpreter as this script
    process = subprocess.Popen([sys.executable, 'our_app.py'])

    # wait for the window
    while True:
        window = pyautogui.getWindow("our window's title")
        if window:
            window.set_foreground()
            break

    # ...interact with the window using PyAutoGUI...
    pyautogui.hotkey('alt', 'F4')

