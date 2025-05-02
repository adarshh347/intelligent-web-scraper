from p2 import extract_list
import gradio as gr
import sys
import os
import asyncio

def display_results():
    results=asyncio.run(extract_list())
    formatted = "\n".join([f"Depth {r['depth']}->{r['url']}" for r in results])
    return formatted

demo = gr.Interface(
    fn=display_results,
    inputs=[],
    outputs="text",
    title="Wedding Venue Crawler",
    description="Crawls wedding venue URLs from TheKnot and displays their depth in the crawl."
)
if __name__ == "__main__":
    demo.launch(debug=True, share=True)
