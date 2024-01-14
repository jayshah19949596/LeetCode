"""
1242. Web Crawler Multithreaded [MEDIUM]
https://leetcode.com/problems/web-crawler-multithreaded/

### 1. Question:
----------------------------
Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links
that are under the same hostname as startUrl.

 ### 2. Solution:
----------------------------
Parallel BFS Algorithm using Multithreading
"""

import threading
import concurrent.futures
from collections import deque, defaultdict
from typing import List


class HtmlParser(object):
   def getUrls(self, url):
       return []


class Solution:
    hostname: str

    def __init__(self):
        self.lock = threading.Lock()

    def visit_neighbors(self, cur_url, nxt_level, visited, output, htmlParser):
        neighbor_urls = htmlParser.getUrls(cur_url)
        for neighbor_url in neighbor_urls:
            neighbor_hostname = neighbor_url.split("/")[2]
            if neighbor_url not in visited and neighbor_hostname == Solution.hostname:
                self.lock.acquire()
                visited.add(neighbor_url)
                self.lock.release()
                nxt_level.append(neighbor_url)
                output.append(neighbor_url)

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        Solution.hostname = startUrl.split("/")[2]
        threads, output = deque([]), [startUrl]
        cur_level, visited = deque([startUrl]), set([startUrl])

        while cur_level:
            nxt_level = deque([])
            for current_node in cur_level:
                thread = threading.Thread(target=self.visit_neighbors,
                                          args=(current_node, nxt_level, visited, output, htmlParser))
                thread.start()
                threads.append(thread)
            else:
                for thread in threads: thread.join()
            cur_level = nxt_level

        return output
