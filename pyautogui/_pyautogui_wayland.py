"""
To Implement:
(LAZY IMPLEMENT) [ ] _mouse_is_swapped: Check if LR mouse buttons are swapped.
"""

import pyautogui
import sys
import os
import subprocess
from pyautogui import LEFT, MIDDLE, RIGHT

import wayland_automation
import pyscreenshot
import pydotool
from pydotool import ClickEnum
from PIL import Image
import time

SCALING = 1
SIZE = None
_display = None
ISGNOME = os.getenv("XDG_CURRENT_DESKTOP") == "ubuntu:GNOME"
if ISGNOME:
    try:
        import gnomopo
        SIZE = gnomopo.getsize()
        SCALING = SIZE.pop()
        print("SIZE", SIZE, "SCALING", SCALING)
    except:
        print("\n\nyou're running ubuntu gnome!")
        print("you need gnomopo for mouse position and screen sizing, so do this:\n")
        print("1) $> pip install gnomopo")
        print("2) $> gnomopo install")
        print("3) log in and out to restart your gnome session")
        print("4) $> gnomopo enable\n")
        print("then pyautogui should work fine\n\n")

def setWindow(offset=0):
    global _display, SIZE
    _display = gnomopo.getwindow(rect="frame")
    _display["y"] -= offset # browser address bar etc
    _display["height"] -= offset
    print("using window geo", _display)
    SIZE = [_display["width"], _display["height"]]

