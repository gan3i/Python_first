"""Computing Mandelbrot sets"""

import math 

def mandel (real, imag):
    """ Compute a point in the mandalbrot.

    The logarithm of number oif iterations needed to 
    determine wehter a comples point in in the 
    madelbrot set.

    Args:
        real: the real coordinate
        imag:imaginary coordinate

    Returns:
        A integer in the range 1-255>
    """
    x = 0
    y = 0
    for i in range(1,257):
        if x * x + y * y > 4.0:
            break
        xt = real + x * x - y * y
        y =  imag + 2.0 * x * y
        x=xt
    return int(math.log(i) * 256 / math.log(256))-1


def Mandelbrot(Size_x,Size_y):
    """ Make an mandelbrot set image.

    Args:
        size_x: Image widht
        size_y: Image height

    Returns:
        A list of lits of integers in the range of 0-255>
    """
    return [[mandel((3.5 * x / Size_x) - 2.5 ,
                    (2.0 * y / Size_y) - 1.0)
                    for x in range(Size_x)]
                    for y in range(Size_y)]

# if __name__=="__main__":
#     pixles=Mandelbrot(448,256)
#     print(pixles)               