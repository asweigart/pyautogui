from __future__ import division, print_function

import unittest
import sys
import os
import time
import threading
from collections import namedtuple  # Added in Python 2.6.
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyautogui

runningOnPython2 = sys.version_info[0] == 2

if runningOnPython2:
    INPUT_FUNC = raw_input
else:
    INPUT_FUNC = input

# TODO - note that currently most of the click-related functionality is not tested.


class P(namedtuple('P', ['x', 'y'])):
    '''Simple, immutable, 2D point/vector class, including some basic
    arithmetic functions.
    '''
    def __str__(self):
        return '{0},{1}'.format(self.x, self.y)

    def __repr__(self):
        return 'P({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return P(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return P(self.x // other, self.y // other)

    def __truediv__(self, other):
        return P(self.x / other, self.y / other)

    def __neg__(self):
        return P(-self.x, -self.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return P(abs(self.x), abs(self.y))


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(42, 42) # make sure failsafe isn't triggered during this test
        pyautogui.FAILSAFE = True


    def tearDown(self):
        pyautogui.FAILSAFE = self.oldFailsafeSetting


    def test_accessibleNames(self):
        # Check that all the functions are defined.

        # mouse-related API
        pyautogui.moveTo
        pyautogui.moveRel
        pyautogui.dragTo
        pyautogui.dragRel
        pyautogui.mouseDown
        pyautogui.mouseUp
        pyautogui.click
        pyautogui.rightClick
        pyautogui.doubleClick
        pyautogui.tripleClick

        # keyboard-related API
        pyautogui.typewrite
        pyautogui.hotkey
        pyautogui.keyDown
        pyautogui.keyUp
        pyautogui.press

        # The functions implemented in the platform-specific modules should also show up in the pyautogui namespace:
        pyautogui.position
        pyautogui.size
        pyautogui.scroll
        pyautogui.hscroll
        pyautogui.vscroll

        # util API
        pyautogui.KEYBOARD_KEYS
        pyautogui.isShiftCharacter

        # Screenshot-related API
        pyautogui.locateAll
        pyautogui.locate
        pyautogui.locateOnScreen
        pyautogui.locateAllOnScreen
        pyautogui.locateCenterOnScreen
        pyautogui.center
        pyautogui.pixelMatchesColor
        pyautogui.pixel
        pyautogui.screenshot
        pyautogui.grab

        # TODO(denilsonsa): I believe we should get rid of these symbols. If someone wants tweening, import pytweening module instead!
        # Tweening-related API
        pyautogui.getPointOnLine
        pyautogui.linear
        pyautogui.easeInQuad
        pyautogui.easeOutQuad
        pyautogui.easeInOutQuad
        pyautogui.easeInCubic
        pyautogui.easeOutCubic
        pyautogui.easeInOutCubic
        pyautogui.easeInQuart
        pyautogui.easeOutQuart
        pyautogui.easeInOutQuart
        pyautogui.easeInQuint
        pyautogui.easeOutQuint
        pyautogui.easeInOutQuint
        pyautogui.easeInSine
        pyautogui.easeOutSine
        pyautogui.easeInOutSine
        pyautogui.easeInExpo
        pyautogui.easeOutExpo
        pyautogui.easeInOutExpo
        pyautogui.easeInCirc
        pyautogui.easeOutCirc
        pyautogui.easeInOutCirc
        pyautogui.easeInElastic
        pyautogui.easeOutElastic
        pyautogui.easeInOutElastic
        pyautogui.easeInBack
        pyautogui.easeOutBack
        pyautogui.easeInOutBack
        pyautogui.easeInBounce
        pyautogui.easeOutBounce
        pyautogui.easeInOutBounce


    def test_size(self):
        width, height = pyautogui.size()

        self.assertTrue(isinstance(width, int), 'Type of width is %s' % (type(width)))
        self.assertTrue(isinstance(height, int), 'Type of height is %s' % (type(height)))
        self.assertTrue(width > 0, 'Width is set to %s' % (width))
        self.assertTrue(height > 0, 'Height is set to %s' % (height))


    def test_position(self):
        mousex, mousey = pyautogui.position()

        if (runningOnPython2 and sys.version_info[2] not in (6, 7)) and sys.platform != 'darwin':
            # Python 2 on OS X returns int.
            self.assertTrue(isinstance(mousex, long), 'Type of mousex is %s' % (type(mousex)))
            self.assertTrue(isinstance(mousey, long), 'Type of mousey is %s' % (type(mousey)))
        else:
            self.assertTrue(isinstance(mousex, int), 'Type of mousex is %s' % (type(mousex)))
            self.assertTrue(isinstance(mousey, int), 'Type of mousey is %s' % (type(mousey)))

        # Test passing x and y arguments to position().
        pyautogui.moveTo(mousex + 1, mousey + 1)
        x, y = pyautogui.position(mousex, None)
        self.assertEqual(x, mousex)
        self.assertNotEqual(y, mousey)

        x, y = pyautogui.position(None, mousey)
        self.assertNotEqual(x, mousex)
        self.assertEqual(y, mousey)


    def test_onScreen(self):
        zero = P(0, 0)
        xone = P(1, 0)
        yone = P(0, 1)
        size = P(*pyautogui.size())
        half = size / 2

        on_screen = [
            zero,
            zero + xone,
            zero + yone,
            zero + xone + yone,
            half,
            size - xone - yone,
        ]
        off_screen = [
            zero - xone,
            zero - yone,
            zero - xone - yone,
            size - xone,
            size - yone,
            size,
        ]

        for value, coords in [(True, on_screen), (False, off_screen)]:
            for coord in coords:
                self.assertEqual(value, pyautogui.onScreen(*coord), 'onScreen({0}, {1}) should be {2}'.format(coord.x, coord.y, value))
                self.assertEqual(value, pyautogui.onScreen(list(coord)), 'onScreen([{0}, {1}]) should be {2}'.format(coord.x, coord.y, value))
                self.assertEqual(value, pyautogui.onScreen(tuple(coord)), 'onScreen(({0}, {1})) should be {2}'.format(coord.x, coord.y, value))
                self.assertEqual(value, pyautogui.onScreen(coord), 'onScreen({0}) should be {1}'.format(repr(coord), value))

        # These can raise either ValueError or TypeError.
        with self.assertRaises(ValueError):
            pyautogui.onScreen([0, 0], 0)
        with self.assertRaises(ValueError):
            pyautogui.onScreen((0, 0), 0)
        with self.assertRaises(TypeError):
            pyautogui.onScreen(0, 0, 0)
        with self.assertRaises(TypeError):
            pyautogui.onScreen(0)

    def test_pause(self):
        oldValue = pyautogui.PAUSE

        startTime = time.time()
        pyautogui.PAUSE = 0.35 # there should be a 0.35 second pause after each call
        pyautogui.moveTo(1, 1)
        pyautogui.moveRel(0,1)
        pyautogui.moveTo(1, 1)

        elapsed = time.time() - startTime
        self.assertTrue(1.0 < elapsed <  1.1, 'Took %s seconds, expected 1.0 < 1.1 seconds.' % (elapsed))

        pyautogui.PAUSE = oldValue # restore the old PAUSE value


class TestMouse(unittest.TestCase):
    # NOTE - The user moving the mouse during many of these tests will cause them to fail.

    # There is no need to test all tweening functions.
    TWEENS = [
        'linear',
        'easeInElastic',
        'easeOutElastic',
        'easeInOutElastic',
        'easeInBack',
        'easeOutBack',
        'easeInOutBack',
    ]

    def setUp(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        self.center = P(*pyautogui.size()) // 2

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(*self.center) # make sure failsafe isn't triggered during this test
        pyautogui.FAILSAFE = True

    def tearDown(self):
        pyautogui.FAILSAFE = self.oldFailsafeSetting

    def test_moveTo(self):
        # moving the mouse
        desired = self.center
        pyautogui.moveTo(*desired)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # no coordinate specified (should be a NO-OP)
        pyautogui.moveTo(None, None)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # moving the mouse to a new location
        desired += P(42, 42)
        pyautogui.moveTo(*desired)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # moving the mouse over time (1/5 second)
        desired -= P(42, 42)
        pyautogui.moveTo(desired.x, desired.y, duration=0.2)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # moving the mouse with only x specified
        desired -= P(42, 0)
        pyautogui.moveTo(desired.x, None)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # ...and only y specified
        desired -= P(0, 42)
        pyautogui.moveTo(None, desired.y)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a list instead of separate x and y.
        desired += P(42, 42)
        pyautogui.moveTo(list(desired))
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a tuple instead of separate x and y.
        desired += P(42, 42)
        pyautogui.moveTo(tuple(desired))
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a sequence-like object instead of separate x and y.
        desired -= P(42, 42)
        pyautogui.moveTo(desired)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

    def test_moveToWithTween(self):
        origin = self.center - P(100, 100)
        destination = self.center + P(100, 100)

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            resetMouse()
            pyautogui.moveTo(destination.x, destination.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, destination, '%s tween move failed. mousepos set to %s instead of %s' % (tweenName, mousepos, destination))

    def test_moveRel(self):
        # start at the center
        desired = self.center
        pyautogui.moveTo(*desired)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move down and right
        desired += P(42, 42)
        pyautogui.moveRel(42, 42)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move up and left
        desired -= P(42, 42)
        pyautogui.moveRel(-42, -42)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move right
        desired += P(42, 0)
        pyautogui.moveRel(42, None)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move down
        desired += P(0, 42)
        pyautogui.moveRel(None, 42)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move left
        desired += P(-42, 0)
        pyautogui.moveRel(-42, None)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # move up
        desired += P(0, -42)
        pyautogui.moveRel(None, -42)
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a list instead of separate x and y.
        desired += P(42, 42)
        pyautogui.moveRel([42, 42])
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a tuple instead of separate x and y.
        desired -= P(42, 42)
        pyautogui.moveRel((-42, -42))
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

        # Passing a sequence-like object instead of separate x and y.
        desired += P(42, 42)
        pyautogui.moveRel(P(42, 42))
        mousepos = P(*pyautogui.position())
        self.assertEqual(mousepos, desired)

    def test_moveRelWithTween(self):
        origin = self.center - P(100, 100)
        delta = P(200, 200)
        destination = origin + delta

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            resetMouse()
            pyautogui.moveRel(delta.x, delta.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, destination, '%s tween move failed. mousepos set to %s instead of %s' % (tweenName, mousepos, destination))

    def test_scroll(self):
        # TODO - currently this just checks that scrolling doesn't result in an error.
        pyautogui.scroll(1)
        pyautogui.scroll(-1)
        pyautogui.hscroll(1)
        pyautogui.hscroll(-1)
        pyautogui.vscroll(1)
        pyautogui.vscroll(-1)


class TypewriteThread(threading.Thread):
    def __init__(self, msg, interval=0.0):
        super(TypewriteThread, self).__init__()
        self.msg = msg
        self.interval = interval


    def run(self):
        time.sleep(0.25) # NOTE: BE SURE TO ACCOUNT FOR THIS QUARTER SECOND FOR TIMING TESTS!
        pyautogui.typewrite(self.msg, self.interval)


class PressThread(threading.Thread):
    def __init__(self, keysArg):
        super(PressThread, self).__init__()
        self.keysArg = keysArg


    def run(self):
        time.sleep(0.25) # NOTE: BE SURE TO ACCOUNT FOR THIS QUARTER SECOND FOR TIMING TESTS!
        pyautogui.press(self.keysArg)


class TestKeyboard(unittest.TestCase):
    # NOTE: The terminal window running this script must be in focus during the keyboard tests.
    # You cannot run this as a scheduled task or remotely.

    def setUp(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(42, 42) # make sure failsafe isn't triggered during this test
        pyautogui.FAILSAFE = True


    def tearDown(self):
        pyautogui.FAILSAFE = self.oldFailsafeSetting


    def test_typewrite(self):
        # 'Hello world!\n' test
        t = TypewriteThread('Hello world!\n')
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'Hello world!')

        # 'Hello world!\n' as a list argument
        t = TypewriteThread(list('Hello world!\n'))
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'Hello world!')

        # All printable ASCII characters test
        allKeys = []
        for c in range(32, 127):
            allKeys.append(chr(c))
        allKeys = ''.join(allKeys)

        t = TypewriteThread(allKeys + '\n')
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, allKeys)


    def checkForValidCharacters(self, msg):
        for c in msg:
            self.assertTrue(pyautogui.isValidKey(c), '"%c" is not a valid key on platform %s' % (c, sys.platform))


    def test_typewrite_slow(self):

        # Test out the interval parameter to make sure it adds pauses.
        t = TypewriteThread('Hello world!\n', 0.1)
        startTime = time.time()
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'Hello world!')
        elapsed = time.time() - startTime
        self.assertTrue(1.0 < elapsed <  2.0, 'Took %s seconds, expected 1.0 < x 2.0 seconds.' % (elapsed))


    def test_typewrite_editable(self):
        # Backspace test
        t = TypewriteThread(['a', 'b', 'c', '\b', 'backspace', 'x', 'y', 'z', '\n'])
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'axyz')

        # TODO - Currently the arrow keys don't seem to work entirely correctly on OS X.
        if sys.platform != 'darwin':
            # Arrow key test
            t = TypewriteThread(['a', 'b', 'c', 'left', 'left', 'right', 'x', '\n'])
            t.start()
            response = INPUT_FUNC()
            self.assertEqual(response, 'abxc')

        # Del key test
        t = TypewriteThread(['a', 'b', 'c', 'left', 'left','left', 'del', 'delete', '\n'])
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'c')

        # Home and end key test
        t = TypewriteThread(['a', 'b', 'c', 'home', 'x','end', 'z', '\n'])
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'xabcz')


    def test_press(self):
        # '' test
        t = PressThread('enter')
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, '')

        # 'a' test, also test sending list of 1- and multi-length strings
        t = PressThread(['a', 'enter'])
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'a')

        # 'ba' test, also test sending list of 1- and multi-length strings
        t = PressThread(['a', 'left', 'b', 'enter'])
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, 'ba')


    def test_typewrite_space(self):
        # Backspace test
        t = TypewriteThread(['space', ' ', '\n']) # test both 'space' and ' '
        t.start()
        response = INPUT_FUNC()
        self.assertEqual(response, '  ')


class TestFailSafe(unittest.TestCase):
    def test_failsafe(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(42, 42) # make sure mouse is not in failsafe position to begin with

        pyautogui.FAILSAFE = True
        self.assertRaises(pyautogui.FailSafeException, pyautogui.moveTo, 0, 0)

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(0, 0)# This line should not cause the fail safe exception to be raised.

        pyautogui.FAILSAFE = self.oldFailsafeSetting


if __name__ == '__main__':
    unittest.main()
