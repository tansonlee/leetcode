class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = [0 for _ in range(len(bank))]
        for i in range(len(bank)):
            for n in bank[i]:
                if n == "1":
                    devices[i] += 1

        result = 0    
        i = 0
        while i < len(devices):
            if devices[i] == 0:
                i += 1
                continue
            
            # find the next lazers
            nxt = i + 1
            while nxt < len(devices) and devices[nxt] == 0:
                nxt += 1
            if nxt == len(devices):
                break
            result += devices[i] * devices[nxt]
            i = nxt
        
        return result

        
