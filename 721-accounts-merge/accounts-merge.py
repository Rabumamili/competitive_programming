class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name
    
        seen = set()
        def dfs(email):
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                if node not in seen:
                    seen.add(node)
                    component.append(node)
                    stack.extend(graph[node])
            return component
 
        ans = []
        for email in email_to_name:
            if email not in seen:
                component = dfs(email)
                ans.append([email_to_name[email]] + sorted(component))

        return ans