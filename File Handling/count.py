fh=open("D:/SEM-4/PYTHON/LABS/PYTHON.txt","r")
count=0
lines=fh.readlines()
for a in lines:
    count=count+1
    print(count,a)
fh.close()