import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

from source_url import urls
from job_site_config import JobSiteConfig
from job_crawler import JobCrawler
from job_parser import JobParser
from job_deduplicator import JobDeduplicator
from job_exporter import JobExporter

async def main():
    all_jobs = []
    crawler = JobCrawler()
    parser = JobParser()
    for site_dict in urls:
        site = JobSiteConfig(site_dict["url"], site_dict["css_selector"], site_dict["pagination_selector"])
        jobs = await crawler.crawl_site(site, parser.process_page)
        all_jobs.extend(jobs)
    if all_jobs:
        JobExporter.export_to_excel(all_jobs)
    else:
        print("⚠️ Không có dữ liệu để export.")

if __name__ == "__main__":
    asyncio.run(main())