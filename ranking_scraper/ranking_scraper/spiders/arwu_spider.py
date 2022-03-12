import scrapy

from ranking_scraper.settings import ranking_urls


class ArwuSpiderSpider(scrapy.Spider):
    name = 'arwu_spider'

    def start_requests(self):
        yield scrapy.Request(
            ranking_urls[2],
            meta=dict(
                playwright = True,
                playwright_include_page = True,
            )
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        last_page_number = int(await page.locator("li.ant-pagination-item >> nth=-1").inner_text())

        async for item in self.parse_page(page):
            yield item

        for _ in range(last_page_number - 1):
            await page.click(".ant-pagination-next")  # Go to next page in ranking
            async for item in self.parse_page(page):
                yield item
    
    async def parse_page(self, page):
        names = await page.locator("span.univ-name").all_inner_texts()
        ranks = await page.locator("div.ranking").all_inner_texts()
        for name, rank in zip(names, ranks):
            yield {"name": name, "rank": rank}