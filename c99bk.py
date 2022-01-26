import os
import shutil
source=input("enter the path :")
destination=input("enter the path :")

source=source+"/"
destination=destination+"/"

listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)

def getTime():
    ctime = os.stat(path).st_ctime
    return ctime


