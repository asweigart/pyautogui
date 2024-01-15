import pyautogui
import time
import pymsgbox

for i in range(5):
    pyautogui.moveTo(220, 200 + 5 * i)
    #pyautogui.displayMousePosition()
    #time.sleep(1)
    pymsgbox.alert(text='Wanna move on?', title='WAIT', button='Gotta move on')