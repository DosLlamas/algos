def played_teams(teams):
    if teams == 2:
       return 0
    power = 2
    while power <= 1000000:
        if power == teams:
            return 0
        if power * 2 > teams:
            d = teams - power
            return d * 2
        power *= 2
n = int(input())
print(played_teams(n))