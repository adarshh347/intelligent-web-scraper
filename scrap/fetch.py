import asyncio
import json
import os
import requests
import inspect
from pydantic import BaseModel

from crawl4ai import LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

class Venue(BaseModel):
    name: str
    location: str
    price: str
    capacity: str
    rating: float
    reviews: int
    description: str

async def main():
    url = "https://example.com"

    # 1) Fetch + force UTF-8 (replace bad bytes)
    resp = requests.get(url, timeout=15)
    resp.encoding = 'utf-8'
    html = resp.text

    # 2) Configure the LLM extractor
    llm_strategy = LLMExtractionStrategy(
        llm_config=LLMConfig(
            provider="groq/llama3-70b-8192",
            api_token=os.getenv('GROQ_API_TOKEN')
        ),
        schema=Venue.model_json_schema(),
        extraction_type="schema",
        instruction=(
            "Extract all venue objects with 'name', 'location', 'price', "
            "'capacity', 'rating', 'reviews', and a 1 sentence description "
            "of the venue from the following HTML content."
        ),
        input_format="html",    # we’re feeding it HTML
        verbose=True,
    )

    # 3) Dynamically assemble the right kwargs for extract()
    sig = inspect.signature(llm_strategy.extract)
    params = list(sig.parameters.keys())[1:]  # skip “self”
    call_kwargs = {}
    for p in params:
        if p in ("ix", "index", "i"):
            call_kwargs[p] = 0
        elif p in ("html", "content", "text", "data"):
            call_kwargs[p] = html

    # 4) Call it!
    result = await llm_strategy.extract(**call_kwargs)
    if not result.success:
        print("Extraction failed:", result.error)
        return

    # 5) Parse & print
    data = json.loads(result.extracted_content)
    print("Extracted items:", data)

if __name__ == "__main__":
    asyncio.run(main())
