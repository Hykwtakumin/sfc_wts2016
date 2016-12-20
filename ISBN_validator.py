import sys
import re

line = sys.stdin.readline()
line = line.rstrip()
    # match = re.search(r'(\d{10})',line) #ISBN
    # if match:
    #     #check_digit = re.search(r'(\d$)', match)
    #     #other_digit = re.search(r'(\d{9})', match)
    #     check_digit = match[-1]
    #     other_digit = match[0:9]
    #     for digits in other_digit:
match = re.search(r'(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)',line) #ISBN
if match:
    total = int(match.group(1)) * 1 + \
            int(match.group(2)) * 2 + \
            int(match.group(3)) * 3 + \
            int(match.group(4)) * 4 + \
            int(match.group(5)) * 5 + \
            int(match.group(6)) * 6 + \
            int(match.group(7)) * 7 + \
            int(match.group(8)) * 8 + \
            int(match.group(9)) * 9 + \
            if total % 11 == int(match.group(10)):
                print 'OK'
