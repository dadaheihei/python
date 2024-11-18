#切片
players=["yu","zhou","zhang","wang","luo","ma"]
print(players[0:3])   #这就是一个切片，代表了从第num1个元素开始直到第num2-1结束的片段（按照索引规律；来讲的第几个）
#也可以换一种方式
print(players[:3])
#遍历切片
for player  in players[1:5]:
    print(player)
#复制列表
#1.副本复制
copy_players=player[:]
copy_players.appened("yang")
print(players)
print(copy_players)
#2.名称复制    (自己起的名字) 就是让这个列表多一个名字而已
copy1_players=players
copy1_players.appened("yang")    #so这步操作之后，无论访问哪一个名字，都会得到修改后的列表
print(copy1_players)
print(players)    
