import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.content_filter_strategy import LLMContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

# from base import groq_api_key, model_name
groq_api_key="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"
base_url1 = "https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"
base_url = "https://www.geeksforgeeks.org/dsa-tutorial-learn-data-structures-and-algorithms/"

async def main():
    browser_config=BrowserConfig(
            #  render_js=True,
        browser_type="chromium",
        headless=False,
        )
    filter = LLMContentFilter(
        llm_config=LLMConfig(
            provider="groq/llama3-70b-8192",
            api_token=groq_api_key,
        ),
        instruction="""
        Focus on extracting the below educational content.
        two pointers,
        sliding window,
        """,
        chunk_token_threshold=4096,  # Adjust based on your needs
        verbose=True
    )
    md_generator = DefaultMarkdownGenerator(content_filter=filter)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=base_url,
            config=CrawlerRunConfig(
                # content_filter=filter,
                markdown_generator=md_generator
            )
        )      

        print(result.markdown)  # Print clean markdown content
        print(result.media)


if __name__ == "__main__":
    asyncio.run(main())