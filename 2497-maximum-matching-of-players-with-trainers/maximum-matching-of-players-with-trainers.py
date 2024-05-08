class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
          
        players.sort()
        trainers.sort()
        count = 0
        j = 0 
        for i in range(len(players)):
        
            while j < len(trainers):
                if players[i] <= trainers[j]:
                    trainers[j] = 0
                    count +=1
                    break
                j += 1
        return count