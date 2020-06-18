#! /usr/bin/env python3

import csv
import os
import sys

# votes_csv = os.path.abspath(sys.argv[1])
votes_csv = os.path.abspath('data\\db-surfaces\\db-surfaces_votes.csv')
complete_csv = votes_csv.replace('votes', 'complete')

votes = []
with open(votes_csv, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        votes.append(row)

for vote in votes:
    sample = vote['sample']
    splits = sample.split('_')

    if splits[0] == 'subject':
        vote['subject'] = '_'.join(splits[0:2])
        vote['sample_type'] = '_'.join(splits[2:])
        vote['gold_standard'] = False
    elif splits[0] == 'gold':
        vote['subject'] = '_'.join(splits[1:3])
        vote['sample_type'] = '_'.join(splits[3:-1])
        vote['gold_standard'] = True
    else:
        print('something went terribly wrong wth the sample on vote ' + vote['vote'])
        vote['subject'] = ''
        vote['sample_type'] = ''
        vote['gold_standard'] = ''

with open(complete_csv, 'w', newline='') as f:
    fieldnames = votes[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for vote in votes:
        writer.writerow(vote)
