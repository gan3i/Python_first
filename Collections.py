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

s="How You doing, How about talking over a dinner".split()
print(s)
print(s[-1])#negative indexing negative indexing is -1 based 
print(s[1:3])#sliciinig(stop not included)
print(s[1:-1])
print(s[:3])
print(s[3:])




