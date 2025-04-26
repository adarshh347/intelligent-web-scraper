# myenv\Scripts\python.exe scrap\fetch.py
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig,CrawlerRunConfig, CacheMode
# async means “this function will run asynchronously” — it doesn’t block other code while waiting for slow operations like network requests.

async def main():
    browser_conf = BrowserConfig(browser_type="chromium",headless=False)
    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS
    )
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun( url="https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"
                                    ,config=run_conf)
        await asyncio.sleep(5)  
        print(result.markdown)

    

if __name__ == "__main__":
    asyncio.run(main())
