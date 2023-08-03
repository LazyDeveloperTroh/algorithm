def solution(players, callings):
    playerMap = {} # player, rank
    rankMap = {} # rank, player
    for i in range(len(players)):
        rankMap[i] = players[i]
        playerMap[players[i]] = i
        
    for call in callings:
        print(playerMap[call])
        currentRank = int(playerMap[call])
        player = rankMap[currentRank-1]
        
        playerMap[player] = rankMap[currentRank]
        playerMap[call] = rankMap[currentRank-1]
    
    answer = list(playerMap.keys())
    return answer

solution(['a', 'b', 'c'], ['c', 'b'])