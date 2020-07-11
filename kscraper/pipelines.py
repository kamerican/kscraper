# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class KscraperPipeline(object):
    def process_item(self, item, spider):
        urls_to_dl = item['image_urls']
        urls_dled = [image_dict['url'] for image_dict in item['images']]
        print("!---Scraped {0} image urls\n!---Downloaded {1} images".format(
            len(urls_to_dl),
            len(urls_dled),
        ))
        print("!---Could not download the following:")
        for url_to_dl in urls_to_dl:
            if url_to_dl not in urls_dled:
                print(url_to_dl)
        print("!---End of listing")
        # print(spider.start_urls)
        return item
