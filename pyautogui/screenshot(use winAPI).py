import numpy
import win32gui
import win32ui
import win32con


class ModelException(Exception):
    """
    PyAutoGUI code will raise this exception class for any invalid actions. If PyAutoGUI raises some other exception,
    you should assume that this is caused by a bug in PyAutoGUI itself. (Including a failure to catch potential
    exceptions raised by PyAutoGUI.)
    """
    pass

# winAPI screenshot
def screenshot(region):
    hdesktop = win32gui.GetDesktopWindow()
    width = region[2]
    height = region[3]
    lefttop_x = -region[0]
    lefttop_y = -region[1]
    rightbottom_x = width + region[0]
    rightbottom_y = height + region[1]
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((lefttop_x, lefttop_y), (rightbottom_x, rightbottom_y), img_dc, (0, 0), win32con.SRCCOPY)
    signedIntsArray = screenshot.GetBitmapBits(True)
    # img = numpy.fromstring(signedIntsArray, dtype='uint8')
    img = numpy.frombuffer(signedIntsArray, dtype='uint8')
    # img = numpy.array(signedIntsArray).astype(dtype="uint8") # This is REALLY slow!
    img.shape = (height, width, 4)    # RGB+Alpha
    img = numpy.delete(img, 3, axis=2)
    return img
