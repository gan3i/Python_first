words ="Why sometimes I have Believed as many as six impossible things before breakfast".split()

iterator=iter(words)
for v in iterator:# ate the end of the collection StopIterartion exception will be raised
    print(v)

iterator2=iter(words)
while iterator2:
    print(next(iterator2))
