try:
    f = open("E:\Harry.txt")
    f.write("LOREM IPSUM")
except:
        print("Something went wrong")
finally:
        f.close()
