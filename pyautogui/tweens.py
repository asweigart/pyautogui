import math


# from http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python
def getLine(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def linearTween(n):
    return n

def easeInQuad(n):
    return n**2;

def easeOutQuad(n):
    return -n * (n-2)

def easeInOutQuad(n):
    if n < 0.5:
        return 2 * n**2
    else:
        n = n * 2 - 1
        return -0.5 * (n*(n-2) - 1)

def easeInCubic(n):
    return n**3

def easeOutCubic(n):
    n = n - 1
    return n**3 + 1

def easeInOutCubic(n):
    n = 2 * n
    if n < 1:
        return 0.5 * n**3
    else:
        n = n - 2
        return 0.5 * (n**3 + 2)

def easeInQuart(n):
    return n**4

def easeOutQuart(n):
    n = n - 1
    return -(n**4 - 1)

def easeInOutQuart(n):
    n = 2 * n
    if n < 1:
        return 0.5 * n**4
    else:
        n = n - 2
        return -0.5 * (n**4 - 2)

def easeInQuint(n):
    return n**5

def easeOutQuint(n):
    n = n - 1
    return n**5 + 1

def easeInOutQuint(n):
    n = 2 * n
    if n < 1:
        return 0.5 * n**5
    else:
        n = n - 2
        return 0.5 * (n**5 + 2)



# dev note - b will always be 0.0, c and d will always be 1.0, their t is my n

def easeInSine(n):
    return -1 * math.cos(n * math.pi / 2) + 1

def easeOutSine(n):
    return math.sin(n * math.pi / 2)

def easeInOutSine(n):
    return -0.5 * (math.cos(math.pi * n) - 1)

def easeInExpo(n):
    if n == 0:
        return 0
    else:
        return 2**(10 * (n - 1))

def easeOutExpo(n):
    if n == 1:
        return 1
    else:
        return -(2 ** (-10 * n)) + 1

def easeInOutExpo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = n * 2
        if n < 1:
            return 0.5 * 2**(10 * (n - 1))
        else:
            return 0.5 * -(2 ** (-10 * (n - 2)) + 2)

def easeInCirc(n):
    return -1 * math.sqrt(1 - n**2)

def easeOutCirc(n):
    return math.sqrt(1 - (n - 1))

def easeInOutCirc(n):
    n = n * 2
    if n < 1:
        return -0.5 * (math.sqrt(1 - n**2) - 1)
    else:
        n = n - 2
        return 0.5 * (math.sqrt(1 - n**2) + 1)


# TODO - currently doesn't work because it can return something above 1.0
def easeInElastic(n, amplitude=None, period=None):
    if period is None:
        period = 0.5

    if amplitude is None:
        amplitude = 1

    if amplitude < 1:
        s = period / 4
    else:
        s = period / (2 * math.pi) * math.asin(1 / amplitude)

    return amplitude * 2**(-10*n) * math.sin( (n-s)*(2*math.pi) / period) + 1


