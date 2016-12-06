dict = {"apple":100, "orange":50, "melon":1000}

print dict.items()
print "=================="

for x in sorted(dict.items(), key=lambda x:x[1]):
    print x

print "=================="

for x in sorted(dict.items(),key=lambda x:x[1], reverse=True):
    print x
