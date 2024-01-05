class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = 0
        locs = set()
        locs.add(curr)

        for d in path:
            if d == "N":
                curr += 1j
            elif d == "S":
                curr -= 1j
            elif d == "E":
                curr += 1
            elif d == "W":
                curr -= 1
            else:
                print("BAD")
            locs.add(curr)
        print(locs)
        return len(path) + 1 != len(locs)

        
