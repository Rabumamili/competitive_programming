class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
          
        players.sort()
        trainers.sort()
        num_matchings = 0
        i, j = 0, 0
        while i < len(players) and j <len(trainers):
            if players[i] <= trainers[j]:
                num_matchings += 1
                i += 1
            j += 1
        return num_matchings
