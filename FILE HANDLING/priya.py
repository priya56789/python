f=open("file.txt","r")
print(f.read())
f.close()
f=open("file.txt","w")
print(f.write("anjali"))
f.close()


with open("file.txt","w") as f:
    f.write("Hiiii\n")
    f.writelines("Hii\n")
with open("file.txt","a") as f:
    f.writelines("where programming\n")
with open("file.txt","r+") as f:
    #print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readlines())
    print(f.tell())
    #print()
    f.seek(0)
    f.truncate(20)
    print(f.read())


    #f.seek(0)
    print(f.read(10))