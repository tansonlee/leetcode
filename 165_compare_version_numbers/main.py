class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        for i in range(min(len(version1), len(version2))):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1
        
        if len(version1) < len(version2) and sum(version2[len(version1):]) > 0:
            return -1
        elif len(version1) > len(version2) and sum(version1[len(version2):]) > 0:
            return 1
        else:
            return 0
        
        
