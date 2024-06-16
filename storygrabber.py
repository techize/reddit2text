import praw

CLIENT_ID     ="oNHJzla6tNZO3XjnxvLk3w'"
CLIENT_SECRET ="9IV8y93zTS9gMxIScs2DYRApbBNpvg"
USER_AGENT    ="script:storygrabber:v1.0 (by u/hedgehog72)"
USERNAME      ="hedgehog72"
PASSWORD      ="AlaRdOMenTAst"


# using the praw library, create a connection to reddit using the above client_id, client_secret, and user_agent

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD)

# # define a function that takes a URL and returns the textualized version of the post
# def textualize_post(URL):
#     submission = reddit.submission(url=URL)
#     post = submission.title + "\n\n" + submission.selftext
#     return post

# # test the function
# URL = 'https://www.reddit.com/r/AskReddit/comments/1by3p2o/whats_the_stupidest_animal_and_how_has_it/'
# output = textualize_post(URL)
# print(output)

print (reddit.read_only)
print (reddit.user.me())

# for submission in reddit.subreddit('AskReddit').hot(limit=10):
#     print(submission.title)