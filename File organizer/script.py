import os, shutil

path = input("Enter path: ")
path = path.replace('\\',"\\\\")
print(path)
try:
    for (path, dirs, files) in os.walk(path):
        print(path, dirs, files)
        for file in files:
            extension = file.split(".")[1]
            print(extension)
            if(os.path.exists(path+extension)):
                if file.endswith(extension):
                    shutil.move(file,path+extension)
            else:
                os.system("mkdir "+extension)
                shutil.move(file,path+"\\"+extension)
except:
    print("Done?")