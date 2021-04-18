import time
import sys

try:
    import Quartz
except:
    assert False, "You must first install pyobjc-core and pyobjc: https://pyautogui.readthedocs.io/en/latest/install.html"
import AppKit

import pyautogui
from pyautogui import LEFT, MIDDLE, RIGHT

if sys.platform !=  'darwin':
    raise Exception('The pyautogui_osx module should only be loaded on an OS X system.')



""" Taken from events.h
/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h

The *KB dictionaries in pyautogui map a string that can be passed to keyDown(),
keyUp(), or press() into the code used for the OS-specific keyboard function.

They should always be lowercase, and the same keys should be used across all OSes."""
keyboardMapping = dict([(key, None) for key in pyautogui.KEY_NAMES])
keyboardMapping.update({
    'a': 0x00, # kVK_ANSI_A
    's': 0x01, # kVK_ANSI_S
    'd': 0x02, # kVK_ANSI_D
    'f': 0x03, # kVK_ANSI_F
    'h': 0x04, # kVK_ANSI_H
    'g': 0x05, # kVK_ANSI_G
    'z': 0x06, # kVK_ANSI_Z
    'x': 0x07, # kVK_ANSI_X
    'c': 0x08, # kVK_ANSI_C
    'v': 0x09, # kVK_ANSI_V
    'b': 0x0b, # kVK_ANSI_B
    'q': 0x0c, # kVK_ANSI_Q
    'w': 0x0d, # kVK_ANSI_W
    'e': 0x0e, # kVK_ANSI_E
    'r': 0x0f, # kVK_ANSI_R
    'y': 0x10, # kVK_ANSI_Y
    't': 0x11, # kVK_ANSI_T
    '1': 0x12, # kVK_ANSI_1
    '!': 0x12, # kVK_ANSI_1
    '2': 0x13, # kVK_ANSI_2
    '@': 0x13, # kVK_ANSI_2
    '3': 0x14, # kVK_ANSI_3
    '#': 0x14, # kVK_ANSI_3
    '4': 0x15, # kVK_ANSI_4
    '$': 0x15, # kVK_ANSI_4
    '6': 0x16, # kVK_ANSI_6
    '^': 0x16, # kVK_ANSI_6
    '5': 0x17, # kVK_ANSI_5
    '%': 0x17, # kVK_ANSI_5
    '=': 0x18, # kVK_ANSI_Equal
    '+': 0x18, # kVK_ANSI_Equal
    '9': 0x19, # kVK_ANSI_9
    '(': 0x19, # kVK_ANSI_9
    '7': 0x1a, # kVK_ANSI_7
    '&': 0x1a, # kVK_ANSI_7
    '-': 0x1b, # kVK_ANSI_Minus
    '_': 0x1b, # kVK_ANSI_Minus
    '8': 0x1c, # kVK_ANSI_8
    '*': 0x1c, # kVK_ANSI_8
    '0': 0x1d, # kVK_ANSI_0
    ')': 0x1d, # kVK_ANSI_0
    ']': 0x1e, # kVK_ANSI_RightBracket
    '}': 0x1e, # kVK_ANSI_RightBracket
    'o': 0x1f, # kVK_ANSI_O
    'u': 0x20, # kVK_ANSI_U
    '[': 0x21, # kVK_ANSI_LeftBracket
    '{': 0x21, # kVK_ANSI_LeftBracket
    'i': 0x22, # kVK_ANSI_I
    'p': 0x23, # kVK_ANSI_P
    'l': 0x25, # kVK_ANSI_L
    'j': 0x26, # kVK_ANSI_J
    "'": 0x27, # kVK_ANSI_Quote
    '"': 0x27, # kVK_ANSI_Quote
    'k': 0x28, # kVK_ANSI_K
    ';': 0x29, # kVK_ANSI_Semicolon
    ':': 0x29, # kVK_ANSI_Semicolon
    '\\': 0x2a, # kVK_ANSI_Backslash
    '|': 0x2a, # kVK_ANSI_Backslash
    ',': 0x2b, # kVK_ANSI_Comma
    '<': 0x2b, # kVK_ANSI_Comma
    '/': 0x2c, # kVK_ANSI_Slash
    '?': 0x2c, # kVK_ANSI_Slash
    'n': 0x2d, # kVK_ANSI_N
    'm': 0x2e, # kVK_ANSI_M
    '.': 0x2f, # kVK_ANSI_Period
    '>': 0x2f, # kVK_ANSI_Period
    '`': 0x32, # kVK_ANSI_Grave
    '~': 0x32, # kVK_ANSI_Grave
    ' ': 0x31, # kVK_Space
    'space': 0x31,
    '\r': 0x24, # kVK_Return
    '\n': 0x24, # kVK_Return
    'enter': 0x24, # kVK_Return
    'return': 0x24, # kVK_Return
    '\t': 0x30, # kVK_Tab
    'tab': 0x30, # kVK_Tab
    'backspace': 0x33, # kVK_Delete, which is "Backspace" on OS X.
    '\b': 0x33, # kVK_Delete, which is "Backspace" on OS X.
    'esc': 0x35, # kVK_Escape
    'escape': 0x35, # kVK_Escape
    'command': 0x37, # kVK_Command
    'shift': 0x38, # kVK_Shift
    'shiftleft': 0x38, # kVK_Shift
    'capslock': 0x39, # kVK_CapsLock
    'option': 0x3a, # kVK_Option
    'optionleft': 0x3a, # kVK_Option
    'alt': 0x3a, # kVK_Option
    'altleft': 0x3a, # kVK_Option
    'ctrl': 0x3b, # kVK_Control
    'ctrlleft': 0x3b, # kVK_Control
    'shiftright': 0x3c, # kVK_RightShift
    'optionright': 0x3d, # kVK_RightOption
    'ctrlright': 0x3e, # kVK_RightControl
    'fn': 0x3f, # kVK_Function
    'f17': 0x40, # kVK_F17
    'volumeup': 0x48, # kVK_VolumeUp
    'volumedown': 0x49, # kVK_VolumeDown
    'volumemute': 0x4a, # kVK_Mute
    'f18': 0x4f, # kVK_F18
    'f19': 0x50, # kVK_F19
    'f20': 0x5a, # kVK_F20
    'f5': 0x60, # kVK_F5
    'f6': 0x61, # kVK_F6
    'f7': 0x62, # kVK_F7
    'f3': 0x63, # kVK_F3
    'f8': 0x64, # kVK_F8
    'f9': 0x65, # kVK_F9
    'f11': 0x67, # kVK_F11
    'f13': 0x69, # kVK_F13
    'f16': 0x6a, # kVK_F16
    'f14': 0x6b, # kVK_F14
    'f10': 0x6d, # kVK_F10
    'f12': 0x6f, # kVK_F12
    'f15': 0x71, # kVK_F15
    'help': 0x72, # kVK_Help
    'home': 0x73, # kVK_Home
    'pageup': 0x74, # kVK_PageUp
    'pgup': 0x74, # kVK_PageUp
    'del': 0x75, # kVK_ForwardDelete
    'delete': 0x75, # kVK_ForwardDelete
    'f4': 0x76, # kVK_F4
    'end': 0x77, # kVK_End
    'f2': 0x78, # kVK_F2
    'pagedown': 0x79, # kVK_PageDown
    'pgdn': 0x79, # kVK_PageDown
    'f1': 0x7a, # kVK_F1
    'left': 0x7b, # kVK_LeftArrow
    'right': 0x7c, # kVK_RightArrow
    'down': 0x7d, # kVK_DownArrow
    'up': 0x7e, # kVK_UpArrow
    'yen': 0x5d, # kVK_JIS_Yen
    #'underscore' : 0x5e, # kVK_JIS_Underscore (only applies to Japanese keyboards)
    #'comma': 0x5f, # kVK_JIS_KeypadComma (only applies to Japanese keyboards)
    'eisu': 0x66, # kVK_JIS_Eisu
    'kana': 0x68, # kVK_JIS_Kana
})

