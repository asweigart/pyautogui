
=======
Roadmap
=======

PyAutoGUI is planned as a replacement for other Python GUI automation scripts, such as PyUserInput, PyKeyboard, PyMouse, pykey, etc. Eventually it would be great to offer the same type of features that [Sikuli](http://www.sikuli.org) offers.

For now, the primary aim for PyAutoGUI is cross-platform mouse and keyboard control and a simple API.

Future features planned (specific versions not planned yet):

- Find a list of all windows and their captions.
- Click coordinates relative to a window, instead of the entire screen.
- Make it easier to work on systems with multiple monitors.
- Basic image recognition, using the Pillow/PIL modules.
- GetKeyState() type of function
- Ability to set global hotkey on all platforms so that there can be an easy "kill switch" for GUI automation programs.
- Optional nonblocking pyautogui calls.


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

Screencapture features (requires PIL/Pillow)
 - locate(image_filename, region=(x, y, width, height)) # returns the center (x, y) of the image found on a current screenshot
 - locateAll(image_filename, region=(x, y, width, height))  # returns a list of (centerx, centery)
 - screenshot()   # returns PIL object (provides cross-platform interface for getting screenshots, since PIL only support screen grabs on Windows.)
 - screenshot(image_filename) # saves the screenshot to a file

Message Box inputs:
 - pyautogui.alert(text, title='PyAutoGUI', button='Ok')
 - pyautogui.confirm(text, buttons=['Ok', 'Cancel'])   # returns string of buttonpressed
 - pyautogui.prompt(text)  # returns text entered
 - pyautogui.password(text)  # like prompt(), but uses asterisks when typing in information