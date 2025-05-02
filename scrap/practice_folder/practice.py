import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import csv
import os

os.environ["PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH"] = r"C:\Program Files\Google\Chrome\Application\chrome.exe"



twitter_url = "https://x.com/TheCinesthetic/status/1917280532318114210"
youtube_url = "https://www.youtube.com/watch?v=Pirzg-F_aag"
base_url = "https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"

harvard_url = "https://scholar.harvard.edu/binxuw/classes/machine-learning-scratch/materials/transformers"

async def main():
    browser_config=BrowserConfig(
            #  render_js=True,
        browser_type="chromium",
        headless=False,
        
        )
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=base_url,
            config=CrawlerRunConfig()
        )
        # print(result.links)
        web_links=result.links
        # with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow(['Link Type', 'URL'])
        #     for link_type, urls in web_links.items():
        #         for url in urls:
        #             writer.writerow([link_type,url])         

        print(result.markdown)  # Print clean markdown content
        print(result.media)


if __name__ == "__main__":
    asyncio.run(main())
