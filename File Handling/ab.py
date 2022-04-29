def uppercount():
    upper=0
    f1=open("D:/SEM-4/PYTHON/LABS/PYTHON.txt",'r')
    line=f1.read()
    for i in line:
        if (i.isupper() == True):
            upper+=1
    print("Total no. of upper-case alphabets :",upper)
uppercount()