import re
from collections import defaultdict
from typing import List, Dict, Any

class JobDeduplicator:
    """Handles duplicate job detection."""
    @staticmethod
    def find_duplicate_jobs(jobs: List[Dict[str, Any]]):
        job_groups = defaultdict(list)
        for i, job in enumerate(jobs):
            company = job.get("companyname - Tên Công ty", "").lower().strip()
            title = job.get("jobname - Tên công việc", "").lower().strip()
            clean_company = re.sub(r'[^\w\s]', '', company)
            clean_title = re.sub(r'[^\w\s]', '', title)
            key = f"{clean_company}_{clean_title}"
            job_groups[key].append(i)
        return {key: indices for key, indices in job_groups.items() if len(indices) > 1} 