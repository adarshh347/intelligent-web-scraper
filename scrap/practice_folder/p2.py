import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import csv
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter

harvard_url = "https://scholar.harvard.edu/binxuw/classes/machine-learning-scratch/materials/transformers"
base_url = "https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"

url_filter = URLPatternFilter(patterns=["wedding-vision   ", "atlanta/buckhead"])

async def extract_list():
    run_config= CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,
            include_external=False,
            max_pages=10,
            # filter_chain=FilterChain([url_filter])

        ),
        
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )
    browser_config=BrowserConfig(
            #  render_js=True,
             headless=False,
              executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        )
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(url=base_url, config=run_config)
        print(f"Crawler {len(results)} pages in total")
        return [
             {
                  "url":result.url,
                  "depth": result.metadata.get("depth", 0)

             }
             for result in results
        ]

# if __name__ == "__main__":
#         asyncio.run(main())

