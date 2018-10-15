"""TUPLES"""

# t= ("norway",4.456, 3 )#immutable
# t[0]#access like lists
# len(t)
# for item in t:
#     print(item)

#   a=t+(3333,2323)  

#   t*3# repeated 3 the number of times 
# # nested tuple
#   a=((2,3)(4,5)(5,2))
#   a[2][0]# is 5 

#   k=(33,)# single element tuple
#   k=()# empty tuple

# def minmax(k):
#     return min(k),max(k)


# print(minmax([3,3,3,2,45,5,5,5]))
# lower, upper=minmax([3,54,4,7, 7,8])
# print(lower)
# print(upper)
# (a,(b,(c,d)))=(7,(4,(2,3)))
# print(a,b,c,d)
# a="jelly"
# b="bean"
# a,b=b,a #swaping values between variables

"""strings"""

# colors=";".join(["#3423324","#454544","#564644"]) 

# print(colors)

# print(colors.split(";"))

# colors="".join(["#3423324","#454544","#564644"]) # one way concatination

# a="unforgetable".partition("ble")# returns a tuple
# print(a)
# a,b,c="unforgetable".partition("ble")
# print(a)
# print(b)
# print(c)

# a,_,c="unforgetable".partition("ble")#"_" is to suppress unused value;

# sentence="the age of {0} is {1}".format('Jim',32)


# sentence="the age of {} is {}".format('Jim',32)# is also valid
# sentence="the age of {name} is {age}".format(name='Jim',age=32)

# print(sentence)

# import math
# a="Math constants : Pi={m.pi}, e={m.e}".format(m=math)
# print(a)
# b="Math constants : Pi={m.pi:.3f}, e={m.e:.4f}".format(m=math)
# print(b)

#python formating mini languages__Help(str)

"""RANGE"""


# print(range(5))#(stop)

# for i in range(5):
#     print(i)
    
    
# for i in range(7,10):#(start,stop)
#     print(i)

# for i in range(7,15,2):#(start,stop,step)
#     print(i)

# a=list(range(2,4))# convertinng range into list
# print(a)
# 
#
# t=[4,4,3,25,5,5,53,7]
# for i in enumerate(t):
#      print(i)

# for i,v in enumerate(t):#Tuple unpacking
#     print("i={0} and v={1}".format(i,v))


"""LISTS"""

# s="How You doing, How about talking over a dinner".split()
# print(s)
# print(s[-1])#negative indexing negative indexing is -1 based 
# print(s[1:3])#sliciinig(stop not included)
# print(s[1:-1])#all the elements expect first and last
# print(s[:3])#slices from the start till 3rd element (stop not included)
# print(s[3:])
# x=s[:]# this copies the list (x refers to a new object now but values are same)
# x=s.copy# this copies the list (x refers to a new object now but values are same)
# x=list(x) 
# ## all this performs a shallow copy PFA screenshots
# c=[3,2]
# d=c*4
# x=[0]*8 #repetitions repeat the ref will not copy the value PFA the screen shots

# i=s.index('You')# returns the index is not found -value error
# count=s.count("you")
# "you" in s# testing for member ship returns true or false
# "hey" not in s #tetsing  none membership returns true or false
# del s[2]# deleted the 2nd element
# s.remove("You")# removes "you" from the list"
# del s[s.index("You")]
# s.insert(2,"hey")
# z="".join(s)# joins the string
# s.extend("bug","me")
# s.reverse()
# s.sort()
# s.sort(reverse=True)#desceding sort(sort returns a new list)
# s.sort(key=len)# sort acco to length ascv
# v=reversed(s)# reversed returns an iterator


""" DICTIONARY"""
# #Keys must be immutable and values can be mutable  ,items are not stored in any perticular order, dicts are iterable
# names_and_ages=[("Alice",32),("Bob",48),("Charlie",28)]
# d=dict(names_and_ages)
# x=dict(a="alfa",b="beta")
# print(d)
# print(x)
# #copy
# z=d.copy()
# c=dict(z)
# c.update(d)#adds content of d to c if the key values are already pressent then corresponding value will be updated.

# for key in names_and_ages:# we can also iterate thro dict using values.
#     print("{key)=>{value}".format(key=key,value=names_and_ages[key]))


# for key ,value in names_and_ages.items():
#     print("{key}")

# #membership operaters in annd not in only work on keys 

#del d["Alice"]
# 
# from pprint import pprint as pp
# m={"H":[1,2,3]
#     ,"He":[3,4]
#     ,"Be":[7.9,10]}
    
# m["H"]+=[4,5,6,7]

# m["N"]=[2,2,2]
# #print(m)
# pp(m)
#d={}# empty dictionary

"""SET"""
# #mutable collection of unordered elements . sets are iterable, and membership operaters works on set
# p={6,3,55,34,3,8,23232}
# print(p)
# print(type(p))
# e=set()#empty set
# s=set([2,3,3,4,2,234,43,8])#from list- duplicates are discarded
# #s.add(233)
# p.update([23,23,23,2,2,2,2])
# print(p)
# p.remove(2)#error if the element is not pressent in the set
# p.discard(233)#no effect is the item is not pressent in the list
# d=p.copy()#shallow copy

# blue_eyes={"Olivia","Harry","Lily","Jack","Amelia"}
# blond_hair={"Harry","Jack","Mia"}
# o_blood={"Harry","Lily"}
# b_blod={"Lola","Amelia","Joshua","Olivia"}

# print(blue_eyes.union(blond_hair))
# print(blond_hair.intersection(blond_hair))
# print(blond_hair.difference(b_blod))#none commutative
# print(b_blod.symmetric_difference(blond_hair))#everything but not in both
# blond_hair.issubset(blue_eyes)
# blond_hair.issubset(b_blod)
# b_blod.isdisjoint(blue_eyes)





