import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        room_ends = [(-1, i) for i in range(n)]
        used_counts = [0 for _ in range(n)]

        for start, end in meetings:
            if room_ends[0][0] > start:
                # Pick the one with the earliest ending time.
                end_time, room_number = heapq.heappop(room_ends)
                used_counts[room_number] += 1
                next_meeting = (end + (end_time - start), room_number)
                heapq.heappush(room_ends, next_meeting)
            else:
                # There could be multiplle rooms open so pick the one with the lowest room number.
                available_rooms = []
                while len(room_ends) > 0 and room_ends[0][0] <= start:
                    available_rooms.append(room_ends[0])
                    heapq.heappop(room_ends)
                lowest = 0
                for i in range(len(available_rooms)):
                    if available_rooms[i][1] < available_rooms[lowest][1]:
                        lowest = i

                used_counts[available_rooms[lowest][1]] += 1
                next_meeting = (end, available_rooms[lowest][1])
                heapq.heappush(room_ends, next_meeting)
                for i in range(len(available_rooms)):
                    if i != lowest:
                        heapq.heappush(room_ends, available_rooms[i])
        
        max_index = 0
        for i in range(len(used_counts)):
            if used_counts[i] > used_counts[max_index]:
                max_index = i
        
        return max_index
        
