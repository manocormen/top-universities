import scrapy


class ArwuSpiderSpider(scrapy.Spider):
    name = 'arwu_spider'

    def start_requests(self):
        yield scrapy.Request(
            "https://www.shanghairanking.com/rankings/gras/2021/RS0210",
            meta=dict(
                playwright = True,
                playwright_include_page = True,
            )
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        last_page_number = int(await page.locator("li.ant-pagination-item >> nth=-1").inner_text())

        names = await page.locator("span.univ-name").all_inner_texts()
        ranks = await page.locator("div.ranking").all_inner_texts()
        for name, rank in zip(names, ranks):
            yield {"name": name, "rank": rank}

        for _ in range(last_page_number - 1):
            await page.click(".ant-pagination-next")
            names = await page.locator("span.univ-name").all_inner_texts()
            ranks = await page.locator("div.ranking").all_inner_texts()
            for name, rank in zip(names, ranks):
                yield {"name": name, "rank": rank}