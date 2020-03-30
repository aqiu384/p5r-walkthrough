#!/usr/bin/python3
import sys

COOPS = {}
CURR_ROUTE = sys.argv[2]

with open(sys.argv[1]) as mdfile:
    for line in mdfile:
        line = line.strip()

        if '[' in line:
            version = line.split('[')[1].split(']')[0]

            if version != CURR_ROUTE:
                continue
        if ' Rank ' in line or ' Hangout ' in line:
            cevent = line.split('(')[0].replace(']', ',')
            cevent = cevent.split(',')[-1].replace('*', '').strip().split(' ')
            coop = cevent[0]
            event = ' '.join(cevent[1:])

            if coop not in COOPS:
                COOPS[coop] = []
            COOPS[coop].append(event)

for coop, events in COOPS.items():
    print(coop)
    for event in events:
        print('*', event)
