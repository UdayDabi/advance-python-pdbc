def readfile():
    file = open("../files/hello.txt", 'r')

    text = file.read()
    print(text)
    file.close()


readfile()
