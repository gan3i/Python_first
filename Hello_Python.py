"""print("Hello!..World")"""
# import math
# math.sqrt(81)
# from math import factorial as fact
# n=13
# r=3
# print(fact(n)/(fact(r)*fact(n-r)))
# print(fact(20))
# for i in range(5):
#     x=i*10
#     print(x)
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
	story_words=[]
	for line in story:
		line_words=line.split()
		for word in line_words:
			story_words.append(word)


print(story_words)

            



            






