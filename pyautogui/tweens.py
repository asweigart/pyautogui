import math

def getPointOnLine(x1, y1, x2, y2, n):
    """Returns the (x, y) tuple of the point that has progressed a proportion
    n along the line defined by the two x, y coordinates.

    Args:
      x1 (int, float): The x coordinate of the line's start point.
      y1 (int, float): The y coordinate of the line's start point.
      x2 (int, float): The x coordinate of the line's end point.
      y2 (int, float): The y coordiante of the line's end point.
      n (float): Progress along the line. 0.0 is the start point, 1.0 is the end point. 0.5 is the midpoint. This value can be less than 0.0 or greater than 1.0.

    Returns:
      Tuple of floats for the x, y coordinate of the point.
    """
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return  (x, y)


def linear(n):
    """A linear tween function
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n


linearTween = linear # kept for backwards compatibility


def easeInQuad(n):
    """A quadratic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**2;


def easeOutQuad(n):
    """A quadratic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -n * (n-2)


def easeInOutQuad(n):
    """A quadratic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n < 0.5:
        return 2 * n**2
    else:
        n = n * 2 - 1
        return -0.5 * (n*(n-2) - 1)


def easeInCubic(n):
    """A cubic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**3


def easeOutCubic(n):
    """A cubic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n**3 + 1


def easeInOutCubic(n):
    """A cubic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**3
    else:
        n = n - 2
        return 0.5 * (n**3 + 2)


def easeInQuart(n):
    """A quartic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**4


def easeOutQuart(n):
    """A quartic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return -(n**4 - 1)


def easeInOutQuart(n):
    """A quartic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**4
    else:
        n = n - 2
        return -0.5 * (n**4 - 2)


def easeInQuint(n):
    """A quintic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n**5


def easeOutQuint(n):
    """A quintic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n**5 + 1


def easeInOutQuint(n):
    """A quintic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = 2 * n
    if n < 1:
        return 0.5 * n**5
    else:
        n = n - 2
        return 0.5 * (n**5 + 2)


def easeInSine(n):
    """A sinusoidal tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -1 * math.cos(n * math.pi / 2) + 1


def easeOutSine(n):
    """A sinusoidal tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return math.sin(n * math.pi / 2)


def easeInOutSine(n):
    """A sinusoidal tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -0.5 * (math.cos(math.pi * n) - 1)


def easeInExpo(n):
    """An exponential tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n == 0:
        return 0
    else:
        return 2**(10 * (n - 1))


def easeOutExpo(n):
    """An exponential tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n == 1:
        return 1
    else:
        return -(2 ** (-10 * n)) + 1


def easeInOutExpo(n):
    """An exponential tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """A circular tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return -1 * (math.sqrt(1 - n * n) - 1)


def easeOutCirc(n):
    """A circular tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n -= 1
    return math.sqrt(1 - (n * n))


def easeInOutCirc(n):
    """A circular tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n * 2
    if n < 1:
        return -0.5 * (math.sqrt(1 - n**2) - 1)
    else:
        n = n - 2
        return 0.5 * (math.sqrt(1 - n**2) + 1)


def easeInElastic(n, amplitude=None, period=None):
    """An elastic tween function that begins with an increasing wobble and then snaps into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """An elastic tween function that overshoots the destination and then "rubber bands" into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """An elastic tween function wobbles towards the midpoint.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """A tween function that backs up first at the start and then goes to the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n * n * ((s + 1) * n - s)


def easeOutBack(n, s=1.70158):
    """A tween function that overshoots the destination a little and then backs into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    n = n - 1
    return n * n * ((s + 1) * n + s) + 1


def easeInOutBack(n, s=1.70158):
    """A "back-in" tween function that overshoots both the start and destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """A bouncing tween function that begins bouncing and then jumps to the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return 1 - easeOutBounce(1 - n)


def easeOutBounce(n):
    """A bouncing tween function that hits the destination and then bounces to rest.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
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
    """A bouncing tween function that bounces at the start and end.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    if n < 0.5:
        return easeInBounce(n * 2) * 0.5
    else:
        return easeOutBounce(n * 2 - 1) * 0.5 + 0.5



