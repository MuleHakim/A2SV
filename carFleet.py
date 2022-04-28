class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        times = [(target-p)/s for p,s in cars]
        fleet = 0
        if len(times)==1:
            fleet += 1
            return fleet
        while len(times) > 1:
            top = times.pop()
            if top < times[-1]:
                fleet += 1
            else:
                times[-1] = top
        return fleet + len(times)
