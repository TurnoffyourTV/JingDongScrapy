# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ID=scrapy.Field()
    image_url=scrapy.Field()
    image_path = scrapy.Field()
    image_category=scrapy.Field()

