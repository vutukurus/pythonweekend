f= open("task.txt")

print f.readlines()
f.close()


d = open("task.txt","w")
d.write("this is my forced line")
d.close()

f= open("task.txt")
#adfasfsda

