# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

REQUIRED = (
    'title',
    'description',
    'original_url',
)


class RecipeItem(scrapy.Item):
    original_url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    kitchenware = scrapy.Field()
    ingredients = scrapy.Field()
    steps = scrapy.Field()
