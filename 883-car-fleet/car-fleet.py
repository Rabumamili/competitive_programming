class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]
        
        fleets = 0
        while times:
            lead = times.pop(0)
            fleets += 1
            while times and times[0] <= lead:
                times.pop(0)
        
        return fleets