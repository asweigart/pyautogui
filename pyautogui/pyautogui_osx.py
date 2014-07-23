import time

import Quartz
import AppKit

import pyautogui.util

import sys
if sys.platform !=  'darwin':
    raise Exception('The pyautogui_osx module should only be loaded on an OS X system.')



""" Taken from events.h
/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h

The *KB dictionaries in pyautogui map a string that can be passed to keyDown(),
keyUp(), or press() into the code used for the OS-specific keyboard function.

They should always be lowercase, and the same keys should be used across all OSes."""
keyboardMapping = dict([(key, None) for key in pyautogui.util.KEYBOARD_KEYS])
keyboardMapping.update({
    'a': 0x00,
    's': 0x01,
    'd': 0x02,
    'f': 0x03,
    'h': 0x04,
    'g': 0x05,
    'z': 0x06,
    'x': 0x07,
    'c': 0x08,
    'v': 0x09,
    'b': 0x0b,
    'q': 0x0c,
    'w': 0x0d,
    'e': 0x0e,
    'r': 0x0f,
    'y': 0x10,
    't': 0x11,
    '1': 0x12,
    '2': 0x13,
    '3': 0x14,
    '4': 0x15,
    '6': 0x16,
    '5': 0x17,
    '=': 0x18,
    '9': 0x19,
    '7': 0x1a,
    '-': 0x1b,
    '8': 0x1c,
    '0': 0x1d,
    ']': 0x1e,
    'o': 0x1f,
    'u': 0x20,
    '[': 0x21,
    'i': 0x22,
    'p': 0x23,
    'l': 0x25,
    'j': 0x26,
    '\'': 0x27,
    'k': 0x28,
    ';': 0x29,
    '\\': 0x2a,
    ',': 0x2b,
    '/': 0x2c,
    'n': 0x2d,
    'm': 0x2e,
    '.': 0x2f,
    '`': 0x32,
    ' ': 0x31,
    '\r': 0x24,
    '\n': 0x24,
    'enter': 0x24,
    'return': 0x24,
    '\t': 0x30,
    'tab': 0x30,
    'shift': 0x38
})

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
    if key in special_key_translate_table:
        _specialKeyEvent(key, 'down')
    else:
        _normalKeyEvent(key, 'down')

def _keyUp(key):
    if key in special_key_translate_table:
        _specialKeyEvent(key, 'up')
    else:
        _normalKeyEvent(key, 'up')


def _normalKeyEvent(key, upDown):
    assert upDown in ('up', 'down'), "upDown argument must be 'up' or 'down'"

    try:
        if pyautogui.util.isShiftCharacter(key):
            key_code = keyboardMapping[key.lower()]

            event = Quartz.CGEventCreateKeyboardEvent(None,
                        keyboardMapping['shift'], upDown == 'down')
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            # Tiny sleep to let OS X catch up on us pressing shift
            time.sleep(.01) # TODO - test to see if this is needed.

        else:
            key_code = keyboardMapping[key]

        event = Quartz.CGEventCreateKeyboardEvent(None, key_code, upDown == 'down')
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

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
    return Quartz.CGDisplayPixelsWide(0), Quartz.CGDisplayPixelsHigh(0)



def _scroll(clicks, x=None, y=None):
    _vscroll(clicks, x, y)


"""
According to https://developer.apple.com/library/mac/documentation/Carbon/Reference/QuartzEventServicesRef/Reference/reference.html#//apple_ref/c/func/Quartz.CGEventCreateScrollWheelEvent
"Scrolling movement is generally represented by small signed integer values, typically in a range from -10 to +10. Large values may have unexpected results, depending on the application that processes the event."
The scrolling functions will create multiple events that scroll 10 each, and then scroll the remainder.
"""

def _vscroll(clicks, x=None, y=None):
    moveTo(x, y)
    clicks = int(clicks)
    for _ in range(abs(clicks) // 10):
        scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
            None, Quartz.kCGScrollEventUnitLine, 1,
            10 if clicks >= 0 else -10)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

    scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
        None, Quartz.kCGScrollEventUnitLine, 1,
        (clicks % 10) if clicks >= 0 else (-1 * clicks % 10))
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)


def _hscroll(clicks, x=None, y=None):
    moveTo(x, y)
    clicks = int(clicks)
    for _ in range(abs(clicks) // 10):
        scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
            None, Quartz.kCGScrollEventUnitLine, 2,
            None,
            10 if clicks >= 0 else -10)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

    scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
        None, Quartz.kCGScrollEventUnitLine, 2,
        None,
        (clicks % 10) if clicks >= 0 else (-1 * clicks % 10))
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)


def _mouseDown(button, x, y):
    if button == 'left':
        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
    elif button == 'middle':
        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
    elif button == 'right':
        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _mouseUp(button, x, y):
    if button == 'left':
        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
    elif button == 'middle':
        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
    elif button == 'right':
        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _click(button, x, y):
    if button == 'left':
        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
    elif button == 'middle':
        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
    elif button == 'right':
        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _sendMouseEvent(ev, x, y, button):
    mouseEvent = Quartz.CGEventCreateMouseEvent(None, ev, (x, y), button)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseEvent)


def _dragTo(x, y, button):
    if button == 'left':
        _sendMouseEvent(Quartz.kCGEventLeftMouseDragged , x, y, Quartz.kCGMouseButtonLeft)
    elif button == 'middle':
        _sendMouseEvent(Quartz.kCGEventOtherMouseDragged , x, y, Quartz.kCGMouseButtonCenter)
    elif button == 'right':
        _sendMouseEvent(Quartz.kCGEventRightMouseDragged , x, y, Quartz.kCGMouseButtonRight)
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


def _moveTo(x, y):
    _sendMouseEvent(Quartz.kCGEventMouseMoved, x, y, 0)
