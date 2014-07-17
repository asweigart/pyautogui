
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


# dev note - b will always be 0.0, c and d will always be 1.0, their t is my n

def easeInQuad(n):
    return n*n;

def easeOutQuad(n):
    return -1.0 * (n)*(n-2)

def easeInOutQuad(n):
    if n < 0.5:
        return 2*n*n
    else:
        n = n * 2 - 1
        return -0.5 * (n*(n-2) - 1)