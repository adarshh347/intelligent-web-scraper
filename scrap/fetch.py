# myenv\Scripts\python.exe scrap\fetch.py
import asyncio
import json
import os
from crawl4ai import AsyncWebCrawler, BrowserConfig,CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
# async means “this function will run asynchronously” — it doesn’t block other code while waiting for slow operations like network requests.
# from scrap.venue import Venue
# from crawl4ai.llm_config import LLMConfig

from pydantic import BaseModel

class Venue(BaseModel):
    name: str
    location: str
    price: str
    capacity: str
    rating: float
    reviews: int
    description: str

async def main():
    llm_strategy = LLMExtractionStrategy(
        llm_config = LLMConfig(provider="groq/llama3-70b-8192", api_token=os.getenv('GROQ_API_TOKEN')),
        schema=Venue.model_json_schema(),
        extraction_type="schema",
        instruction=(
            "Extract all venue objects with 'name', 'location', 'price', 'capacity', "
            "'rating', 'reviews', and a 1 sentence description of the venue from the "
            "following content."
        ),
        input_format="markdown",
        verbose=True,
    )

    browser_conf = BrowserConfig(browser_type="chromium",headless=False)
    run_conf = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASSz
    )
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun( url="https://example.com"
                                    ,config=run_conf)
        # print(result)
        if result.success:
            data = json.loads(result.extracted_content)
            await asyncio.sleep(5)  
            print("Extracted items:",data)

    

if __name__ == "__main__":
    asyncio.run(main())