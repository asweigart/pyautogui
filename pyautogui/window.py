# Window-handling features of PyAutoGUI

# UNDER CONSTRUCTION

"""
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
 """