# Screenshot-related features of PyAutoGUI

# UNDER CONSTRUCTION

"""
Screencapture features (requires PIL/Pillow)
 - locate(image_filename, region=(x, y, width, height)) # returns the center (x, y) of the image found on a current screenshot
 - locateAll(image_filename, region=(x, y, width, height))  # returns a list of (centerx, centery)
 - screenshot()   # returns PIL object (provides cross-platform interface for getting screenshots, since PIL only support screen grabs on Windows.)
 - screenshot(image_filename) # saves the screenshot to a file
"""

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
