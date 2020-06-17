#! /usr/bin/env python3

import csv
import json
import os
import re
import sys

# database_json = os.path.abspath(sys.argv[1])
database_json = 'data\\db-func_to_t1_reg.json'

sampleCounts_csv = database_json + '_sampleCounts.csv'
sampleSummary_csv = database_json + '_sampleSummary.csv'
userSeenSamples_csv = database_json + '_userSeenSamples.csv'
users_csv = database_json + '_users.csv'
votes_csv = database_json + '_votes.csv'

with open(database_json, 'r') as f:
    db = json.load(f)

sampleCounts_dict = db['sampleCounts']
sampleSummary_dict = db['sampleSummary']
userSeenSamples_dict = db['userSeenSamples']
users_dict = db['users']
votes_dict = db['votes']

# sampleCounts
with open('data\\sampleCounts_header.csv', 'r') as f:
    header = f.readline().split(',')

with open(sampleCounts_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for sample in sampleCounts_dict:
        writer.writerow({ 
            'sample': sample , 
            'count': sampleCounts_dict[sample] 
            })


# sampleSummary
with open('data\\sampleSummary_header.csv', 'r') as f:
    header = f.readline().split(',')

with open(sampleSummary_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for sample in sampleSummary_dict:
        writer.writerow({ 
            'sample': sample , 
            'aveVote': sampleSummary_dict[sample]['aveVote'] , 
            'count': sampleSummary_dict[sample]['count'] 
            })


# userSeenSamples
with open('data\\userSeenSamples_header.csv', 'r') as f:
    header = f.readline().split(',')

with open(userSeenSamples_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for user in userSeenSamples_dict:
        for sample in userSeenSamples_dict[user]:
            writer.writerow({ 
                'user': user , 
                'sample': sample , 
                'count': userSeenSamples_dict[user][sample] 
                })


# users
with open('data\\users_header.csv', 'r') as f:
    header = f.readline().split(',')

with open(users_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for user in users_dict:
        if 'admin' in users_dict[user]:
            admin = users_dict[user]['admin']
        else:
            admin = ''

        if 'consent' in users_dict[user]:
            consent = users_dict[user]['consent']
        else:
            consent = ''

        if 'level' in users_dict[user]:
            level = users_dict[user]['level']
        else:
            level = ''

        if 'score' in users_dict[user]:
            score = users_dict[user]['score']
        else:
            score = ''

        if 'taken_tutorial' in users_dict[user]:
            taken_tutorial = users_dict[user]['taken_tutorial']
        else:
            taken_tutorial = ''

        writer.writerow({
            'user': user ,
            'admin': admin ,
            'consent': consent ,
            'level': level ,
            'score': score ,
            'taken_tutorial': taken_tutorial
            })


# votes
with open('data\\votes_header.csv', 'r') as f:
    header = f.readline().split(',')

with open(votes_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for vote in votes_dict:
        writer.writerow({
            'vote': vote ,
            'response': votes_dict[vote]['response'] ,
            'sample': votes_dict[vote]['sample'] ,
            'time': votes_dict[vote]['time'] ,
            'user': votes_dict[vote]['user']
            })

