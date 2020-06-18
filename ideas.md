# These are ideas

## For analysis/visualizations

For all ratings provided by citizen scientist ABC, how reliably does ABC vote compared to the gold standard data?  (How raters do versus gold standard/ground truth rated data?)

- threshold for frequency of agreement with gold standard
- percentage match with gold standard rating
    - One percentage score for each user overall; OR
    - Frequency of match on pass vs match on fail
    - The same could be done with vote consensus instead of ground truth
- Percentage of Type I errors vs Type II errors

Among all citizen scientists, who are the best raters?  How well are reviewers doing?  Some metrics would be good.

- highest agreement with gold standard ratings
    - ranking
- cutoff for top 5 or top 10 percent of raters
    - could use different rating metrics:
        - Number of votes (Leaderboard)
        - Percent of gold standard matches
        - Percent of consensus agreement
- consistency, a.k.a. seeing the same sample more than once and voting the same or different (not quite inter-rater reliability)
    - would require multiple views of same samples
- frequency of swiping left vs right
    - scatter plot?
    - two bin histogram
- time taken to swipe images (a distribution)
    - historam?

What is the inter-rater reliability on image XYZ?

- https://en.wikipedia.org/wiki/Cohen%27s_kappa

Of this set, are you getting worse quality images from a specific age range?

- would require subject demographics

What scans or scan types are getting worse or better ratings?

- average score or some other metric would reveal quality of ratings

Are certain users "super-users"?

- This might mean a lot of ratings (swipes)
- This could also mean the disctirbution of scores being given
- The distribution of times spent per image

For all the images associated with one subject's data, should that entire subject be considered a Pass or Fail for inclusion in further analysis?

- weighted average of datatype and frequency of being rated

How can we use deep learning to align crowd sourced QC data with gold standard expert evaluation?

- following Anisha's paper or coming up with own methods

## Code improvements to change how data is presented to users

What about having these scans go through different "check points"?  If a scan has at least 100 good swipes and at least a 66% swipe right frequency, then this subject's image can be sent to a more "reliable" QC-er.

- test QC-ers against non-experts
- This idea is also a coding improvement idea to present more "questionable" samples to more experienced or expert users
- Experts assigned more questionable scans, maybe...

First focus on scans where consensus is good, then questionable, then worse ones

When people spent more time looking at the image, present it more often

Weighted averages per user

Two QC ideas:

1. 2D slices in a GIF animation or a 3rd dimension slider
2. BrainSprite 3D images (orthogonal "browse-able" view) that you can pass or fail
