
=======
Roadmap
=======

PyAutoGUI is planned as a replacement for other Python GUI automation scripts, such as PyUserInput, PyKeyboard, PyMouse, pykey, etc. Eventually it would be great to offer the same type of features that Sikuli_ offers.

For now, the primary aim for PyAutoGUI is cross-platform mouse and keyboard control and a simple API.

Future features planned (specific versions not planned yet):

- A tool for determining why an image can't be found in a particular screenshot. (This is a common source of questions for users.)
- Full compatibility on Raspberry Pis.
- "Wave" function, which is used just to see where the mouse is by shaking the mouse cursor a bit. A small helper function.
- locateNear() function, which is like the other locate-related screen reading functions except it finds the first instance near an xy point on the screen.
- Find a list of all windows and their captions.
- Click coordinates relative to a window, instead of the entire screen.
- Make it easier to work on systems with multiple monitors.
- GetKeyState() type of function
- Ability to set global hotkey on all platforms so that there can be an easy "kill switch" for GUI automation programs.
- Optional nonblocking pyautogui calls.
- "strict" mode for keyboard - passing an invalid keyboard key causes an exception instead of silently skipping it.
- rename keyboardMapping to KEYBOARD_MAPPING
- Ability to convert png and other image files into a string that can be copy/pasted directly in the source code, so that they don't have to be shared separately with people's pyautogui scripts.
- Test to make sure pyautogui works in Windows/mac/linux VMs.
- A way to compare two images and highlight differences between them (good for pointing out when a UI changes, etc.)

Window handling features:
 - pyautogui.getWindows()      # returns a dict of window titles mapped to window IDs
 - pyautogui.getWindow(str_title_or_int_id)   # returns a "Win" object
 - win.move(x, y)
 - win.resize(width, height)
 - win.maximize()
 - win.minimize()
 - win.restore()
 - win.close()
 - win.position()  # returns (x, y) of top-left corner
 - win.moveRel(x=0, y=0)   # moves relative to the x, y of top-left corner of the window
 - win.clickRel(x=0, y=0, clicks=1, interval=0.0, button='left')  # click relative to the x, y of top-left corner of the window
 - Additions to screenshot functionality so that it can capture specific windows instead of full screen.

.. _Sikuli: http://www.sikuli.org
