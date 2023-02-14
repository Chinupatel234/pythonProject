import sys
file = open("d:\\chinmay.txt")
line1 = file.readline()
line2 = file.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write("No errors occurred\n")
