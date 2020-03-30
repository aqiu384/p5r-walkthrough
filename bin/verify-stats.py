#!/usr/bin/python3
import sys

SSTATS = ['Knowledge', 'Guts', 'Proficiency', 'Kindness', 'Charm']
STOTALS = { x: 0 for x in SSTATS }
STHRESH = {
    'Knowledge': [34, 82, 126, 192, 999],
    'Guts': [11, 38, 68, 113, 999],
    'Proficiency': [12, 34, 60, 87, 999],
    'Kindness': [14, 47, 94, 136, 999],
    'Charm': [6, 52, 92, 132, 999]
}

CURR_RANKS = { x: [STHRESH[x][0], 1] for x in SSTATS }
FNAME = sys.argv[1]
MIN_VERSION = int(sys.argv[2].replace('.', ''))

currdate = ''
rankups = []

with open(sys.argv[1]) as mdfile:
    for line in mdfile:
        line = line.strip()

        if line.startswith('### '):
            print(STOTALS, line[3:].strip())
        if line.startswith('#### '):
            currdate = line[4:].strip()
        if '+' not in line:
            continue
        if '[' in line:
            version = line.split('[')[1].split(']')[0]
            comp, version = version.replace('Version', '').strip().split()
            version = int(version.replace('.', ''))

            if comp == '>=' and MIN_VERSION < version:
                continue
            elif comp == '<' and MIN_VERSION >= version:
                continue

        sparts = [x.strip() for x in line.replace('(', ',').replace(')', ',').split(',')]

        for spart in sparts:
            if '+' in spart:
                sname, sgain = spart.split(' +')
                sgain = int(sgain)

                if sname in STOTALS:
                    STOTALS[sname] += sgain

                    if STOTALS[sname] >= CURR_RANKS[sname][0]:
                        nthresh, ntind = CURR_RANKS[sname]
                        rankups.append(' '.join([
                            currdate, line, sname, 
                            'Lv. {} {}'.format(ntind + 1, STOTALS[sname])
                        ]))

                        CURR_RANKS[sname] = [STHRESH[sname][ntind], ntind + 1]

for rankup in rankups:
    print(rankup)
