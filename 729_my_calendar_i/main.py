from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.events = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        prev_event_index = self.events.bisect_right((start, end))

        if prev_event_index > 0 and self.events[prev_event_index - 1][1] > start:
            return False
        
        if prev_event_index < len(self.events) and self.events[prev_event_index][0] < end:
            return False
        
        self.events.add((start, end))
        return True


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
