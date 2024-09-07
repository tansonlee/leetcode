class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Convert flower start and end to events that occur.
        events = []
        for start, end in flowers:
            events.append((start, 1))
            # Since the flower bloom is inclusive of the end time,
            # the flower really stops blooming 1 tick after the given end.
            events.append((end + 1, -1))
        events.sort()

        # Sort people by when they arrive but track their original
        # index for the result
        people = [(people[i], i) for i in range(len(people))]
        people.sort()

        result = [None for _ in range(len(people))]
        event_index = 0
        flower_count = 0
        for time, index in people:
            # Simulate up to the time that the person enters
            while event_index < len(events) and events[event_index][0] <= time:
                flower_count += events[event_index][1]
                event_index += 1
            
            result[index] = flower_count

        return result

