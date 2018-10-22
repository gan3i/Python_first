""" read annd print an integer series ."""


import sys
from pprint import pprint 
def read_series(filename):
    # try:
    #     f=open(filename,mode="rt",encoding="UTF-8")
    #     return[int(line.strip()) for line in f]
    #     # series=[]
    #     # for line in f:
    #     #     a=int(line.strip())
    #     #     series.append(a)
    #     # return series
    # finally:
    #     f.close()

    with open(filename,mode="rt",encoding="UTF-8") as f:
        return[int(line.strip()) for line in f]

    

def main(filename):
    series=read_series(filename)
    pprint(series)

if __name__=="__main__":
    # main(sys.argv[1])
    main("wasteland.txt")
