players = [29, 58, 66, 71, 87]
print(players[2])
#66

players[2] = 68
print(players)
#[29, 58, 68, 71, 87]

print(players + [90, 91, 98])
#[29, 58, 68, 71, 87, 90, 91, 98]
print(players)
#[29, 58, 68, 71, 87]

players.append(120)
print( players)
#[29, 58, 68, 71, 87, 120]

print(players[:2])
#[29, 58]

players[:2] = [0, 0]
print(players)
#[0, 0, 68, 71, 87, 120]

players[:2] = []
print(players)
#[68, 71, 87, 120]

players[:] = []
print(players)
#[]