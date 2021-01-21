from pathlib import Path
import scrapy
import tweepy

from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

base_prefix = "https://pbs.twimg.com/media/"
format_and_name = "?format=jpg&name=large"

def get_image_urls():
    url_list_post = []
    urls = Path(__file__).parent.parent.parent / 'user_input' / 'urls.txt'
    with urls.open(mode='r', newline='') as f:
        url_list_pre = f.readlines()
    for url in url_list_pre:
        # Strip whitespace (mainly the \n and \n newline)
        url = url.rstrip()
        # Transform mobile version of links
        url = url.replace("mobile.", "")
        url_list_post.append(url)
    return url_list_post

def get_urls():
    return ["https://google.com"]

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    start_urls = get_urls()

    def parse(self, response):
        tweet_urls = get_image_urls()
        id_list = []
        image_urls = []

        for tweet_url in tweet_urls:
            id_list.append(tweet_url.split('/')[-1])
        # print(id_list)
        tweets = api.statuses_lookup(id_=id_list, tweet_mode='extended')
        for tweet in tweets:
            print(tweet.id)
            media_array = tweet.extended_entities['media']
            # print(media_array)
            for media in media_array:
                url = media['media_url_https']
                base = ".".join(url.split('.')[:-1])
                image_url = base + format_and_name
                image_urls.append(image_url)
        # print(image_urls_test)

        # tweet_id = response.url.split('/')[-1]
        # for src in response.xpath('//div[has-class("AdaptiveMedia-photoContainer")]/img/@src').getall():
        #     base, extension = src.rsplit('.', 1)
        #     image_url = "{0}{1}{2}{3}".format(
        #         base,
        #         "?format=",
        #         extension,
        #         "&name=orig",
        #     )
        #     image_urls.append(image_url)
        yield {
            'image_urls': image_urls,
        }