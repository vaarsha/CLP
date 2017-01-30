import subprocess
import sys
val=raw_input("Enter value\n")
args = val.split()
if args[0] == 'rm'and args[1] = '\':
    print "Danger don\'t even try it"
    sys.exit()
print args
process = subprocess.Popen(args,shell=False)
