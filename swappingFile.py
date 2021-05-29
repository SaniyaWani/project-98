def swapFileData ():
    textInput = input("Write name of file you want to open")
    if(textInput=="file1"): 
        openFile=open('sample2.txt',"r")
        lines = openFile.readlines()
        for l in lines :
            print(l)
    elif(textInput=="file2"): 
        openFile=open('sample1.txt',"r")
        lines = openFile.readlines()
        for l in lines :
            print(l)


swapFileData()