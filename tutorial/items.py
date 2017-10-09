# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    time = scrapy.Field()
    mileage = scrapy.Field()
    place = scrapy.Field()
    price = scrapy.Field()
    new_car_price = scrapy.Field()
    tag = scrapy.Field()
    pic = scrapy.Field()
    url = scrapy.Field()

