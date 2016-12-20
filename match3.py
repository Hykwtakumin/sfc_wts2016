import re
import codecs

for line in open('contact.html','r','euc-jp'):
    line = line.rstrip()
    match = re.search(r'(\d{4})-(\d{2})-(\d{4})',line)
    if match:
        print match.group(1),match.group(2),match.group(3)
