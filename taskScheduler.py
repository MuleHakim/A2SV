class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[value for value in Counter(tasks).values()]
        count = sorted(count)
        maxFreq=count.pop()
        room=maxFreq-1
        idle=(room)*n
        while count and idle > 0:
            idle -= min(room, count.pop())
        return max(0,idle)+len(tasks)
        
