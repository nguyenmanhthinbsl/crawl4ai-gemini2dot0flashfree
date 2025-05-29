# Crawl4AI Gemini Job Crawler

A modular, Python crawler for extracting job postings (with Gemini/Google Generative AI) from multiple Vietnamese job sites, exporting results to Excel with duplicate highlighting.

## Features
- Async crawling with pagination support
- Modular, maintainable codebase (SOLID principles)
- LLM-powered job info extraction (Google Gemini)
- Duplicate job detection and Excel highlighting
- Easy to add new job sites via configuration

## Project Structure
```
.
├── main.py                # Main orchestration script
├── job_site_config.py     # JobSiteConfig class (site config)
├── job_crawler.py         # JobCrawler class (crawling & pagination)
├── job_parser.py          # JobParser class (LLM extraction)
├── job_deduplicator.py    # JobDeduplicator class (duplicate detection)
├── job_exporter.py        # JobExporter class (Excel export)
├── source_url.py          # List of job site configs (urls, selectors)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
└── README.md              # This file
```

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup
Create a `.env` file in the project root with your Gemini/Google Generative AI API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```
- You may also use `GEMINI_API_KEY` for compatibility.

## Usage
Run the crawler:
```bash
python main.py
```
- The script will crawl all configured job sites, extract job info, and export results to an Excel file (with duplicate jobs highlighted).

## Adding/Editing Job Sites
Edit `source_url.py` to add or modify job site configurations:
```python
urls = [
    {
        "url": "https://example.com/jobs",
        "css_selector": "div.job-item",
        "pagination_selector": "a.next-page"
    },
    # ... more sites ...
]
```

## Output
- The output Excel file will be named like `jobs_data_YYYY-MM-DD_HH-MM.xlsx`.
- Duplicate jobs (same company & job title) are highlighted with colors and a legend.

## Requirements
See `requirements.txt` for all dependencies.

## Reference

- thank Crawl4AI for helpful opensource 
- If u interested, visit official repository here: 

## License
MIT (or your chosen license)