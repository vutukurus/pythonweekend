import subprocess
import sys

msg = sys.argv[1]

cmd1 = "git status"
cmd2= "git add *"
cmd3= 'git commit -m "{}" '.format(msg)
print cmd3


subprocess.call(cmd1, shell=True)
subprocess.call(cmd2, shell=True)
subprocess.call(cmd3, shell=True)
