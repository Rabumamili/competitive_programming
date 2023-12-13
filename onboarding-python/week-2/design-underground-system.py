# class UndergroundSystem:

    # def __init__(self):
    #     self.checkinmap = {} # id..> (startstation, time)
    #     self.totalmap ={}   # (start, end) -->[totaltime, count]

        

    # def checkIn(self, id: int, stationName: str, t: int) -> None:
    #     self.checkinmap[id] =(stationName, t)
        

    # def checkOut(self, id: int, endstation: str, t: int) -> None:
    #     start, time = self.checkinmap[id]
    #     route = (start, endstation)
    #     if route not in self.totalmap:
    #         self.totalmap[route]= [0,0]
    #     self.totalmap[route][0] += t -time
    #     self.totalmap[route][1] +=1

class UndergroundSystem:
    def __init__(self):
        self.checkinmap = {}  # Stores check-in information for each id: {id -> (startstation, time)}
        self.totalmap = {}    # Stores total time and count for each route: {(start, end) -> [totaltime, count]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinmap[id] = (stationName, t)  # Save check-in information for the id

    def checkOut(self, id: int, endstation: str, t: int) -> None:
        start, time = self.checkinmap.pop(id)    
        route = (start, endstation)               

        # Update the total time and count for the route
        total, count = self.totalmap.get(route, (0, 0))  
        self.totalmap[route] = (total + t - time, count + 1)  # Update total time and count for the route

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalmap.get((startStation, endStation), (0, 0))   
        return total / count if count > 0 else 0.0  
    # def getAverageTime(self, startStation: str, endStation: str) -> float:
    #     total, count = self.totalmap[(startStation, endStation)]
    #     return total/count

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)