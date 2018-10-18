""" read annd print an integer series ."""


import sys
def read_series(filename):
    f=open(filename,mode="rt",encoding="UTF-8")
    series=[]
    for line in f:
        a=int(line.split())
        series.append(a)
    f.close()
    return series

def main(filename):
    series=read_series(filename)
    print(series)

if __name__=="__main__":
    main(sys.argv[1])
