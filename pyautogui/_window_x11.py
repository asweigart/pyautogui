from Xlib import X, Xutil, protocol
from Xlib.protocol import event
from Xlib.display import Display

import sys
if sys.platform in ('java', 'darwin', 'win32'):
    raise Exception('The _window_x11 module should only be loaded on a Unix system that supports X11.')

NET_CLOSE_WINDOW = Display().intern_atom("_NET_CLOSE_WINDOW")
NET_CLIENT_LIST = Display().intern_atom("_NET_CLIENT_LIST")
NET_WM_STATE = Display().intern_atom("_NET_WM_STATE")
WM_CHANGE_STATE = Display().intern_atom("WM_CHANGE_STATE")
NET_WM_NAME = Display().intern_atom("_NET_WM_NAME")
NET_WM_STATE_ABOVE = Display().intern_atom("_NET_WM_STATE_ABOVE")
NET_WM_STATE_MAXIMIZED_HORZ = Display().intern_atom("_NET_WM_STATE_MAXIMIZED_HORZ")
NET_WM_STATE_MAXIMIZED_VERT = Display().intern_atom("_NET_WM_STATE_MAXIMIZED_VERT")

# https://standards.freedesktop.org/wm-spec/wm-spec-1.3.html#idm140130317598336

NET_WM_STATE_REMOVE = 0
NET_WM_STATE_ADD = 1
NET_WM_STATE_TOGGLE = 2

def win_send_event(root, window, ctype, data, mask=None):
    data = (data + ([0] * (5 - len(data))))[:5] 
    ev = event.ClientMessage(window=window, client_type=ctype, data=(32, (data)))
    root.send_event(ev, event_mask=X.SubstructureRedirectMask|X.SubstructureNotifyMask)


class Window(object):

    def __init__(self, win_id):
        self.dpy = Display()
        self.screen = self.dpy.screen()
        self.root = self.screen.root
        self._hwnd = self.dpy.create_resource_object('window', win_id)

    def set_position(self, x, y, width, height):
        """Set window top-left corner position and size"""
        self._hwnd.configure(x=x, y=y, width=width, height=height)
        self.dpy.sync()

    def move(self, x, y):
        """Move window top-left corner to position"""
        self._hwnd.configure(x=x, y=y)
        self.dpy.sync()

    def resize(self, width, height):
        """Change window size"""
        self._hwnd.configure(width=width, height=height)
        self.dpy.sync()

    def maximize(self):
        win_send_event(self.root, self._hwnd, NET_WM_STATE, [NET_WM_STATE_TOGGLE, NET_WM_STATE_MAXIMIZED_HORZ, NET_WM_STATE_MAXIMIZED_VERT])
        self.dpy.sync()

    def set_foreground(self):
        self._hwnd.set_input_focus(X.RevertToParent, X.CurrentTime)
        win_send_event(self.root, self._hwnd, NET_WM_STATE, [NET_WM_STATE_ADD, NET_WM_STATE_ABOVE])
        self.dpy.sync()

    def minimize(self):
        win_send_event(self.root, self._hwnd, WM_CHANGE_STATE, [Xutil.IconicState])
        self.dpy.sync()

    def restore(self):
        self._hwnd.map()
        self.dpy.sync()

    def close(self):
        win_send_event(self.root, self._hwnd, NET_CLOSE_WINDOW, [])
        self.dpy.sync()

    def get_position(self):
        # get_geometry() in KDE5 always returns zero x and y
        coords = self._hwnd.translate_coords(self.root,0,0)
        # translate_coords always returns inverted coordinates
        if coords.x < 0:
            x = abs(coords.x)
        else:
            x = coords.x*-1
        if coords.y < 0:
            y = abs(coords.y)
        else:
            y = coords.y*-1

        return x,y

    #def moveRel(self, x=0, y=0):
        # moves relative to the x, y of top-left corner of the window
        #pass
    #def clickRel(self, x=0, y=0, clicks=1, interval=0.0, button='left'):
        #  click relative to the x, y of top-left corner of the window
        #pass


def getWindows():
    """Return dict: {'window title' : window id} for all visible windows"""

    titles = {}

    display = Display()
    root = display.screen().root
    win_list = root.get_full_property(NET_CLIENT_LIST, X.AnyPropertyType).value
    for win_id in win_list:
        window = display.create_resource_object('window', win_id)
        class_list = window.get_wm_class()
        """
        get_wm_name() method unable to handle utf-8 characters, thats why
        below window title gets from property and decoding instead of using 
        one short Window method that provided by python xlib
        """
        try:
            win_name = window.get_full_property(NET_WM_NAME,X.AnyPropertyType).value
        except:
            pass
        if win_name:
            try:
                win_name = win_name.decode("utf-8")
            except:
                pass
            titles[win_name] = win_id
        else:
            titles[class_list[1]] = win_id

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
