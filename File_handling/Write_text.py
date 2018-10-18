# f=open("wasteland.txt",mode="wt",encoding="UTF-8")
# f.write("hello!!!....wasteland")
# f.write("\n what the hell!!")

# f.writelines(["hi Sam, \n",
# 		 "hello Ram"])
	   
# f.close()
# print(f)


import sys

def main(filename):
    f=open(filename,mode='rt',encoding="UTF-8")
    for line in f:
        print(line)

if __name__=="__main__":
    # main(sys.argv[1])
    main("wasteland.txt")