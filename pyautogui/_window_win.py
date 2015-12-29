# Window-handling features of PyAutoGUI for win_32
import ctypes
import ctypes.wintypes

import sys
if sys.platform != 'win32':
    raise Exception('The _window_win module should only be loaded on a Windows system.')

SetWindowPos = ctypes.windll.user32.SetWindowPos
# Flags for SetWindowPos:
SWP_NOMOVE = ctypes.c_uint(0x0002)
SWP_NOSIZE = ctypes.c_uint(0x0001)

ShowWindow = ctypes.windll.user32.ShowWindow
# Flags for ShowWindow:
SW_MAXIMIZE = 3
SW_MINIMIZE = 6
SW_RESTORE = 9

SwitchToThisWindow = ctypes.windll.user32.SwitchToThisWindow
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow
CloseWindow = ctypes.windll.user32.CloseWindow
GetWindowRect = ctypes.windll.user32.GetWindowRect

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


class _Rect(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]


class Window(object):

    def __init__(self, hwnd):
        self._hwnd = hwnd         # Window handle

    def set_position(self, x, y, width, height):
        """Set window top-left corner position and size"""
        SetWindowPos(self._hwnd, None, x, y, width, height, ctypes.c_uint(0))

    def move(self, x, y):
        """Move window top-left corner to position"""
        SetWindowPos(self._hwnd, None, x, y, 0, 0, SWP_NOSIZE)

    def resize(self, width, height):
        """Change window size"""
        SetWindowPos(self._hwnd, None, 0, 0, width, height, SWP_NOMOVE)

    def maximize(self):
        ShowWindow(self._hwnd, SW_MAXIMIZE)

    def set_foreground(self):
        SetForegroundWindow(self._hwnd)

    def minimize(self):
        ShowWindow(self._hwnd, SW_MINIMIZE)

    def restore(self):
        ShowWindow(self._hwnd, SW_RESTORE)

    def close(self):
        CloseWindow(self._hwnd)

    def get_position(self):
        """Returns tuple of 4 numbers: (x, y)s of top-left and bottom-right corners"""
        rect = _Rect()
        GetWindowRect(self._hwnd, ctypes.pointer(rect))
        return rect.left, rect.top, rect.right, rect.bottom

    # def moveRel(self, x=0, y=0):   # moves relative to the x, y of top-left corner of the window
    #     pass
    # def clickRel(self, x=0, y=0, clicks=1, interval=0.0, button='left'):
        #  click relative to the x, y of top-left corner of the window
    #     pass


def getWindows():    #https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/
    """Return dict: {'window title' : window handle} for all visible windows"""
    titles = {}

    def foreach_window(hwnd, lparam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles[buff.value] = hwnd
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)

    return titles

def getWindow(title, exact=False):
    """Return Window object if 'title' or its part found in visible windows titles, else return None

    Return only 1 window found first
    Args:
        title: unicode string
        exact (bool): True if search only exact match
    """
    titles = getWindows()
    hwnd = titles.get(title, None)
    if not hwnd and not exact:
        for k, v in titles.items():
            if title in k:
                hwnd = v
                break
    if hwnd:
        return Window(hwnd)
    else:
        return None
