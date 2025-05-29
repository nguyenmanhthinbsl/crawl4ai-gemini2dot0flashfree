from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode
import asyncio

class JobCrawler:
    """Handles crawling and pagination for job sites."""
    def __init__(self, browser_config=None):
        self.browser_config = browser_config or BrowserConfig()

    async def get_pagination_urls(self, crawler, base_url, pagination_selector):
        pagination_urls = set([base_url])
        urls_to_process = [base_url]
        processed_urls = set()
        max_retries = 3
        delay_between_requests = 2  # seconds

        while urls_to_process:
            current_url = urls_to_process.pop(0)
            if current_url in processed_urls:
                continue
            for retry in range(max_retries):
                try:
                    run_config = CrawlerRunConfig(
                        only_text=False,
                        exclude_external_links=True,
                        remove_forms=True,
                        excluded_tags=["script", "style"],
                        cache_mode=CacheMode.BYPASS,
                        keep_attrs=["href"],
                        css_selector=pagination_selector
                    )
                    await asyncio.sleep(delay_between_requests)
                    result = await crawler.arun(url=current_url, config=run_config)
                    if not result.success:
                        print(f"Failed to crawl pagination for {current_url} - Attempt {retry + 1}/{max_retries}")
                        if retry < max_retries - 1:
                            continue
                        break
                    soup = BeautifulSoup(result.html, 'html.parser')
                    pagination_links = soup.select(pagination_selector)
                    for link in pagination_links:
                        href = link.get("href")
                        if not href:
                            continue
                        if href.startswith("/"):
                            from urllib.parse import urljoin
                            href = urljoin(current_url, href)
                        if href.startswith("#") or href in pagination_urls:
                            continue
                        from urllib.parse import urlparse
                        base_domain = urlparse(base_url).netloc
                        href_domain = urlparse(href).netloc
                        if base_domain != href_domain:
                            continue
                        pagination_urls.add(href)
                        urls_to_process.append(href)
                    processed_urls.add(current_url)
                    break
                except Exception as e:
                    print(f"Error processing pagination for {current_url} - Attempt {retry + 1}/{max_retries}: {str(e)}")
                    if retry < max_retries - 1:
                        await asyncio.sleep(delay_between_requests)
                    else:
                        processed_urls.add(current_url)
        return list(pagination_urls)

    async def crawl_site(self, site, process_page_func):
        all_jobs = []
        max_concurrent_tasks = 5
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            pagination_urls = await self.get_pagination_urls(crawler, site.url, site.pagination_selector)
            print(f"Found {len(pagination_urls)} pages for {site.url}")
            for i in range(0, len(pagination_urls), max_concurrent_tasks):
                chunk = pagination_urls[i:i + max_concurrent_tasks]
                tasks = [asyncio.create_task(process_page_func(crawler, page_url, site.css_selector)) for page_url in chunk]
                chunk_results = await asyncio.gather(*tasks, return_exceptions=True)
                for result in chunk_results:
                    if isinstance(result, Exception):
                        print(f"Error processing page: {str(result)}")
                    elif result:
                        if isinstance(result, list):
                            all_jobs.extend(result)
                        else:
                            all_jobs.append(result)
                await asyncio.sleep(2)
        return all_jobs 