#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return lines

def main():
    #get our data as an array from read_in()
    lines = read_in()

    print lines

    # #create a numpy array
    # np_lines = np.array(lines)
    #
    # #use numpys sum method to find sum of all elements in the array
    # lines_sum = np.sum(np_lines)
    #
    # #return the sum to the output stream
    # print lines_sum

#start process
if __name__ == '__main__':
    main()
