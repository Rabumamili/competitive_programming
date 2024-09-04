class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos
        
        total_cost = 0
        
        # Calculate the cost for moving vertically
        if start_row < home_row:
            total_cost += sum(rowCosts[start_row + 1 : home_row + 1])
        else:
            total_cost += sum(rowCosts[home_row : start_row])
        
        # Calculate the cost for moving horizontally
        if start_col < home_col:
            total_cost += sum(colCosts[start_col + 1 : home_col + 1])
        else:
            total_cost += sum(colCosts[home_col : start_col])
        
        return total_cost