# Screenshot-related features of PyAutoGUI

# UNDER CONSTRUCTION

import datetime
import os
import subprocess
import sys
from PIL import Image

whichProc = subprocess.Popen(['which', 'scrot'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
scrotExists = whichProc.wait() == 0

"""
Screencapture features (requires PIL/Pillow)
 - locate(image_filename, region=(x, y, width, height)) # returns the center (x, y) of the image found on a current screenshot
 - locateAll(image_filename, region=(x, y, width, height))  # returns a list of (centerx, centery)
 - screenshot()   # returns Image object
 - screenshot(image_filename) # saves the screenshot to a file, returns Image object
"""

#imageFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))

def screenshot_win32(imageFilename=None):
    from PIL import ImageGrab
    im = ImageGrab.grab()
    if imageFilename is not None:
        im.save(imageFilename)
    return im


def screenshot_osx(imageFilename=None):
    if imageFilename is None:
        tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
    else:
        tmpFilename = imageFilename
    subprocess.call(['screencapture', tmpFilename])
    im = Image.open(tmpFilename)
    if imageFilename is None:
        os.unlink(tmpFilename)
    return im


def screenshot_linux(imageFilename=None):
    if imageFilename is None:
        tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
    else:
        tmpFilename = imageFilename
    if scrotExists:
        proc = subprocess.call(['scrot', tmpFilename])
        proc.wait()
        im = Image.open(tmpFilename)
        if imageFilename is None:
            os.unlink(tmpFilename)
        return im
    else:
        raise Exception('The scrot program must be installed to take a screenshot with PyAutoGUI on Linux. Run: sudo apt-get install scrot')



def kmp(haystack, needle): # Knuth-Morris-Pratt search algorithm implementation (to be used by screen capture)
    # build table of shift amounts
    shifts = [1] * (len(needle) + 1)
    shift = 1
    for pos in range(len(needle)):
        while shift <= pos and needle[pos] != needle[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in haystack:
        while matchLen == len(needle) or \
              matchLen >= 0 and needle[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(needle):
            yield startPos


