# Screenshot-related features of PyAutoGUI

"""
So, apparently Pillow support on Ubuntu 64-bit has several additional steps since it doesn't have JPEG/PNG support out of the box. Description here:

https://stackoverflow.com/questions/7648200/pip-install-pil-e-tickets-1-no-jpeg-png-support
http://ubuntuforums.org/showthread.php?t=1751455
"""

import datetime
import os
import subprocess
import sys
import cv2
import numpy as np

RUNNING_PYTHON_2 = sys.version_info[0] == 2

scrotExists = False
try:
    if sys.platform not in ('java', 'darwin', 'win32'):
        whichProc = subprocess.Popen(['which', 'scrot'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        scrotExists = whichProc.wait() == 0
except:
    # if there is no "which" program to find scrot, then assume there is no scrot.
    pass


def locateAll(needleImage, haystackImage, grayscale=False, limit=None, confidence=0.999):
    """generate location(s) of needle image in haystack, confidence threshold
    """
    # code adapted from https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
    # "OpenCV uses BGR channel order by default, so be careful, e.g. when you compare an image you loaded with cv2.imread to an image you converted from PIL to numpy. You can always use cv2.cvtColor to convert between formats."
    if grayscale:
        load_fmt = cv2.CV_LOAD_IMAGE_GRAYSCALE
    else:
        load_fmt = cv2.CV_LOAD_IMAGE_COLOR

    # load images from filenames:
    if isinstance(needleImage, str):
        needleImage = cv2.imread(needleImage, load_fmt)
        needleHeight, needleWidth = needleImage.shape[:2]
    else:
        raise NotImplementedError  # TO-DO: convert to cv; see caveat about BGR conversion
    if isinstance(haystackImage, str):
        haystackImage = cv2.imread(haystackImage, load_fmt)
    else:
        raise NotImplementedError  # TO-DO: convert to cv; see caveat about BGR conversion

    result = cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
    match_indices = np.arange(result.size)[(result > confidence).flatten()]
    unraveled = np.unravel_index(match_indices, result.shape)

    for y, matchx in zip(unraveled[0], unraveled[1]):
        yield (matchx, y, needleWidth, needleHeight)


def locate(needleImage, haystackImage, grayscale=False):
    # Note: The gymnastics in this function is because we want to make sure to exhaust the iterator so that the needle and haystack files are closed in locateAll.
    points = tuple(locateAll(needleImage, haystackImage, grayscale, 1))
    if len(points) > 0:
        return points[0]
    else:
        return None


def locateOnScreen(image, grayscale=False):
    screenshotIm = screenshot()
    retVal = locate(image, screenshotIm, grayscale)
    if 'fp' in dir(screenshotIm):
        screenshotIm.fp.close() # Screenshots on Windows won't have an fp since they came from ImageGrab, not a file.
    return retVal


def locateAllOnScreen(image, grayscale=False, limit=None):
    screenshotIm = screenshot()
    retVal = locateAll(image, screenshotIm, grayscale, limit)
    if 'fp' in dir(screenshotIm):
        screenshotIm.fp.close() # Screenshots on Windows won't have an fp since they came from ImageGrab, not a file.
    return retVal


def locateCenterOnScreen(image, grayscale=False):
    return center(locateOnScreen(image, grayscale))


def _screenshot_win32(imageFilename=None):
    im = ImageGrab.grab()
    if imageFilename is not None:
        im.save(imageFilename)
    return im


def _screenshot_osx(imageFilename=None):
    if imageFilename is None:
        tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
    else:
        tmpFilename = imageFilename
    subprocess.call(['screencapture', '-x', tmpFilename])
    im = Image.open(tmpFilename)
    if imageFilename is None:
        os.unlink(tmpFilename)
    return im


def _screenshot_linux(imageFilename=None):
    if not scrotExists:
        raise NotImplementedError('"scrot" must be installed to use screenshot functions in Linux. Run: sudo apt-get install scrot')
    if imageFilename is None:
        tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
    else:
        tmpFilename = imageFilename
    if scrotExists:
        subprocess.call(['scrot', tmpFilename])
        im = Image.open(tmpFilename)
        if imageFilename is None:
            os.unlink(tmpFilename)
        return im
    else:
        raise Exception('The scrot program must be installed to take a screenshot with PyAutoGUI on Linux. Run: sudo apt-get install scrot')


def center(coords):
    return (coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2))


def pixelMatchesColor(x, y, expectedRGBColor, tolerance=0):
    r, g, b = screenshot().getpixel((x, y))
    exR, exG, exB = expectedRGBColor

    return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance)


def pixel(x, y):
    return screenshot().getpixel((x, y))


# set the screenshot() function based on the platform running this module
if sys.platform.startswith('java'):
    raise NotImplementedError('Jython is not yet supported by PyAutoGUI.')
elif sys.platform == 'darwin':
    screenshot = _screenshot_osx
elif sys.platform == 'win32':
    screenshot = _screenshot_win32
    from PIL import ImageGrab
else:
    screenshot = _screenshot_linux


grab = screenshot # for compatibility with Pillow/PIL's ImageGrab module.
