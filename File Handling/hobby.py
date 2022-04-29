def count_words():
    file = open("D:\SEM-4\PYTHON\LABS\python.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count+=1
    print(count)
    file.close()

count_words()