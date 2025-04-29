import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import csv
twitter_url = "https://x.com/TheCinesthetic/status/1917280532318114210"
youtube_url = "https://www.youtube.com/watch?v=Pirzg-F_aag"
harvard_url = "https://scholar.harvard.edu/binxuw/classes/machine-learning-scratch/materials/transformers"
async def main():

    async with AsyncWebCrawler(config=BrowserConfig()) as crawler:
        result = await crawler.arun(
            url=harvard_url,
            config=CrawlerRunConfig()
        )
        # print(result.links)
        web_links=result.links
        with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Link Type', 'URL'])
            for link_type, urls in web_links.items():
                for url in urls:
                    writer.writerow([link_type,url])         

        # print(result.markdown)  # Print clean markdown content
        # print(result.media)


if __name__ == "__main__":
    asyncio.run(main())
