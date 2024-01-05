class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # return [[[["Push", "Pop"]]] for i in range(1, target[0])] + [[["Push"]]] + [[["Push", "Pop"] for j in range(target[i]+1, target[i+1])] + [["Push"]] for i in range(len(target) - 1)]
        return [subsubitem for item in [[["Push", "Pop"]] for i in range(1, target[0])] + [[["Push"]]] + [[["Push", "Pop"] for j in range(target[i]+1, target[i+1])] + [["Push"]] for i in range(len(target) - 1)] for subitem in item for subsubitem in subitem]
        # result = []

        # for i in range(1, target[0]):
        #     result.append("Push")
        #     result.append("Pop")
        # result.append("Push")

        # for i in range(len(target) - 1):
        #     for j in range(target[i] + 1, target[i + 1]):
        #         result.append("Push")
        #         result.append("Pop")
        #     result.append("Push")
        

        # return result

