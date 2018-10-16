from pprint import pprint as pp
from math import sqrt
#{key_expr:value_expr for item in iterable}

coutry_to_capital = {"United Kingdom":"London",
                    "Brazil":"Bazilia",
                    "Moroco":"Rabat",
                    "Sweden":"Stockholm"}

capital_to_coutry = {capital:country for country, capital in coutry_to_capital.items()}#IF THERE ARE IDENTICAL KEYS LATER KEYS WILL OVERWRITE EARLIER KEYS

# pp(capital_to_coutry)


def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i ==0:
            return False
    return True

# print(is_prime(1))
print([x for x in range(101) if is_prime(x)])   

prime_square_divisors={x*x:(1,x,x*x) for x in range(101) if is_prime(x)}

# pp(prime_square_divisors)