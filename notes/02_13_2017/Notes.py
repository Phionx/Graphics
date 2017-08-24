#!/usr/bin/env python
'''
Notes
Aim: Line Algorithm
    Octant I
    (x0,y0) - (x1, y1)
    x = x0, y = y0
    d = 2A + B
    while (x <  x1):
        plot(x,y)
        if (d > 0 )
            y++
            d+=2B
        x++
        d+=2A
    
    Octant II
    midpoint: f(x+1/2, y + 1)
    (x0,y0) - (x1, y1)
    x = x0, y = y0
    d = A + 2B
    while (x <  x1):
        plot(x,y)
        if (d < 0 )
            x++
            d+=2A
        y++
        d+=2B

    Octant VIII
    midpoint: f(x + 1, y - 1/2)
    (x0,y0) - (x1, y1)
    x = x0, y = y0
    d = 2A - B
    while (x <  x1):
        plot(x,y)
        if (d < 0 )
            y--
            d-=2B
        x++
        d+=2A

    Octant VII
    midpoint: f(x + 1/2, y - 1)
    (x0,y0) - (x1, y1)
    x = x0, y = y0
    d = A-2B
    while (x <  x1):
        plot(x,y)
        if (d > 0 )
            x++
            d+=2B
        y--
        d-=2A
    '''
