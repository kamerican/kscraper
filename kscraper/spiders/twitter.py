from pathlib import Path
import scrapy

def get_urls():
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

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    start_urls = get_urls()

    def parse(self, response):
        # follow links to author pages
        image_urls = []
        for src in response.xpath('//div[has-class("AdaptiveMedia-photoContainer")]/img/@src').getall():
            base, extension = src.rsplit('.', 1)
            image_url = "{0}{1}{2}{3}".format(
                base,
                "?format=",
                extension,
                "&name=orig",
            )
            image_urls.append(image_url)
        yield {
            'image_urls': image_urls,
        }