"""
# TODO - additional key codes to add
  kVK_ANSI_KeypadDecimal        = 0x41,
  kVK_ANSI_KeypadMultiply       = 0x43,
  kVK_ANSI_KeypadPlus           = 0x45,
  kVK_ANSI_KeypadClear          = 0x47,
  kVK_ANSI_KeypadDivide         = 0x4B,
  kVK_ANSI_KeypadEnter          = 0x4C,
  kVK_ANSI_KeypadMinus          = 0x4E,
  kVK_ANSI_KeypadEquals         = 0x51,
  kVK_ANSI_Keypad0              = 0x52,
  kVK_ANSI_Keypad1              = 0x53,
  kVK_ANSI_Keypad2              = 0x54,
  kVK_ANSI_Keypad3              = 0x55,
  kVK_ANSI_Keypad4              = 0x56,
  kVK_ANSI_Keypad5              = 0x57,
  kVK_ANSI_Keypad6              = 0x58,
  kVK_ANSI_Keypad7              = 0x59,
  kVK_ANSI_Keypad8              = 0x5B,
  kVK_ANSI_Keypad9              = 0x5C,
"""

# add mappings for uppercase letters
for c in 'abcdefghijklmnopqrstuvwxyz':
    keyboardMapping[c.upper()] = keyboardMapping[c]

