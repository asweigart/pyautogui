
=======================
Mouse Control Functions
=======================

moveTo(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween)


moveRel(x=None, y=None, duration=0.0, tween=pyaytoguid.tweens.linearTween)

dragTo(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween, button='left')

dragRel(x=None, y=None, duration=0.0, tween=pyautogui.tweens.linearTween, button='left')

click(button='left', x=None, y=None, clicks=1, interval=0.0)

rightClick(x=None, y=None, interval=0.0)

doubleClick(button='left', x=None, y=None, interval=0.0)

mouseDown(button='left', x=None, y=None)

mouseUp(button='left', x=None, y=None)

scroll(clicks, x=None, y=None)

vscroll(clicks, x=None, y=None)

hscroll(clicks, x=None, y=None)


Valid values for PyAutoGUI's button parameters: 'left', 'right', 'middle', TODO - add info about scrolling.