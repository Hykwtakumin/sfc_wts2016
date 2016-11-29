import sys

sys.stdout.write("Input first number")
n1 = sys.stdin.readline()
n1 = int(n1.rstrip())

sys.stdout.write("Input second number")
n2 = sys.stdin.readline()
n2 = int(n2.rstrip())

if n1 > n2:
    print "%d is larger" % n1
elif n2 > n1:
    print "%d is larger" % n2
else:
    print "same"
