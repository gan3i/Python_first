words ="Why sometimes I have Believed as many as six impossible things before breakfast".split()

iterator=iter(words)
while next(iterator):# ate the end of the collection StopIterartion exception will be raised
    print(iterator)
