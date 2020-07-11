import tweepy
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
# import twitter

base_prefix = "https://pbs.twimg.com/media/"
format_and_name = "?format=jpg&name=large"

id_list = [
    1266713028315078657,
    1266741104759631872,
    1266784468548718597,
    1266842282478702597,
    1266842297187987456,
    1266842308609110016,
    1266864287345020928,
    1266927379647066112,
    1266927420478636032,
    1266924135906570241,
    1267070917693169666,
    1267063177751089152,
    1266660838225502208,
    1266720660455174144,
    1266654310193979392,
    1266654171010232320,
    1266654307748732928,
    1267116636286251010,
    1267116563494105090,
    1267116264234684416,
    1267116171519614977,
    1267135885897633793,
    1267136415906717697,
    1267131540439330818,
    1267131384797122560,
    1267309270749478912,
    1267262984163713025,
    1267500367719231489,
    1267500162617753602,
    1267407906426597378,
    1267424497654591490,
    1267683775661527040,
    1267844474803122176,
    1267788201931886593,
    1267788032217767937,
    1267787899556163586,
    1267787725618286592,
]


# twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,
#                   consumer_secret=CONSUMER_SECRET,
#                   access_token_key=ACCESS_TOKEN_KEY,
#                   access_token_secret=ACCESS_TOKEN_SECRET)
# tweets = twitter_api.GetStatuses(id_list)
# for tweet in tweets:
#     tweet_dict = tweet.AsDict()
#     if "media" in tweet_dict:
#         print("Media found")
#     else:
#         print("Media attribute not found in tweet id: {}".format(tweet.id))





auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)
tweets = tweepy_api.statuses_lookup(id_=id_list, tweet_mode='extended')
# print(tweets)
for tweet in tweets:
    
    if hasattr(tweet, 'extended_entities'):
        # print("Has extended_entities")
        media_array = tweet.extended_entities['media']
        # print(media_array)
        for media in media_array:
            url = media['media_url_https']
            base = ".".join(url.split('.')[:-1])
            image_url = base + format_and_name
            print(image_url)
    elif hasattr(tweet, 'entities'):
        # print("Has entities")
        # entities = tweet.entities
        # print(entities)
        if "media" in tweet.entities:
            print(tweet.entities['media'])
        else:
            print("Missing entities from: {} {}\n{}".format(
            tweet.user.screen_name,
            tweet.id_str,
            tweet,
        ))
    else:
        print("Missing entities from: {}".format(
            # tweet.user,
            tweet.id_str,
        ))
    
    # print(type(entities))
    # try:
    #     media_array = tweet.extended_entities['media']
    #     # print(media_array)
    #     for media in media_array:
    #         url = media['media_url_https']
    #         base = ".".join(url.split('.')[:-1])
    #         image_url = base + format_and_name
    #         # print(image_url)
    # except AttributeError:
    #     print(tweet.entities)
    #     media = tweet.entities['media']
    #     url = media['media_url_https']
    #     base = ".".join(url.split('.')[:-1])
    #     image_url = base + format_and_name
    



