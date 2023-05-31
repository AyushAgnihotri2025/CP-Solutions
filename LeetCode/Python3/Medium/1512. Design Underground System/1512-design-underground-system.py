class UndergroundSystem:

    def __init__(self):
        self.passengers = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        data = self.passengers.pop(id)
        start = data[0]
        startTime = data[1]
        tripTime = t - startTime
        key = (start + ', ' + stationName)
        if key not in self.passengers:
            self.passengers[key] = [tripTime, 1]
        else:
            self.passengers[key][0]+=tripTime
            self.passengers[key][1]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation + ', '+endStation)
        time, trips = self.passengers[key]
        return time/float(trips)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)