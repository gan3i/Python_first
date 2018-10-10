# #integer is immutable objecct type
# a=2
# print(id(a))
# b=a 
# a==b
# # id(a) and id(b) are equal

# #lists are mutable objecct types

# a=[1,2,3]
# s=a
# s[0]=4
# # now even list a will have the value which is same as list s


# m=[9,3,3,]
# def modify(k):
#     k.append(2)
#     print("k=",k)# this prints k=[9,3,3,2] and at the end of this even list m will have the same valules 

# def replace(f):
#     f=[17,12,15]
#     print("f=",f)# this will print f=[17,12,15] and the list m will still have the original velues
#     #this happens if we re-assign a new list to the formal referece 

# def replace_contents(f):
#     f[1]=45
#     f[2]=56
#     print("f=",f)# this will print f=[17,12,15] and the list m will still have the original velues
#     #this happens if we re-assign a new list to the formal referece 
# g=[1,2,3]
# print(g)#this  will print [1,2,3]
# replace_contents(g)
# print(g)#this will print [1, 45, 56]

#################Function args and default value####################################
# def banner(message,border="-"):
#     line=border*len(message)
#     print(line)
#     print (message)
#     print(line)

# banner("line with border")
# banner("line with border","*")
# banner("line with border,border="*")
# banner(meessage="line with border",border="*")

# ----------------
# line with border
# ----------------
# ****************
# line with border
# ****************
# w


# import time
# time.ctime()
# def show_default(arg=time.ctime()):
#     print(arg)


# show_default()
# show_default()
# show_default()# the display time never progresses because default argument evaluation happens along with def
# #to avoid the issues because of this behaviour always try to use immutable objects as default values 


# def add_spam(menu=[]):
#     menu.append("spam")
#     return menu

# breakfast=["bacon","eggs"]
# add_spam(breakfast)#["bacon","eggs","spam"]

# def add_spam(menu=None):
#     menu.append("spam")
#     return menu


# """Variable scoping"""
# count=0
# def show_count():
#     print("count=",count)


# def set_count(c):
#     global count# this line is required to avoid the local scoping of the variable count
#     count=c

import Modularity
import Print_words
# print(type(Modularity))
# print(dir(Modularity)) 
# print(type(Modularity.__name__))
#print(type(Print_words.fetch_words))
print(dir(Print_words.fetch_words))



 
