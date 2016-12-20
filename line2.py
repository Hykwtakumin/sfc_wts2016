fp = open('output', 'w')

for line in open('country_names.lst','r'):
    line = line.rstrip()
    fp.write(line + '\n')

fp.close()
