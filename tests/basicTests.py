import unittest
import sys
import os
import time
import threading
sys.path.append(os.path.abspath('..'))
import pyautogui

class TestGeneral(unittest.TestCase):
    def test_accessibleNames(self):
        # This is a platform-specific test, you need to run this file on Win/OSX/Linux for full code coverage.

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

    def test_size(self):
        width, height = pyautogui.size()

        self.assertTrue(type(width) == int)
        self.assertTrue(type(height) == int)
        self.assertTrue(width > 0)
        self.assertTrue(height > 0)

    def test_position(self):
        mousex, mousey = pyautogui.position()

        self.assertTrue(type(mousex) == int)
        self.assertTrue(type(mousey) == int)

    def test_onScreen(self):
        width, height = pyautogui.size()
        halfWidth = int(width / 2)
        halfHeight = int(height / 2)

        self.assertTrue(pyautogui.onScreen(0, 0))
        self.assertTrue(pyautogui.onScreen([0, 0]))

        self.assertTrue(pyautogui.onScreen(halfWidth, 0))
        self.assertTrue(pyautogui.onScreen([halfWidth, 0]))
        self.assertTrue(pyautogui.onScreen(0, halfHeight))
        self.assertTrue(pyautogui.onScreen([0, halfHeight]))
        self.assertTrue(pyautogui.onScreen(halfWidth, halfHeight))
        self.assertTrue(pyautogui.onScreen([halfWidth, halfHeight]))

        self.assertFalse(pyautogui.onScreen(-1, 0))
        self.assertFalse(pyautogui.onScreen([-1, 0]))
        self.assertFalse(pyautogui.onScreen(-1, -1))
        self.assertFalse(pyautogui.onScreen([-1, -1]))
        self.assertFalse(pyautogui.onScreen(0, -1))
        self.assertFalse(pyautogui.onScreen([0, -1]))

        self.assertFalse(pyautogui.onScreen(width, 0))
        self.assertFalse(pyautogui.onScreen([width, 0]))
        self.assertFalse(pyautogui.onScreen(0, height))
        self.assertFalse(pyautogui.onScreen([0, height]))
        self.assertFalse(pyautogui.onScreen(width, height))
        self.assertFalse(pyautogui.onScreen([width, height]))


class TestMouse(unittest.TestCase):
    def test_moveTo(self):
        # NOTE - The user moving the mouse during this test will cause it to fail.

        # moving the mouse
        pyautogui.moveTo(1, 1)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))

        # no coordinate specified (should be a NO-OP)
        pyautogui.moveTo(None, None)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))

        # moving the mouse to a new location
        pyautogui.moveTo(2, 2)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (2, 2))

        # moving the mouse over time (1/5 second)
        pyautogui.moveTo(1, 1, 0.2)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))

        # moving the mouse with only x specified
        pyautogui.moveTo(5, None)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (5, 1))

        # ...and only y specified
        pyautogui.moveTo(None, 5)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (5, 5))

    def test_moveRel(self):
        # NOTE - The user moving the mouse during this test will cause it to fail.

        # start at 1,1
        pyautogui.moveTo(1, 1)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))

        # move down and right
        pyautogui.moveRel(4, 4)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (5, 5))

        # move up and left
        pyautogui.moveRel(-4, -4)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))

        # move right
        pyautogui.moveRel(4, None)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (5, 1))

        # move down
        pyautogui.moveRel(None, 4)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (5, 5))

        # move left
        pyautogui.moveRel(-4, None)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 5))

        # move up
        pyautogui.moveRel(None, -4)
        mousepos = pyautogui.position()
        self.assertTrue(mousepos == (1, 1))


class TypewriteThread(threading.Thread):
    def __init__(self, msg, interval=0.0):
        self.msg = msg
        self.interval = interval
        super(TypewriteThread, self).__init__()

    def run(self):
        time.sleep(0.25)
        pyautogui.typewrite(self.msg, self.interval)


class TestKeyboard(unittest.TestCase):
    # NOTE: The terminal window running this script must be in focus during the keyboard tests.
    # You cannot run this as a scheduled task or remotely.
    def test_typewrite(self):
        # 'Hello world!\n' test
        t = TypewriteThread('Hello world!\n')
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'Hello world!')

        # 'Hello world!\n' as a list argument
        t = TypewriteThread(list('Hello world!\n'))
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'Hello world!')

        # All printable ASCII characters test
        allKeys = []
        for c in range(32, 127):
            allKeys.append(chr(c))
        allKeys = ''.join(allKeys)

        t = TypewriteThread(allKeys + '\n')
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, allKeys)

    def test_typewrite_slow(self):
        t = TypewriteThread('Hello world!\n', 0.1)
        startTime = time.time()
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'Hello world!')
        self.assertTrue(time.time() > startTime + 1.2)

    def test_typewrite_editable(self):
        # Backspace test
        t = TypewriteThread(['a', 'b', 'c', '\b', 'backspace', 'x', 'y', 'z', '\n'])
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'axyz')

        # Arrow key test
        t = TypewriteThread(['a', 'b', 'c', 'left', 'left', 'right', 'x', '\n'])
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'abxc')

        # Del key test
        t = TypewriteThread(['a', 'b', 'c', 'left', 'left','left', 'del', 'delete', '\n'])
        t.start()
        if sys.version_info[0] == 2:
            response = raw_input()
        else:
            response = input()
        self.assertEqual(response, 'c')



if __name__ == '__main__':
    unittest.main()
