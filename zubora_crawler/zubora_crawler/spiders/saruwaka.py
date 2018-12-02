import scrapy
from scrapy import Request

from zubora_crawler.items import RecipeItem


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
            ingredients.append({info[0]: info[1]})
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
        item['main_image'] =  response.xpath('//div[@class="post-thumbnail"]/img/@data-lazy-src').extract_first()

        yield item
