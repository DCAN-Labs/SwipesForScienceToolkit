#! python3

import csv
import json
import os
import sys

database_json = os.path.abspath(sys.argv[1])
anonymized_json = database_json + '_anonymized'
sample_json =  database_json + '_samples'
users_json = database_json + '_users'


with open(database_json, 'r') as f:
    db = json.load(f)


del db['chats']
del db['settings']
del db['userSettings']


sample_lookup = {}
for i, sample in enumerate(db['sampleCounts']):
    anon_sample = 'sample_%06d' % i
    sample_lookup[sample] = anon_sample
    db['sampleCounts'][anon_sample] = db['sampleCounts'].pop(sample)


user_lookup = {}
for i, user in enumerate(db['users']):
    anon_user = 'user_%04d' % i
    user_lookup[user] = anon_user
    db['users'][anon_user] = db['users'].pop(user)


for sample in db['sampleSummary']:
    anon_sample = sample_lookup[sample]
    db['sampleSummary'][anon_sample] = db['sampleSummary'].pop(sample)


for user in db['userSeenSamples']:
    anon_user = user_lookup[user]
    db['userSeenSamples'][anon_user] = db['userSeenSamples'].pop(user)
    for sample in db['userSeenSamples'][anon_user]:
        anon_sample = sample_lookup[sample]
        db['userSeenSamples'][anon_user][anon_sample] = db['userSeenSamples'][anon_user].pop(sample)


for vote in db['votes']:
    sample = db['votes'][vote]['sample']
    user = db['votes'][vote]['user']
    db['votes'][vote]['sample'] = sample_lookup[sample]
    db['votes'][vote]['user'] = user_lookup[user]


with open(anonymized_json, 'w') as f:
    json.dump(db, f, indent=2)

with open(sample_json, 'w') as f:
    json.dump(sample_lookup, f, indent=2)

with open(users_json, 'w') as f:
    json.dump(user_lookup, f, indent=2)

