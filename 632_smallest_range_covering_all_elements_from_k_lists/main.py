class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Idea: merge the k sorted lists but in the process, determine the
        # smallest range.

        # During the process of merging the lists, the heap always contains
        # exactly 1 element from each list.

        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapify(heap)
        result = [-inf, inf]

        maximum = max(heap)[0]

        while heap:
            num, list_number, index = heappop(heap)
            minimum = num

            if (maximum - minimum < result[1] - result[0]) or \
                (maximum - minimum == result[1] - result[0] and minimum < result[0]):
                result = [minimum, maximum]

            if index + 1 >= len(nums[list_number]):
                # Done because now, one list won't be part of the heap
                break
            else:
                next_num = nums[list_number][index + 1]
                heappush(heap, (next_num, list_number, index + 1))
                maximum = max(maximum, next_num)
            
        
        return result

        # Notice that the heap always contains exactly 1 element from each list.
        # Second, 

        """
        # First, merge all of the sorted lists
        # and record which list each number came from
        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapify(heap)
        merged = []
        while heap:
            num, list_number, index = heappop(heap)
            merged.append((num, list_number))

            if index + 1 < len(nums[list_number]):
                heappush(heap, (nums[list_number][index + 1], list_number, index + 1))
        # Second, use a sliding window to find the smallest window that encompases
        # at least 1 number from each list
        result = [0, inf]
        left = 0
        right = 0
        counts = defaultdict(int)

        def covers_all(counts):
            for i in range(len(nums)):
                if counts[i] <= 0:
                    return False
            return True

        while right < len(merged):
            # Increment right until valid
            while right < len(merged) and not covers_all(counts):
                counts[merged[right][1]] += 1
                right += 1

            # Increment left until invalid
            while covers_all(counts):
                # See if this is the best so far
                best_range = result[1] - result[0]
                curr_range = merged[right - 1][0] - merged[left][0]
                if (curr_range < best_range) or (curr_range == best_range and merged[left][0] < result[0]):
                    result = [merged[left][0], merged[right - 1][0]]

                counts[merged[left][1]] -= 1
                left += 1

        return result
        """

        
