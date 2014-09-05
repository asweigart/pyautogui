.. default-role:: code

=======
Testing
=======

The unit tests for PyAutoGUI are currently not comprehensive. The tests (in basicTests.py) cover the following:

- onScreen()
- size()
- position()
- moveTo()
- moveRel()
- typewrite()
- PAUSE

Platforms Tested
================

- Python 3.4, 3.3, 3.2, 3.1, 2.7, 2.6, 2.5
- Windows
- OS X
- Raspberry Pi

(If you have run the unit tests successfully on other platforms, please tell al@inventwithpython.com.)

PyAutoGUI is not compatible with Python 2.4 or before.

The keyboard functions do not work on Ubuntu when run in VirtualBox on Windows.
