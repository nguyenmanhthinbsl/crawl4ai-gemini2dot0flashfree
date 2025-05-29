import os
import re
import json
import time
import sys
import google.generativeai as genai
from bs4 import BeautifulSoup
from crawl4ai.async_configs import CrawlerRunConfig, CacheMode
from dotenv import load_dotenv
from notify import NOTIFY

class JobParser:

    """Load environment variables from .env file."""
    load_dotenv()

    """Handles parsing and LLM extraction for job info."""
    @staticmethod
    async def process_gemini_response(response_text):
        pattern = r'```(?:json)?\s*(.*?)```'
        match = re.search(pattern, response_text, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
            try:
                json_data = json.loads(json_text)
                return json_data
            except json.JSONDecodeError as e:
                print(NOTIFY["json_parse_error"].format(error=e))
                return None
        else:
            try:
                json_data = json.loads(response_text.strip())
                return json_data
            except json.JSONDecodeError:
                print(NOTIFY["json_extract_error"])
                return None

    @staticmethod
    def load_prompt():
        with open("job_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    async def get_job_info(data, url):
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        if not api_key:
            print(NOTIFY["no_api_key"])
            sys.exit(1)
        genai.configure(api_key=api_key)
        # Check if API key is right by making a test API call
        try:
            _ = genai.GenerativeModel("gemini-2.0-flash").generate_content("ping")
        except Exception as e:
            print(NOTIFY["invalid_api_key"].format(error=e))
            sys.exit(1)
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt_template = JobParser.load_prompt()
        prompt = prompt_template.format(url=url, data=data)
        time.sleep(2)
        response = model.generate_content(prompt)
        return await JobParser.process_gemini_response(response.text)

    @staticmethod
    async def process_page(crawler, page_url, css_selector):
        try:
            run_config = CrawlerRunConfig(
                only_text=False,
                exclude_external_links=True,
                remove_forms=True,
                excluded_tags=["script", "style"],
                cache_mode=CacheMode.BYPASS,
                keep_attrs=["src", "class", "href", "jscontroller", "jsname", "data-ved"],
                css_selector=css_selector
            )
            result = await crawler.arun(url=page_url, config=run_config)
            if not result.success:
                print(NOTIFY["crawl_failed"].format(url=page_url))
                return None
            soup = BeautifulSoup(result.html, 'html.parser')
            job_elements = soup.select(css_selector)
            job_content = "\n".join([elem.get_text(strip=True) for elem in job_elements])
            return await JobParser.get_job_info(job_content, page_url)
        except Exception as e:
            print(NOTIFY["page_process_error"].format(url=page_url, error=e))
            return None 