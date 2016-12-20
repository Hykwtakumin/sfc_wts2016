import re

for line in open('country_names.lst','r'):
    line = line.rstrip()
    if re.search(r'Ja',line):
        print line
