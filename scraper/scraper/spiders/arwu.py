import scrapy

from scraper.items import UniItemLoader


class ArwuSpider(scrapy.Spider):
    name = "arwu"

    # Uncomment to see browser during crawl
    custom_settings = {
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            #"headless": False,
            #"slow_mo": 1000,
        }
    }


    def start_requests(self):
        yield scrapy.Request(
            url="https://www.shanghairanking.com/rankings/gras/2022/RS0210",
            meta={
                "playwright": True,
                "playwright_include_page": True,
            }
        )


    async def parse(self, response):
        page = response.meta["playwright_page"]

        async for uni in self.parse_page(page):
            yield uni

        next_button = page.locator(".ant-pagination-next:not([aria-disabled='true'])")
        while await next_button.count(): # While next page button is present and enabled
            await next_button.click()
            async for uni in self.parse_page(page):
                yield uni


    async def parse_page(self, page):
        names = await page.locator(".rk-table .univ-name").all_inner_texts()
        ranks = await page.locator(".rk-table .ranking").all_inner_texts()
        for name, rank in zip(names, ranks):
            loader = UniItemLoader()
            loader.add_value("name", name)
            loader.add_value("rank", rank)
            yield loader.load_item()
