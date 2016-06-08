.. default-role:: code

============
Installation
============

To install PyAutoGUI, install the `pyautogui` package from PyPI and dependencies.

On Windows, this is:

    ``C:\Python34\pip.exe install pyautogui``

(Though you may have a different version of Python installed other than 3.4)

On OS X, this is:

    ``pip3 install pyobjc-core``

    ``pip3 install pyobjc``

    ``pip3 install pyautogui``

If you are running El Capitan and have problems installing pyobjc try:

    ``MACOSX_DEPLOYMENT_TARGET=10.11 pip install pyobjc``

On Linux, this is:

    ``pip3 install python3-xlib``

    ``sudo apt-get install scrot``

    ``sudo apt-get install python3-tk``

    ``sudo apt-get install python3-dev``

    ``pip3 install pyautogui``

PyAutoGUI will try to install Pillow (for its screenshot capabilities). This happens when pip installs PyAutoGUI.
