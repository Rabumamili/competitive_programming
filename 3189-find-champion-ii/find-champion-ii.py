class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for edge in edges:
            k, to_team = edge
            in_degree[to_team] += 1

        champions = [i for i, degree in enumerate(in_degree) if degree == 0]
        if len(champions) == 1:
            return champions[0]
        else:
            return -1