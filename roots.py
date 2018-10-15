import sys
def sqrt(x):
    """Compute square roots using the method of heron of alexadria.

    Args:
        The square root of x.

    Raises: 
        ValueError:if x is nagative
    """
    if x<0:
        raise ValueError("Raised Exception Cannot compute the sqrt of the nagative number : {}".format(x))
    guess=x
    i=0
    while guess * guess != x and i < 20:
        guess= ( guess + x / guess) /2.0
        i+=1
    return guess


def main():
    #print(sqrt(9))
    try:
        print(sqrt(-1))
    except ZeroDivisionError as e:
        print("Cannot compute the sqrt of the nagative number: {ex}".format(ex=e))
    except ValueError as e:
        print("Cannot compute the sqrt of the nagative number: {ex}".format(ex=e))
        print(e,file=sys.stderr)

if __name__=="__main__":
    main()


