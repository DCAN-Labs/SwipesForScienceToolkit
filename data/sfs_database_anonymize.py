#! /usr/bin/env python3

import csv
import json
import os
import re
import sys

database_json = os.path.abspath(sys.argv[1])
anonymized_json = database_json + '_anonymized'
sample_json = database_json + '_samples'
users_json = database_json + '_users'
subject_json = os.path.abspath('anonymized_subjects_map.json')


with open(database_json, 'r') as f:
    db = json.load(f)


del db['chats']
del db['settings']
del db['userSettings']


sample_lookup = {}
if os.path.exists(subject_json):
    with open(subject_json, 'r') as f:
        subject_lookup = json.load(f)
        subject_idx = len(subject_lookup)
else:
    subject_lookup = {}
    subject_idx = 0
sampleCounts = db['sampleCounts'].copy()
for sample in sampleCounts:
    splits = sample.split('_')
    for i, chunk in enumerate(splits):
        if 'NDARINV' in chunk:

            # create anonymous subject id and add to subject lookup dict
            if chunk not in subject_lookup.keys():
                subject_idx += 1
                anon_subject = 'subject_%06d' % subject_idx
                subject_lookup[chunk] = anon_subject
            else:
                anon_subject = subject_lookup[chunk]

            # replace subject id in sample name
            if i == 0:
                anon_sample = '_'.join([anon_subject] + splits[2:])
            else:
                anon_sample = '_'.join(['gold', anon_subject] + splits[3:])

            # replace
            sample_lookup[sample] = anon_sample
            db['sampleCounts'][anon_sample] = db['sampleCounts'].pop(sample)




user_lookup = {}
for i, user in enumerate(db['users']):
    anon_user = 'user_%04d' % i
    user_lookup[user] = anon_user

for user in user_lookup:
    anon_user = user_lookup[user]
    db['users'][anon_user] = db['users'].pop(user)


sampleSummary = db['sampleSummary'].copy()
for sample in sampleSummary:
    anon_sample = sample_lookup[sample]
    db['sampleSummary'][anon_sample] = db['sampleSummary'].pop(sample)


userSeenSamples = db['userSeenSamples'].copy()
for user in userSeenSamples:
    anon_user = user_lookup[user]
    db['userSeenSamples'][anon_user] = db['userSeenSamples'].pop(user)

    userSeenSamples_user = userSeenSamples[user].copy()
    for sample in userSeenSamples_user:
        anon_sample = sample_lookup[sample]
        db['userSeenSamples'][anon_user][anon_sample] = db['userSeenSamples'][anon_user].pop(sample)


votes = db['votes'].copy()
for vote in votes:
    try:
        sample = db['votes'][vote]['sample']
        user = db['votes'][vote]['user']

        db['votes'][vote]['sample'] = sample_lookup[sample]
        db['votes'][vote]['user'] = user_lookup[user]

    except:
        db['votes'].pop(vote)


with open(anonymized_json, 'w') as f:
    json.dump(db, f, sort_keys=True, indent=2)

with open(sample_json, 'w') as f:
    json.dump(sample_lookup, f, sort_keys=True, indent=2)

with open(users_json, 'w') as f:
    json.dump(user_lookup, f, sort_keys=True, indent=2)

with open(subject_json, 'w') as f:
    json.dump(subject_lookup, f, sort_keys=True, indent=2)

