testcase_size = int(input())
from collections import Counter

for i in range(testcase_size):
    planet_count,c=list(map(int,input().split(' ')))
    planets = list(map(int,input().split(' ')))
    orbit_count = Counter(planets)
    cost = 0

    for orbit,planets_count in orbit_count.items():
        if(planets_count<=c):
            cost+=planets_count
        else:
            cost+=c
        
    print(cost)

