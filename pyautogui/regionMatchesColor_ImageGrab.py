mport cv2
import numpy
from PIL import ImageGrab


class ModelException(Exception):
    """
    PyAutoGUI code will raise this exception class for any invalid actions. If PyAutoGUI raises some other exception,
    you should assume that this is caused by a bug in PyAutoGUI itself. (Including a failure to catch potential
    exceptions raised by PyAutoGUI.)
    """
    pass

def regionMatchesColor(region, expectedRGBColor, tolerance=0, model=0):
    region = list(region)
    region[2] += region[0]
    region[3] += region[1]
    im = numpy.array(ImageGrab.grab(bbox=region))
    # print(ImageGrab.grab(bbox=region))
    low = numpy.array([item - tolerance for item in list(expectedRGBColor)])
    high = numpy.array([item + tolerance for item in list(expectedRGBColor)])
    dst = cv2.inRange(src=im, lowerb=low, upperb=high)
    position = numpy.column_stack(numpy.where(dst == 255))
    if len(position) > 0:
        if model == 0:
            return int(position[0][1]) + region[0], int(position[0][0]) + region[1]
        elif model == 1:
            return int(position[int(len(position) / 2)][1]) + region[0], int(position[int(len(position) / 2)][0]) + \
                   region[1]
        elif model == 2:
            return int(position[-1][1]) + region[0], int(position[-1][0]) + region[1]
        else:
            raise ModelException("Value of model should be one of 0,1,2")
    else:
        return None
