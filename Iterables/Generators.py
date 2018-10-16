
words ="Why sometimes I have Believed as many as six impossible things before breakfast".split()

# def gen123():
#     print("yield 1")
#     yield 1
#     print("yield 1")
#     yield 2
#     print("yield 1")
#     yield 3
#     #return #implpicit return

# g=gen123()
# z=gen123()# each of thesee objectcs will have distinct adresses.
# f=next(g)
# h=next(g)
# i=next(g)
# # j=next(g)# stop iteration exception
# print(f,h,i)


def take(count,iterable):
    """Take first count elements
       stops when count number of elements are yielded
    """
    counter=0# generators maintain state in local variables. lazy evaluation
    for item in iterable:
        if counter==count:
            return
        counter+=1
        yield item


def run_take():
    for word in take(4,words):
        print(word)


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    yield:
        Unique elements in order from "iterable".
    """
    seen=set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items=[2,2,88,4,3,4,34,3,21223,8]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items=[2,4,5,5,3,88,4,6,6,7]
    for item in take(3,distinct(items)):
        print(item)




# Lucas series
def lucas():
    yield 2
    a=2
    b=1
    while True:
        yield b
        a, b= b, a+b


def print_lucas():
    for x in lucas():
        print(x)


if __name__=="__main__":
    # run_take()
    # run_distinct()
    # run_pipeline()
    print_lucas()# prints infite numbers ctrl+c to exit the lood on REPL






