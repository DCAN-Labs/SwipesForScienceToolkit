# Swipe Data

Data dictionary

 - sampleCounts:
    - sample id: number of times swiped
 - sampleSummary:
    - aveVote: average swipe right (pass). Range between 0 (all fail) and 1 (all pass)
    - count: number of swipes
 - userSeenSamples
    - user id: dictionary of all samples that a user has swiped
        - sample id: 1 or 0 indicating pass or fail respectively
 - users: (This field can likely be ignored)
    - user id:
        - admin: If admin of site or not
        - consent: Whether or not they have agreed to the data use agreement consent form (should be true for all users)
        - level: What level badge they have achieved (correlated with number of swipes)
        - score: Number of images they have swiped
        - taken_tuorial: Whether or not the user has taken the tutorial (should be true for all users as it is required)
 - votes
    - random hash:
        - response: 1 = swipe right (pass), 2 = swipe left (fail)
        - sample: sample id
        - time: time spent on the image
        - user: user id that swiped