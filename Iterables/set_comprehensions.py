words ="Why sometimes I have Believed as many as six impossible things before breakfast".split()

# print(words)
x={len(word) for word in words}#{Expr(item) for item in iterable}
# print(x)

from math import factorial
f={len(str(factorial(x))) for x in range (1,20)}# returs the set and eleminates duplicates and is unordered 
print(f)