# Taken from ev_keymap.h
# http://www.opensource.apple.com/source/IOHIDFamily/IOHIDFamily-86.1/IOHIDSystem/IOKit/hidsystem/ev_keymap.h
special_key_translate_table = {
    'KEYTYPE_SOUND_UP': 0,
    'KEYTYPE_SOUND_DOWN': 1,
    'KEYTYPE_BRIGHTNESS_UP': 2,
    'KEYTYPE_BRIGHTNESS_DOWN': 3,
    'KEYTYPE_CAPS_LOCK': 4,
    'KEYTYPE_HELP': 5,
    'POWER_KEY': 6,
    'KEYTYPE_MUTE': 7,
    'UP_ARROW_KEY': 8,
    'DOWN_ARROW_KEY': 9,
    'KEYTYPE_NUM_LOCK': 10,
    'KEYTYPE_CONTRAST_UP': 11,
    'KEYTYPE_CONTRAST_DOWN': 12,
    'KEYTYPE_LAUNCH_PANEL': 13,
    'KEYTYPE_EJECT': 14,
    'KEYTYPE_VIDMIRROR': 15,
    'KEYTYPE_PLAY': 16,
    'KEYTYPE_NEXT': 17,
    'KEYTYPE_PREVIOUS': 18,
    'KEYTYPE_FAST': 19,
    'KEYTYPE_REWIND': 20,
    'KEYTYPE_ILLUMINATION_UP': 21,
    'KEYTYPE_ILLUMINATION_DOWN': 22,
    'KEYTYPE_ILLUMINATION_TOGGLE': 23
}

def _keyDown(key):
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if key in special_key_translate_table:
        _specialKeyEvent(key, 'down')
    else:
        _normalKeyEvent(key, 'down')

def _keyUp(key):
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if key in special_key_translate_table:
        _specialKeyEvent(key, 'up')
    else:
        _normalKeyEvent(key, 'up')


def _normalKeyEvent(key, upDown):
    assert upDown in ('up', 'down'), "upDown argument must be 'up' or 'down'"

    try:
        if pyautogui.isShiftCharacter(key):
            key_code = keyboardMapping[key.lower()]

            event = Quartz.CGEventCreateKeyboardEvent(None,
                        keyboardMapping['shift'], upDown == 'down')
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            # Tiny sleep to let OS X catch up on us pressing shift
            time.sleep(pyautogui.DARWIN_CATCH_UP_TIME)

        else:
            key_code = keyboardMapping[key]

        event = Quartz.CGEventCreateKeyboardEvent(None, key_code, upDown == 'down')
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        time.sleep(pyautogui.DARWIN_CATCH_UP_TIME)

    # TODO - wait, is the shift key's keyup not done?
    # TODO - get rid of this try-except.

    except KeyError:
        raise RuntimeError("Key %s not implemented." % (key))

def _specialKeyEvent(key, upDown):
    """ Helper method for special keys.

    Source: http://stackoverflow.com/questions/11045814/emulate-media-key-press-on-mac
    """
    assert upDown in ('up', 'down'), "upDown argument must be 'up' or 'down'"

    key_code = special_key_translate_table[key]

    ev = AppKit.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
            Quartz.NSSystemDefined, # type
            (0,0), # location
            0xa00 if upDown == 'down' else 0xb00, # flags
            0, # timestamp
            0, # window
            0, # ctx
            8, # subtype
            (key_code << 16) | ((0xa if upDown == 'down' else 0xb) << 8), # data1
            -1 # data2
        )

    Quartz.CGEventPost(0, ev.CGEvent())









