# Swipe Data

## Data dictionary

 - sampleCounts:
    - sample id: number of times swiped
 - sampleSummary:
    - aveVote: average swipe right (pass). Range between 0 (all fail) and 1 (all pass)
    - count: number of swipes
 - userSeenSamples
    - user id: dictionary of all samples that a user has swiped
        - sample id: count of times sample was seen
 - users: (This field can likely be ignored)
    - user id:
        - admin: If admin of site or not
        - consent: Whether or not they have agreed to the data use agreement consent form (should be true for all users)
        - level: What level badge they have achieved (correlated with number of swipes)
        - score: Number of images they have swiped
        - taken_tuorial: Whether or not the user has taken the tutorial (should be true for all users as it is required)
 - votes
    - random hash:
        - response: 1 = swipe right (pass), 0 = swipe left (fail)
        - sample: sample id
        - time: time spent on the image
        - user: user id that swiped

## Database similarities and differences

1. db-func_to_t1_reg

   - This is the largest
   - this has the biggest counts of images per subject, but images are very similar

2. db-surfaces

   - This is the mid-size
   - this has the widest variety of images per subject

3. db-t1_to_atlas_reg

   - This is the smallest
   - there are only two images per subject (atlas to t1 OR t1 to atlas registration)
