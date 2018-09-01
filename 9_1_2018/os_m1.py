#Os module.
import os #importing os module functionality...
import shutil #copy, move

#os - operating system..
#os.listdir -> all files present in a folder...
print os.listdir(r"C:\Users\siv\Desktop\test")

#os.path.exists()-
#presence of a file..
print os.path.exists(r"C:\Users\siv\Desktop\test\abc.py")
print os.path.exists(r"C:\Users\siv\Desktop\test\fadfjsak.py")

#how to check whether it is a filer or director
#os.path.isdir--> true
#os.path.isfile-> true..
print os.path.isfile(r"C:\Users\siv\Desktop\test\abc.py")
print os.path.isfile(r"C:\Users\siv\Desktop\test")

#create a directory..
#os.mkdir(r"C:\Users\siv\Desktop\test\python")
#makedirs.. recursively..
#os.makedirs(r"C:\Users\siv\Desktop\test\one\two\three")

#copying files from one locagtion to other location..
#shutil.move
shutil.copy(r"C:\Users\siv\Desktop\test\ex_1.py",r"C:\Users\siv\Desktop\test\python")

#os.remove()
#shutil.rmtree()
#os.getcwd()
print os.getcwd()

#os.chdir --> used to change teh dierctory
os.chdir(r"C:\Users\siv\Desktop\weekend\tt")

print os.getcwd()




