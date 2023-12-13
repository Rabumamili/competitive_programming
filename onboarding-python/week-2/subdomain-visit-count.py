class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
     
        mp = defaultdict(int)
        
        for domain in cpdomains:
            count, full_domain = domain.split()
            count = int(count)
            subdomains = full_domain.split('.')
            
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                mp[subdomain] += count
        
        result = [f"{count} {domain}" for domain, count in mp.items()]
        return result