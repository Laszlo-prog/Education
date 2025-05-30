powers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

mini, maxi = 1, 20
for power in powers:
    if mini == 1 and maxi == 20:
        mini, maxi = powers[0], powers[0]
        print(mini, maxi)

    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
        print(mini, maxi)

