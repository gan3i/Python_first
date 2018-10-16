"""generator comprehensions"""

million_squares=(x*x for x in range(1,10001))
# print(next(million_squares))

l=list(million_squares)

# print(l)

a=sum(x*x for x in range(1,10001))#we can add if clauss

#itertools 10.1


from itertools import islice,count
from Dict_comprehensions import is_prime


thousand_primes=islice((x for x in count() if is_prime(x)),1000)
# print(sum(list(thousand_primes)))

# print(any([True,False,True]))

# print(any([True,True,True]))

# print(any(is_prime(x) for x in range(1328,1361)))

# print(all(name==name.ti for name in ["London","New York","Sydney"]))

sunday=[12,23,1,2,1,1,1,1,1,3,4,4,23,]
monday=[2,2,4,2,2,23,23,23,23,2,323,2,]

for item in zip(sunday,monday):
    print(item)

for sun,mon in zip(sunday,monday):# zip can accept any number of iterable objects
    print("average=", (sun+mon)/2)


from itertools import chain

tempe=chain(sunday,monday)# this is temp chain
print(tempe)