def _position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple.

    Returns:
        (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    if ISGNOME:
        x, y = gnomopo.getpos()
    else:
        gen = wayland_automation.mouse_position_generator()
        x, y = next(gen)
        gen.close()
    if _display:
        x -= _display["x"]
        y -= _display["y"]
    x, y = x*SCALING, y*SCALING
    return x, y

def _size():
    # We will cache the screen size as this process is not the fastest.
    global SIZE
    if SIZE is not None:
        return SIZE
    im: Image.Image = pyscreenshot.grab()
    SIZE = im.size
    return SIZE


def _moveTo(x, y):
    cur_x, cur_y = _position()
    dx = (x - cur_x) / SCALING
    dy = (y - cur_y) / SCALING
    subprocess.run(["ydotool", "mousemove", "-x", str(dx), "-y", str(dy)])
    time.sleep(pyautogui.WAYLAND_MOVE_TIME)

if "Getting constant values" and not ISGNOME:
    init_x, init_y = _position()
    w, h = _size()
    
    _moveTo(w, h)
    x, y = _position()
    _moveTo(init_x, init_y)
    new_x, new_y = _position()
    if init_x != new_x:
        raise Exception("Please disable mouse acceleration.\nPyAutoGUI does not work properly with acceleration enabled.\nDevice name should be 'ydotool virtual device'")
    SCALING = w/x

def _vscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return

    if x is not None and y is not None:
        _moveTo(x, y)

    subprocess.run(["ydotool", "mousemove", "-w", "-x", "0", "-y", str(clicks)])


def _hscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return

    if x is not None and y is not None:
        _moveTo(x, y)

    subprocess.run(["ydotool", "mousemove", "-w", "-x", str(clicks), "-y", "0"])


def _scroll(clicks, x=None, y=None):
    return _vscroll(clicks, x, y)


def __click(code:int):
    code = hex(code)
    time.sleep(pyautogui.WAYLAND_CLICK_TIME)
    subprocess.run(["ydotool", "click", code])
    time.sleep(pyautogui.WAYLAND_CLICK_TIME)

def _click(x, y, button):
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        __click(ClickEnum.LEFT | ClickEnum.LEFT_CLICK)
    if button == MIDDLE:
        __click(ClickEnum.MIDDLE | ClickEnum.MOUSE_CLICK)
    if button == RIGHT:
        __click(ClickEnum.RIGHT | ClickEnum.LEFT_CLICK)


def _mouse_is_swapped():
    # TODO: Cant figure out how to get this, so assuming the value is False.
    return False


def _mouseDown(x, y, button):
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        __click(ClickEnum.LEFT | ClickEnum.MOUSE_DOWN)
    if button == MIDDLE:
        __click(ClickEnum.MIDDLE | ClickEnum.MOUSE_DOWN)
    if button == RIGHT:
        __click(ClickEnum.RIGHT | ClickEnum.MOUSE_DOWN)


def _mouseUp(x, y, button):
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        __click(ClickEnum.LEFT | ClickEnum.MOUSE_UP)
    if button == MIDDLE:
        __click(ClickEnum.MIDDLE | ClickEnum.MOUSE_UP)
    if button == RIGHT:
        __click(ClickEnum.RIGHT | ClickEnum.MOUSE_UP)


""" Information for keyboardMapping derived from PyKeyboard's special_key_assignment() function.

The *KB dictionaries in pyautogui map a string that can be passed to keyDown(),
keyUp(), or press() into the code used for the OS-specific keyboard function.

They should always be lowercase, and the same keys should be used across all OSes."""
keyboardMapping = dict([(key, None) for key in pyautogui.KEY_NAMES])
keyboardMapping.update(
    {
        "\t": pydotool.KEY_TAB,
        "\n": pydotool.KEY_ENTER,
        "\r": pydotool.KEY_ENTER,
        " ": pydotool.KEY_SPACE,
        "!": pydotool.KEY_1 | pydotool.FLAG_UPPERCASE,
        '"': pydotool.KEY_APOSTROPHE | pydotool.FLAG_UPPERCASE,
        "#": pydotool.KEY_3 | pydotool.FLAG_UPPERCASE,
        "$": pydotool.KEY_4 | pydotool.FLAG_UPPERCASE,
        "%": pydotool.KEY_5 | pydotool.FLAG_UPPERCASE,
        "&": pydotool.KEY_7 | pydotool.FLAG_UPPERCASE,
        "'": pydotool.KEY_APOSTROPHE,
        "(": pydotool.KEY_9 | pydotool.FLAG_UPPERCASE,
        ")": pydotool.KEY_0 | pydotool.FLAG_UPPERCASE,
        "*": pydotool.KEY_8 | pydotool.FLAG_UPPERCASE,
        "+": pydotool.KEY_EQUAL | pydotool.FLAG_UPPERCASE,
        ",": pydotool.KEY_COMMA,
        "-": pydotool.KEY_MINUS,
        ".": pydotool.KEY_DOT,
        "/": pydotool.KEY_SLASH,
        "0": pydotool.KEY_0,
        "1": pydotool.KEY_1,
        "2": pydotool.KEY_2,
        "3": pydotool.KEY_3,
        "4": pydotool.KEY_4,
        "5": pydotool.KEY_5,
        "6": pydotool.KEY_6,
        "7": pydotool.KEY_7,
        "8": pydotool.KEY_8,
        "9": pydotool.KEY_9,
        ":": pydotool.KEY_SEMICOLON | pydotool.FLAG_UPPERCASE,
        ";": pydotool.KEY_SEMICOLON,
        "<": pydotool.KEY_COMMA | pydotool.FLAG_UPPERCASE,
        "=": pydotool.KEY_EQUAL,
        ">": pydotool.KEY_DOT | pydotool.FLAG_UPPERCASE,
        "?": pydotool.KEY_SLASH | pydotool.FLAG_UPPERCASE,
        "@": pydotool.KEY_2 | pydotool.FLAG_UPPERCASE,
        "[": pydotool.KEY_LEFTBRACE,
        "\\": pydotool.KEY_BACKSLASH,
        "]": pydotool.KEY_RIGHTBRACE,
        "^": pydotool.KEY_6 | pydotool.FLAG_UPPERCASE,
        "_": pydotool.KEY_MINUS | pydotool.FLAG_UPPERCASE,
        "`": pydotool.KEY_GRAVE,
        "a": pydotool.KEY_A,
        "b": pydotool.KEY_B,
        "c": pydotool.KEY_C,
        "d": pydotool.KEY_D,
        "e": pydotool.KEY_E,
        "f": pydotool.KEY_F,
        "g": pydotool.KEY_G,
        "h": pydotool.KEY_H,
        "i": pydotool.KEY_I,
        "j": pydotool.KEY_J,
        "k": pydotool.KEY_K,
        "l": pydotool.KEY_L,
        "m": pydotool.KEY_M,
        "n": pydotool.KEY_N,
        "o": pydotool.KEY_O,
        "p": pydotool.KEY_P,
        "q": pydotool.KEY_Q,
        "r": pydotool.KEY_R,
        "s": pydotool.KEY_S,
        "t": pydotool.KEY_T,
        "u": pydotool.KEY_U,
        "v": pydotool.KEY_V,
        "w": pydotool.KEY_W,
        "x": pydotool.KEY_X,
        "y": pydotool.KEY_Y,
        "z": pydotool.KEY_Z,
        "A": pydotool.KEY_A,
        "B": pydotool.KEY_B,
        "C": pydotool.KEY_C,
        "D": pydotool.KEY_D,
        "E": pydotool.KEY_E,
        "F": pydotool.KEY_F,
        "G": pydotool.KEY_G,
        "H": pydotool.KEY_H,
        "I": pydotool.KEY_I,
        "J": pydotool.KEY_J,
        "K": pydotool.KEY_K,
        "L": pydotool.KEY_L,
        "M": pydotool.KEY_M,
        "N": pydotool.KEY_N,
        "O": pydotool.KEY_O,
        "P": pydotool.KEY_P,
        "Q": pydotool.KEY_Q,
        "R": pydotool.KEY_R,
        "S": pydotool.KEY_S,
        "T": pydotool.KEY_T,
        "U": pydotool.KEY_U,
        "V": pydotool.KEY_V,
        "W": pydotool.KEY_W,
        "X": pydotool.KEY_X,
        "Y": pydotool.KEY_Y,
        "Z": pydotool.KEY_Z,
        "{": pydotool.KEY_LEFTBRACE | pydotool.FLAG_UPPERCASE,
        "|": pydotool.KEY_BACKSLASH | pydotool.FLAG_UPPERCASE,
        "}": pydotool.KEY_RIGHTBRACE | pydotool.FLAG_UPPERCASE,
        "~": pydotool.KEY_GRAVE | pydotool.FLAG_UPPERCASE,
        "add": pydotool.KEY_KPPLUS,
        "alt": pydotool.KEY_LEFTMETA,
        "altleft": pydotool.KEY_LEFTMETA,
        "altright": pydotool.KEY_RIGHTMETA,
        "backspace": pydotool.KEY_BACKSPACE,
        "\b": pydotool.KEY_BACKSPACE,
        "capslock": pydotool.KEY_CAPSLOCK,
        "ctrl": pydotool.KEY_LEFTCTRL,
        "ctrlleft": pydotool.KEY_LEFTCTRL,
        "ctrlright": pydotool.KEY_RIGHTCTRL,
        "decimal": pydotool.KEY_KPDOT,
        "del": pydotool.KEY_DELETE,
        "delete": pydotool.KEY_DELETE,
        "divide": pydotool.KEY_KPSLASH,
        "down": pydotool.KEY_DOWN,
        "end": pydotool.KEY_END,
        "enter": pydotool.KEY_ENTER,
        "esc": pydotool.KEY_ESC,
        "escape": pydotool.KEY_ESC,
        "f1": pydotool.KEY_F1,
        "f2": pydotool.KEY_F2,
        "f3": pydotool.KEY_F3,
        "f4": pydotool.KEY_F4,
        "f5": pydotool.KEY_F5,
        "f6": pydotool.KEY_F6,
        "f7": pydotool.KEY_F7,
        "f8": pydotool.KEY_F8,
        "f9": pydotool.KEY_F9,
        "f10": pydotool.KEY_F10,
        "f11": pydotool.KEY_F11,
        "f12": pydotool.KEY_F12,
        "f13": pydotool.KEY_F13,
        "f14": pydotool.KEY_F14,
        "f15": pydotool.KEY_F15,
        "f16": pydotool.KEY_F16,
        "f17": pydotool.KEY_F17,
        "f18": pydotool.KEY_F18,
        "f19": pydotool.KEY_F19,
        "f20": pydotool.KEY_F20,
        "f21": pydotool.KEY_F21,
        "f22": pydotool.KEY_F22,
        "f23": pydotool.KEY_F23,
        "f24": pydotool.KEY_F24,
        "help": pydotool.KEY_HELP,
        "home": pydotool.KEY_HOME,
        "insert": pydotool.KEY_INSERT,
        "left": pydotool.KEY_LEFT,
        "multiply": pydotool.KEY_KPASTERISK,
        "num0": pydotool.KEY_KP0,
        "num1": pydotool.KEY_KP1,
        "num2": pydotool.KEY_KP2,
        "num3": pydotool.KEY_KP3,
        "num4": pydotool.KEY_KP4,
        "num5": pydotool.KEY_KP5,
        "num6": pydotool.KEY_KP6,
        "num7": pydotool.KEY_KP7,
        "num8": pydotool.KEY_KP8,
        "num9": pydotool.KEY_KP9,
        "numlock": pydotool.KEY_NUMLOCK,
        "pagedown": pydotool.KEY_PAGEDOWN,
        "pageup": pydotool.KEY_PAGEUP,
        "pause": pydotool.KEY_PAUSE,
        "pgdn": pydotool.KEY_PAGEDOWN,
        "pgup": pydotool.KEY_PAGEUP,
        "print": pydotool.KEY_PRINT,
        "printscreen": pydotool.KEY_PRINT,
        "prntscrn": pydotool.KEY_PRINT,
        "prtsc": pydotool.KEY_PRINT,
        "prtscr": pydotool.KEY_PRINT,
        "return": pydotool.KEY_ENTER,
        "right": pydotool.KEY_RIGHT,
        "scrolllock": pydotool.KEY_SCROLLLOCK,
        "shift": pydotool.KEY_LEFTSHIFT,
        "shiftleft": pydotool.KEY_LEFTSHIFT,
        "shiftright": pydotool.KEY_RIGHTSHIFT,
        "sleep": pydotool.KEY_SLEEP,
        "space": pydotool.KEY_SPACE,
        "stop": pydotool.KEY_STOP,
        "subtract": pydotool.KEY_KPMINUS,
        "tab": pydotool.KEY_TAB,
        "up": pydotool.KEY_UP,
        "volumedown": pydotool.KEY_VOLUMEDOWN,
        "volumemute": pydotool.KEY_MUTE,
        "volumeup": pydotool.KEY_VOLUMEUP,
        "win": None,
        "winleft": None,
        "winright": None,
    }
)

def __sendkey(keys:list[tuple[int, int]], next_delay:int | float | None = None):
    seq = [] if next_delay is None else [f"--key-delay={next_delay}"]
    for key, mod in keys:
        seq.append(f'{key}:{mod}')
    e = subprocess.run(["ydotool", "key", *seq])
    e.check_returncode()
    

def _keyDown(key):
    """Performs a keyboard key press without the release. This will put that
    key in a held down state.

    Args:
      key (str): The key to be pressed down. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """
    
    if type(key) is int:
        __sendkey([(key, pydotool.DOWN)])
        return
    
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    needsShift = pyautogui.isShiftCharacter(key)
    if needsShift:
        __sendkey([(pydotool.KEY_LEFTSHIFT, pydotool.DOWN), (keyboardMapping[key], pydotool.DOWN), (pydotool.KEY_LEFTSHIFT, pydotool.UP)])
    else:
        __sendkey([(keyboardMapping[key], pydotool.DOWN)])


def _keyUp(key):
    """Performs a keyboard key release (without the press down beforehand).

    Args:
      key (str): The key to be released up. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if type(key) is int:
        keycode = key
    else:
        keycode = keyboardMapping[key]

    __sendkey([(keycode, pydotool.UP)])
