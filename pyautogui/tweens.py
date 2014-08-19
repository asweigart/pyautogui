import math

def getPointOnLine(x1, y1, x2, y2, n):
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return  (x, y)

def linear(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n

linearTween = linear # kept for backwards compatibility

def easeInQuad(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**2;


def easeOutQuad(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -n * (n-2)


def easeInOutQuad(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n < 0.5:
        return 2 * n**2
    else:
        n = n * 2 - 1
        return -0.5 * (n*(n-2) - 1)


def easeInCubic(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**3


def easeOutCubic(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n**3 + 1


def easeInOutCubic(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**3
    else:
        n = n - 2
        return 0.5 * (n**3 + 2)


def easeInQuart(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**4


def easeOutQuart(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return -(n**4 - 1)


def easeInOutQuart(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**4
    else:
        n = n - 2
        return -0.5 * (n**4 - 2)


def easeInQuint(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**5


def easeOutQuint(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n**5 + 1


def easeInOutQuint(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**5
    else:
        n = n - 2
        return 0.5 * (n**5 + 2)


def easeInSine(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -1 * math.cos(n * math.pi / 2) + 1


def easeOutSine(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return math.sin(n * math.pi / 2)


def easeInOutSine(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -0.5 * (math.cos(math.pi * n) - 1)


def easeInExpo(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n == 0:
        return 0
    else:
        return 2**(10 * (n - 1))


def easeOutExpo(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n == 1:
        return 1
    else:
        return -(2 ** (-10 * n)) + 1


def easeInOutExpo(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = n * 2
        if n < 1:
            return 0.5 * 2**(10 * (n - 1))
        else:
            n -= 1
            # 0.5 * (-() + 2)
            return 0.5 * (-1 * (2 ** (-10 * n)) + 2)


def easeInCirc(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -1 * (math.sqrt(1 - n * n) - 1)


def easeOutCirc(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n -= 1
    return math.sqrt(1 - (n * n))


def easeInOutCirc(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n * 2
    if n < 1:
        return -0.5 * (math.sqrt(1 - n**2) - 1)
    else:
        n = n - 2
        return 0.5 * (math.sqrt(1 - n**2) + 1)


def easeInElastic(n, amplitude=None, period=None):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if period is None:
        period = 0.3

    if amplitude is None:
        amplitude = 1

    if amplitude < 1:
        amplitude = 1
        s = period / 4
    else:
        s = period / (2 * math.pi) * math.asin(1 / amplitude)

    n -= 1
    return -1 * (amplitude * 2**(10*n) * math.sin( (n-s)*(2*math.pi) / period))


def easeOutElastic(n, amplitude=None, period=None):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')

    if period is None:
        period = 0.3

    if amplitude is None:
        amplitude = 1

    if amplitude < 1:
        amplitude = 1
        s = period / 4
    else:
        s = period / (2 * math.pi) * math.asin(1 / amplitude)

    return amplitude * 2**(-10*n) * math.sin((n-s)*(2*math.pi / period)) + 1


def easeInOutElastic(n, amplitude=None, period=None):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')

    if period is None:
        period = 0.5

    if amplitude is None:
        amplitude = 1

    if amplitude < 1:
        amplitude = 1
        s = period / 4
    else:
        s = period / (2 * math.pi) * math.asin(1 / amplitude)

    n *= 2
    if n < 1:
        n = n - 1
        return -0.5 * (amplitude * 2**(10*n) * math.sin((n - s) * 2 * math.pi / period))
    else:
        n = n - 1
        return amplitude * 2**(-10*n) * math.sin((n - s) * 2 * math.pi / period) * 0.5 + 1


def easeInBack(n, s=1.70158):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n * n * ((s + 1) * n - s)


def easeOutBack(n, s=1.70158):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n * n * ((s + 1) * n + s) + 1


def easeInOutBack(n, s=1.70158):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')

    n = n * 2
    if n < 1:
        s *= 1.525
        return 0.5 * (n * n * ((s + 1) * n - s))
    else:
        n -= 2
        s *= 1.525
        return 0.5 * (n * n * ((s + 1) * n + s) + 2)


def easeInBounce(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return 1 - easeOutBounce(1 - n)


def easeOutBounce(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n < (1/2.75):
        return 7.5625 * n * n
    elif n < (2/2.75):
        n -= (1.5/2.75)
        return 7.5625 * n * n + 0.75
    elif n < (2.5/2.75):
        n -= (2.25/2.75)
        return 7.5625 * n * n + 0.9375
    else:
        n -= (2.65/2.75)
        return 7.5625 * n * n + 0.984375


def easeInOutBounce(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n < 0.5:
        return easeInBounce(n * 2) * 0.5
    else:
        return easeOutBounce(n * 2 - 1) * 0.5 + 0.5

