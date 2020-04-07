#!/usr/bin/python3
import sys

COSTS = []
CURR_ROUTE = sys.argv[2]

ppalace = 'START'
ctotal = 0

with open(sys.argv[1]) as mdfile:
    for line in mdfile:
        line = line.strip()

        if 'Palace' in line and 'Clear' not in line:
            print(ctotal, ppalace)
            ctotal = 0
            ppalace = line
        elif '(Y' in line:
            cost = int(line.split('(Y')[1].split(')')[0])
            print('   ', cost, line)
            ctotal += cost
        elif 'uy ' in line:
            print('   ', line)
