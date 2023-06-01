class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        player=0
        trainer=0
        match=0
        players.sort()
        trainers.sort()
        while player<len(players) and trainer<len(trainers):
            print(player, trainer)
            if players[player]<=trainers[trainer]:
                match+=1
                player+=1
                trainer+=1
            else:
                trainer+=1
        return match

        