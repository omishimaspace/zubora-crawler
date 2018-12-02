# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

REQUIRED = (
    'name',
    'description',
    'original_url',
    'steps',
)


class RecipeItem(scrapy.Item):
    original_url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    kitchenware = scrapy.Field()
    ingredients = scrapy.Field()
    steps = scrapy.Field()
    elapsed_minutes = scrapy.Field()
    category = scrapy.Field()
    main_image = scrapy.Field()
