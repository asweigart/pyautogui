Screenshots
===========

TODO - finish these docs

Screenshot functionality requires PIL/Pillow

OS X uses "screencapture" command (comes with OS X). Linux requires 'scrot' to be installed.

    screenshot() - Returns a PIL Image object of a screenshot.

    screenshot(filename) - Returns a PIL Image object of a screenshot, but also saves it to a file.

    locateOnScreen(image) - Returns (x, y) coordinate of first found instance of the image on the screen. 'image' can be a string of an image filename or a PIL Image object. Returns None if not found on the screen.

    locateAllOnScreen(image) - Returns an iterator the returns (x, y) coordinates.

    locate(needle_image, haystack_image) - Returns (x, y) coordinate of first found instance of the needle_image on the haystack_image. Arguments can be a string of an image filename or a PIL Image object. Returns None if not found on the screen.

    locateAll(needle_image, haystack_image) - Returns an iterator the returns (x, y) coordinates.
