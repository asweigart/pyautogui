import pyautogui as driver

def complete():
    xScreen, yScreen = driver.size()
    return (0, 0, xScreen, yScreen)

def halfTop ():
    xScreen, yScreen = driver.size()
    return (0, 0, xScreen, yScreen/2)
    
def halfBottom ():
    xScreen, yScreen = driver.size()
    return (0, yScreen/2, xScreen, yScreen/2)

def halfLeft():
    xScreen, yScreen = driver.size()
    return (0, 0, xScreen/2, yScreen)

def halfRight():
    xScreen, yScreen = driver.size()
    return (xScreen/2, 0, xScreen/2, yScreen)
    
def topLeft():
    xScreen, yScreen = driver.size()
    return (0, 0, xScreen/2, yScreen/2)

def topRight():
    xScreen, yScreen = driver.size()
    return (xScreen/2, 0, xScreen/2, yScreen/2)

def bottomLeft():
    xScreen, yScreen = driver.size()
    return (0, yScreen/2, xScreen/2, yScreen/2)

def bottomRight():
    xScreen, yScreen = driver.size()
    return (xScreen/2, yScreen/2, xScreen/2, yScreen/2)
