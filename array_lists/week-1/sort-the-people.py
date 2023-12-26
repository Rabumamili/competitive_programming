class Solution(object):
    def sortPeople(self, names, heights):
        dic ={heights[i]: names[i] for i in range (len(names))}
        for i in range(len(heights)-1):
            for j in range(len(heights)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
            
        for i in range(len(heights)):
            names[i] = dic[heights[i]]
        return names
