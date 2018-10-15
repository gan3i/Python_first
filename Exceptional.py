import sys
from math import log
def convert(s):
    '''convert to an integer.'''
    if not isinstance(s,int):#tend not to type error
        raise TypeError("Argument must be integer")
    try:
        return int(s)
    except ValueError as e:#except (TypeError,ValueError):
        print("convert failed:Value Eror : {0}".format(str(e)),file=sys.stderr)
        raise
        #return -1
    except TypeError as e:
        print("convert failed:Type Error : {0}".format(str(e)),file=sys.stderr)
        return -1
    except:
        #print("f**king Error")
        pass
#Inentation error, SyntaxError, Name Error are result of programmer's mistake better not to cath these exception
 #Look before you leapp
 #EASP

def string_log(s):
    v=convert("S")
    return log(v)

# p="/Files/text.txt"
# try:
#     process_file(f)
# except OSError as elif expression:
#     pass
   
 
convert("e")
