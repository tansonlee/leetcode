class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for x in cpdomains:
            count, domain = x.split(" ")
            count = int(count)

            domains = domain.split(".")

            for i in range(len(domains)):
                counts[".".join(domains[i:])] += count
        
        result = []
        for d in counts:
            result.append(f"{counts[d]} {d}")
        
        return result

        
