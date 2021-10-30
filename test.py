'''
    Exemple of how it works
    in this file only to explain with tests
    To see all look file app.py
'''
import os, shutil, re, mimetypes, time, datetime


dirName = 'temp/'
dirNameTree = 'temp2/x/p/t/o'


#create a dir unique
if not os.path.exists(dirName):
    os.makedir(dirName)
    print("Directory " , dirName ,  " Created ")
else:
    print("Directory " , dirName ,  " already exists")


#create a tree of dirs
if not os.path.exists(dirNameTree):
    os.makedirs(dirNameTree)
    print("Directory " , dirNameTree ,  " Created ")
else:    
    print("Directory " , dirNameTree ,  " already exists")


#Find all type of files in dir name past and show all the files
[print(re.match("(.*?)/",mimetypes.guess_type(i)[0]).group(1)) for i in os.listdir() if '.' in i]

#Using dir windowns for test in my computer
dir_test = 'D:\HermesAugusto\Documents\files'

#get date of create and date of modification using getmtime
#Format the date of file to yyyy-mm
time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime("new 3.txt"))))
#Frist get time of file in seconds is return a float
x = os.path.getctime("new 3.txt")
#convert to time in format Fri Oct 29 20:30:15 2021
y = time.ctime(x)
#Convrerto to object time and transform to pattern yyyy-mm
t_obj = time.strftime("%Y-%m",time.strptime(y))

#walk in tree dirs using regx to get type each of file and printing this
for root, dirs, files in os.walk(dir_test):
    print("ROOT: ", root)
    print("dirs: ", dirs)
    print("files: ", files)
    
    [print(re.match("(.*?)/",mimetypes.guess_type(i)[0]).group(1)) for i in files ]
#How make a copy of file using shutil
shutil.copy2('new 3.txt','D:\HermesAugusto\Documents\Projects\personal\study' )
#How make a move of file using shutil
shutil.move('new 3.txt','D:\HermesAugusto\Documents\Projects\personal\study')
