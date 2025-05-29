# python file store url list with CSS selectors and pagination selectors for easy maintenance

urls = [
    {
        "url": "https://www.topcv.vn/tim-viec-lam-it-support-tai-binh-duong-kl3?sba=1&locations=l3",
        "css_selector": "div.job-item-info, div.box-job-info",  # TopCV job items
        "pagination_selector": "ul.pagination li a[rel='next']"
    },
    {
        "url": "https://careerviet.vn/viec-lam/it-support-tai-binh-duong-kl650-vi.html",
        "css_selector": "div.job-list-item, div.job-item-info",  # CareerViet job items
        "pagination_selector": "ul.pagination li.next a"
    },
    {
        "url": "https://www.vietnamworks.com/viec-lam?q=it-support&l=11",
        "css_selector": "div.job-item, div.job-search-result",  # VietnamWorks job items
        "pagination_selector": "a.page-link[rel='next'], li.next-page a"
    },
    {
        "url": "https://jobsgo.vn/viec-lam-it-support-tai-binh-duong.html",
        "css_selector": "div.job-item, div.job-card-inner",  # JobsGo job items
        "pagination_selector": "ul.pagination li:last-child:not(.disabled) a"
    },
    {
        "url": "https://www.jobstreet.vn/j?sp=search&trigger_source=serp&q=it+support&l=B%C3%ACnh+D%C6%B0%C6%A1ng",
        "css_selector": "article[data-job-id], div.sx2jih0.zcydq876._18qlyvc0._18qlyvc1x._18qlyvc1._1d0g9qk4",  # JobStreet job items
        "pagination_selector": "a[aria-label='Next']"
    },
    {
        "url": "https://www.google.com/search?q=vi%E1%BB%87c+l%C3%A0m+it+support+t%E1%BA%A1i+b%C3%ACnh+d%C6%B0%C6%A1ng&num=100",  # Set num=100 to get max results per page
        "css_selector": """
            div[class*='g']:not([class*='kno-kp']) div.yuRUbf, 
            div[class*='g']:not([class*='kno-kp']) div.tF2Cxc,
            div.MjjYud div[jscontroller],
            div[jsname='Cpkphb']
        """,  # Google search result items including lazy loaded content
        "pagination_selector": "a#pnnext, div[role='navigation'] a[aria-label*='Page']"
    }
]