import sys

sys.stdout.write("Whats your name?")
name = sys.stdin.readline()
name = name.rstrip()

print "Hello %s!" % name
