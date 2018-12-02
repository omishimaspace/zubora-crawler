import re

import scrapy
from scrapy import Request

from zubora_crawler.items import RecipeItem

UNITS = {
    (re.compile('(小さじ)(\d+[\d./〜~]*)?'), 2, 1),
    (re.compile('(大さじ)(\d+[\d./〜~]*)?'), 2, 1),
    (re.compile('(\d+[\d./〜~]*)?(cm)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(cc)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(パック)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(g)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(枚)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(振り)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(合)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(切れ)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(掴み)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(袋)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(束)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(つまみ)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(缶)'), 1, 2),
    (re.compile('([大小])?(\d+[\d./〜~]*)?(個)'), 2, 3),
    (re.compile('(\d+[\d./〜~]*)?(本)'), 1, 2),
    (re.compile('(\d+[\d./〜~]*)?(人[分前])'), 1, 2),
}


class SaruwakaSpider(scrapy.Spider):
    name = 'saruwaka'
    allowed_domains = ['saruwakakun.com']
    start_urls = ['http://saruwakakun.com/life/recipe/']

    def parse(self, response):
        urls = [url for url in response.xpath('//article/a/@href').extract()]
        for url in urls:
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = RecipeItem()
        item['original_url'] = response.url
        item['name'] = response.xpath('//title/text()').extract_first().strip()
        description = response.xpath('//header[@class="post-header"]/p/text()').extract_first()
        item['description'] = description.strip()
        ingredients = []
        for foodinfo in response.xpath('//div[@class="ingredients"]//div[@class="foodinfo"]'):
            info = [_ for _ in foodinfo.xpath('span/text()').extract()]
            ingredients.append({info[0]: divide(info[1])})
        item['ingredients'] = ingredients
        steps = []
        for step in response.xpath('//div[@class="cook_step"]//div[@class="card"]'):
            short_explain = step.xpath('.//p[@class="h3"]/text()').extract_first()
            explain = step.xpath('.//p[@class="explain"]/text()').extract_first()
            image = step.xpath('.//p[@class="stepimg"]/img/@data-lazy-src').extract_first()
            steps.append({
                'title': short_explain,
                'description': explain,
                'image': image,
            })
        item['steps'] = steps
        item['main_image'] = response.xpath(
            '//div[@class="post-thumbnail"]/img/@data-lazy-src').extract_first()

        yield item


def divide(duty_amount):
    clean_amount = duty_amount.replace('くらい', '').replace('約', '').replace('一', '1')
    amount, unit = match(clean_amount)
    return {
        'original': duty_amount,
        'amount': amount,
        'unit': unit,
    }


def match(amount_str):
    for unit in UNITS:
        m = unit[0].match(amount_str)
        if m:
            return m.group(unit[1]), m.group(unit[2])
    return None, None
