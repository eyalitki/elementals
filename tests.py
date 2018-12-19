import pycodestyle
import pydocstyle
import os

SRC_DIR = "elementals"

def fileList() :
	return map(lambda x : os.path.join(SRC_DIR, x), filter(lambda x : x.endswith(".py"), os.listdir(SRC_DIR)))

file_list = fileList()	

passed = True

# Documentation tests
for check in pydocstyle.check(file_list, ignore = ["D100", "D104", "D413", "D213", "D203"]) :
	print check
	passed = False
	
# last status
exit(0 if passed else 1)