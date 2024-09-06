# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return url.split('/')[2]

        def helper(curr_url, hostname, visited):
            if get_hostname(curr_url) != hostname:
                return []
            
            if curr_url in visited:
                return []
            
            visited.add(curr_url)
            
            links = htmlParser.getUrls(curr_url)
            result = [curr_url]
            for l in links:
                result.extend(helper(l, hostname, visited))
            return result
        
        return helper(startUrl, get_hostname(startUrl), set())


        
