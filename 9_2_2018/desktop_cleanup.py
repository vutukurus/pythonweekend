#Desktop cleanup system
#design..
#first all grab all d files in the folder..
#i will get extension of the files..
#[py,txt,txt,py]
#[py,txt]
import os
import shutil
clean_path = r"C:\Users\siv\Desktop"

#step1: Get list of files/folders present in your designated path..
list_of_files = os.listdir(clean_path)
cleaned_list=[]
extns = []
print list_of_files


for i in list_of_files:
	fullpath = clean_path +"\\"+ i
	#print fullpath
	if os.path.isfile(fullpath):
		print "FILE : {}".format(fullpath)
		cleaned_list.append(fullpath)
	else:
		print "DIR : {}".format(fullpath)

print cleaned_list
#step3: Getting extensions..
for i in cleaned_list:
	ext = i.split(".")
	extns.append(ext[-1])
print extns
rem_dupl_extns = set(extns)
print rem_dupl_extns

#cleaned system dire..
cleaned_path = clean_path + "\\" + "cleaned_system"
if os.path.exists(cleaned_path):
	print "Folder exists not creating"
else:
	os.mkdir(cleaned_path)

for i in rem_dupl_extns:
	full_path = cleaned_path + "\\" + i
	if os.path.exists(full_path):
		print "Folder exists"
	else:
		os.mkdir(full_path)

#Copy respective files to their home directories..
for i in cleaned_list:
	ext = i.split(".")[-1]
    #C:\Users\siv\Desktop\two.json #C:\Users\siv\Desktop\cleaned_system\json
	dest_path = cleaned_path + "\\" + ext
	print dest_path
	shutil.move(i,dest_path) 


















