import subprocess
val=raw_input("Enter value\n")
args = val.split()
print args
process = subprocess.Popen(args,shell=False)
