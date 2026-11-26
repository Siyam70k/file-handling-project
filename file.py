from pathlib import Path
import os
def readfileandfolder():
    path=Path('')
    items=list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1}:{items}")
#create file code
def createfile():
    readfileandfolder()
    try:
        name=input("tell your file name:-")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("what do you wanna write:-")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else: 
            print("not possible this file already exist")
    except Exception as err:
        print(f"an error occured in{err}")
# readfile code
def readfile():
    readfileandfolder()
    try:
        name=input("hey buddy which file you wanna read:-")
        p=Path(name)
        if  p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
            print("YOU READ THE FILE SUCCESSFULLY")
        else:
            print("there is no file matched file name you Entered")
    except Exception as err:
        print(f"an error occured in {err}")
#updating file code
def updatingfile():
    try:
        readfileandfolder()
        name=input("which file name you want to change:-")
        p=Path(name)
        print("press 1 for change the file name")
        print("press 2 for overwrite in the file ")
        print("press 3 for append the file")
        res=int(input("please tell your response:-"))
        #code for file name changed
        if res ==1:
            name2=input("tell your new file name:-")
            p2=Path(name2)
            if p.exists() and p.is_file():
                p.rename(p2)
                print("NAME CHANGED SUCCESSFULLY")
            else:
                print("not existed")
        #code for overwrite in file
        if res==2:
            if p.exists() and p.is_file():
                with open(p,"w") as fs:
                    data=input("what you wanna overwrite:-")
                    fs.write(data)
                    print("OVERWRITE SUCCESSFULLY")
            else:
                print("sorry something went wrong")
        #code for append something in file
        if res==3:
            if p.exists() and p.is_file():
                with open(p,"a") as fs:
                    data=input("what you wanna append:-")
                    fs.write(data)
                    print("APPEND SUCCESSFULLY")
            else:
                print("something is wrong")
    except Exception as err:
        print(f"an error occured in {err}")
#deleting file code
def deletingfile():
    try:
        readfileandfolder()
        name=input("which file you wanna delete:-")
        p=Path(name)
        if p.exists() and  p.is_file():
            os.remove(p)
            print("REMOVED FILE SUCCESSFULLY")
        else:
            print("your entered file doesn't exist")
    except Exception as err:
        print(f"an error occured in{err}")  
#code for user input         
print("press 1 for create file")
print("pres 2 for read file ")
print("press 3 for updating file")
print("press 4 for deleting the file")
check=int(input("please tell your response:-"))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatingfile()
if check ==4:
    deletingfile()


    