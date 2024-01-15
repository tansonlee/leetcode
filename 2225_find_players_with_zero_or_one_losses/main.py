class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}

        for winner, loser in matches:
            if winner not in players:
                players[winner] = [0, 0]
            if loser not in players:
                players[loser] = [0, 0]
            
            players[winner][0] += 1
            players[loser][1] += 1
        
        no_loss = []
        for p in players:
            if players[p][1] == 0:
                no_loss.append(p)
        one_loss = []
        for p in players:
            if players[p][1] == 1:
                one_loss.append(p)
        
        no_loss.sort()
        one_loss.sort()
        return [no_loss, one_loss]

        
