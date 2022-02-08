
def climbingLeaderboard(ranked, player):
    # Write your code here
    rank_table={}

    c=1
    for x in sorted(set(ranked),reverse=True):
        rank_table[c]=x
        c+=1
    for x in player:
        for y in rank_table:
            if x >=rank_table[y]:
                print(y,x)
                break
            if x<=rank_table[y]:
                c+=1
                rank_table[c]=x
                print(c)
        
    
    # print(rank_table)
climbingLeaderboard([100,90,90,80],[70,80,105])