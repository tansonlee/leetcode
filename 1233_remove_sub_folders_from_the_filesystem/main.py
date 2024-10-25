class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def sub_folder(f1, f2):
            f1s = f1.split("/")
            f2s = f2.split("/")
            return f2s[:len(f1s)] == f1s
        folder.sort()

        result = []
        i = 0
        while i < len(folder):
            match = folder[i]
            result.append(match)
            i += 1
            while i < len(folder) and sub_folder(match, folder[i]):
                i += 1
            
        return result
        
