class UndergroundSystem:

    def __init__(self):
        self.times = {} # (station1, station2) -> [total, count]
        self.customer_check_in = {} # id -> (stationName, t)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.customer_check_in[id]
        
        if (check_in_station, stationName) not in self.times:
            self.times[(check_in_station, stationName)] = [0, 0]
        
        self.times[(check_in_station, stationName)][0] += (t - check_in_time)
        self.times[(check_in_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.times[(startStation, endStation)]
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
