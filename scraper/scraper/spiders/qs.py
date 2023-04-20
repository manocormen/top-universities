import scrapy


class QsSpider(scrapy.Spider):
    name = "qs"
    allowed_domains = ["www.topuniversities.com"]
    start_urls = ["https://www.topuniversities.com/rankings/endpoint?nid=3846233&page=0&items_per_page=700&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by="]

    def parse(self, response):
        ranking = response.json()["score_nodes"]
        for uni in ranking:
            yield {
                "name": uni["title"],
                "rank": int(uni["rank"]),
            }
