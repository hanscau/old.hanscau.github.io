from os import listdir
from os.path import isfile, join
open('trainval.txt', 'w').close()
mypath="../../JPEGImages/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
with open("trainval.txt", "a") as f:
	f.truncate()
	for fi in onlyfiles:
		s=str(fi)
		f.write("%s\n" % (s[:-4]))
		print(s[:-4])
