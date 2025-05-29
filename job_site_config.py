class JobSiteConfig:
    """Configuration for a job site (URL, CSS selectors)."""
    def __init__(self, url, css_selector, pagination_selector):
        self.url = url
        self.css_selector = css_selector
        self.pagination_selector = pagination_selector 