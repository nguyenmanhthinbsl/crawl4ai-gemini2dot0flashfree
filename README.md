# crawl4ai-gemini

## Overview
`crawl4ai-gemini` is a project designed to facilitate web crawling and data extraction for AI-driven applications. It provides tools and utilities to efficiently gather and preprocess data from various online sources.

## Features
- **Customizable Crawling**: Define specific rules and targets for web crawling.
- **Data Preprocessing**: Clean and structure data for AI models.
- **Scalability**: Handle large-scale data extraction tasks.
- **Extensibility**: Easily integrate with other AI pipelines.

## Installation
Clone the repository:
```bash
git clone https://github.com/nguyenmanhthinbsl/crawl4ai-gemini
cd crawl4ai-gemini
```

## Requirement:
### Python3 
### pip3 


Install dependencies:
```bash
pip install -r requirements.txt 
# or using pip3
```

## Usage
1. Create your own api key

Create your gemini-2.0-flash api key for free at https://ai.google.dev/gemini-api/docs/api-key

2. Create and configure your environment crawling settings in the `.env` file.\n
    
    create .env file: 
    ```bash
    nano .env
    #or using ur favorite tools
    ```
    put your key in your environment file: 
    ```bash
    GEMINI_API_KEY="your key here"
    ```
3. Install requirements pagekage
    ```bash
    pip3 install -r requirements.txt
    ```
4. Run the crawler:
    ```bash
    python main.py 
    or 
    python3 main.py 
    ```