# import rarfile , csv 
# rar_path = rarfile.RarFile('//Users//muditverma//Downloads//FOM-1.rar')

# rar_path.printdir()
from sys import argv
try :
	import patoolib
except :
	print 'Not available , use "pip install patool" and then run this script '
	exit()
	
if len(argv) != 2  :
	print "No. of arguements expected = 1 ," ,len(argv)-1, "given. Use 'help' for more info"
	exit()
if argv[1] == 'help' :
	print 'Enter the absolute path in the arguement,\n  python',__file__,'[file-path]'
	print 'Extract location same as the archived file.'
	exit()

path = str (argv[1])

path_split = (argv[1]).split('/')
p = str(argv[1])
out = p.replace(path_split[-1] , '')
print out 

patoolib.extract_archive(path , outdir = out )
print 'Done!'