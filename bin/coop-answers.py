#!/usr/bin/python3
import re
import json

coops = {}
currop = {}
currans = []

with open('src/confidants.md') as txtfile:
    for line in txtfile:
        if line == '':
            continue
        if line.startswith('###') and line[3] != '#':
            cname = line.replace('###', '').strip()
            currans = []
            currop = {}
            coops[cname] = currop
        elif line.startswith('Rank ') or line.startswith('Hangout '):
            rname = ' '.join(line.split(' ')[:2]).strip().replace(':', '')

            if 'Romance' in line:
                rname += ' Romance'
            if 'Friendship' in line:
                rname += ' Friendship'

            currans = []
            currop[rname] = currans
        elif re.search('^\d+', line):
            boostans = line.replace('(+2)', '(+3)').replace('(+1)', '(+2)')
            currans.append(boostans)

for arcana in ['Moon', 'Sun']:
    coops[arcana]['Rank 0.1'] = []
    coops[arcana]['Rank 6.1'] = []
    for i in range(10):
        coops[arcana]['Rank ' + str(i + 1)] = []

with open('dist/coop-answers.json', 'w+') as jsonfile:
    json.dump(coops, jsonfile, indent=2, sort_keys=True)
