#!/usr/bin/python3
import json

with open('dist/coop-answers.json') as jsonfile:
    coops = json.load(jsonfile)

for currwalk in ['walkthrough.md', 'ace-walkthrough.md']:
    with open('src/' + currwalk.replace('walkthrough', 'how-to-use')) as txtfile:
        nlines = list(txtfile)

    with open('src/' + currwalk) as txtfile:
        for line in txtfile:
            bline = line.replace('(', "**(").replace(')', ")**").replace('[', '**[').replace(']', ']**')
            nlines.append(bline)

            if '[' in line:
                line = '* ' + line.split('] ')[1]

            if ' Rank ' in line or (' Hangout ' in line and 'Strength' not in line):
                rank = line[2:].split('(')[0].strip()
                rank = rank.split(' ')[-4:]
                if ',' in rank[0]:
                    rank = rank[1:]
                arcana = rank[0]
                rankey = ' '.join(rank[1:])

                for aline in coops[arcana][rankey]:
                    nlines.append('    ' + aline)

    with open('dist/' + currwalk, 'w+') as txtfile:
        txtfile.write(''.join(nlines))