def _position():
    loc = AppKit.NSEvent.mouseLocation()
    return int(loc.x), int(Quartz.CGDisplayPixelsHigh(0) - loc.y)


def _size():
    return Quartz.CGDisplayPixelsWide(Quartz.CGMainDisplayID()), Quartz.CGDisplayPixelsHigh(Quartz.CGMainDisplayID())



def _scroll(clicks, x=None, y=None):
    _vscroll(clicks, x, y)


"""
According to https://developer.apple.com/library/mac/documentation/Carbon/Reference/QuartzEventServicesRef/Reference/reference.html#//apple_ref/c/func/Quartz.CGEventCreateScrollWheelEvent
"Scrolling movement is generally represented by small signed integer values, typically in a range from -10 to +10. Large values may have unexpected results, depending on the application that processes the event."
The scrolling functions will create multiple events that scroll 10 each, and then scroll the remainder.
"""

def _vscroll(clicks, x=None, y=None):
    _moveTo(x, y)
    clicks = int(clicks)
    for _ in range(abs(clicks) // 10):
        scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
            None, # no source
            Quartz.kCGScrollEventUnitLine, # units
            1, # wheelCount (number of dimensions)
            10 if clicks >= 0 else -10) # vertical movement
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

    scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
        None, # no source
        Quartz.kCGScrollEventUnitLine, # units
        1, # wheelCount (number of dimensions)
        clicks % 10 if clicks >= 0 else -1 * (-clicks % 10)) # vertical movement
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)


def _hscroll(clicks, x=None, y=None):
    _moveTo(x, y)
    clicks = int(clicks)
    for _ in range(abs(clicks) // 10):
        scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
            None, # no source
            Quartz.kCGScrollEventUnitLine, # units
            2, # wheelCount (number of dimensions)
            0, # vertical movement
            10 if clicks >= 0 else -10) # horizontal movement
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

    scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
        None, # no source
        Quartz.kCGScrollEventUnitLine, # units
        2, # wheelCount (number of dimensions)
        0, # vertical movement
        (clicks % 10) if clicks >= 0 else (-1 * clicks % 10)) # horizontal movement
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)


def _mouseDown(x, y, button):
    if button == LEFT:
        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
    elif button == MIDDLE:
        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
    elif button == RIGHT:
        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _mouseUp(x, y, button):
    if button == LEFT:
        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
    elif button == MIDDLE:
        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
    elif button == RIGHT:
        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _click(x, y, button):
    if button == LEFT:
        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
    elif button == MIDDLE:
        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
    elif button == RIGHT:
        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"

def _multiClick(x, y, button, num, interval=0.0):
    btn    = None
    down   = None
    up     = None

    if button == LEFT:
        btn  = Quartz.kCGMouseButtonLeft
        down = Quartz.kCGEventLeftMouseDown
        up   = Quartz.kCGEventLeftMouseUp
    elif button == MIDDLE:
        btn  = Quartz.kCGMouseButtonCenter
        down = Quartz.kCGEventOtherMouseDown
        up   = Quartz.kCGEventOtherMouseUp
    elif button == RIGHT:
        btn  = Quartz.kCGMouseButtonRight
        down = Quartz.kCGEventRightMouseDown
        up   = Quartz.kCGEventRightMouseUp
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"
        return

    for i in range(num):
        _click(x, y, button)
        time.sleep(interval)


def _sendMouseEvent(ev, x, y, button):
    mouseEvent = Quartz.CGEventCreateMouseEvent(None, ev, (x, y), button)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseEvent)


def _dragTo(x, y, button):
    if button == LEFT:
        _sendMouseEvent(Quartz.kCGEventLeftMouseDragged , x, y, Quartz.kCGMouseButtonLeft)
    elif button == MIDDLE:
        _sendMouseEvent(Quartz.kCGEventOtherMouseDragged , x, y, Quartz.kCGMouseButtonCenter)
    elif button == RIGHT:
        _sendMouseEvent(Quartz.kCGEventRightMouseDragged , x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"
    time.sleep(pyautogui.DARWIN_CATCH_UP_TIME) # needed to allow OS time to catch up.

def _moveTo(x, y):
    _sendMouseEvent(Quartz.kCGEventMouseMoved, x, y, 0)
    time.sleep(pyautogui.DARWIN_CATCH_UP_TIME) # needed to allow OS time to catch up.
