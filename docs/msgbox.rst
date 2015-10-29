.. default-role:: code

=====================
Message Box Functions
=====================

PyAutoGUI makes use of the message box functions in PyMsgBox to provide a cross-platform, pure Python way to display JavaScript-style message boxes. There are four message box functions provided:

The alert() Function
====================

    >>> alert(text='', title='', button='OK')

Displays a simple message box with text and a single OK button. Returns the text of the button clicked on.

The confirm() Function
======================

    >>> confirm(text='', title='', buttons=['OK', 'Cancel'])

Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized. Returns the text of the button clicked on.

The prompt() Function
=====================

    >>> prompt(text='', title='' , default='')

Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or None if Cancel was clicked.

The password() Function
=======================

    >>> password(text='', title='', default='', mask='*')

Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as ``*``. Returns the text entered, or None if Cancel was clicked.

