def sub(c,x):
    list1=[]
    for i in c:
        list1.append(abs(i-x))
    return list1


def flatlandSpaceStations(n, c):
    station_distance={}
    space_station_list=[x for x in range(n)]

    for x in space_station_list:
        station_distance[x]=sub(c,x)
    list2=[]
    for key,val in station_distance.items():
        list2.append(min(val))
    print(max(list2))
# flatlandSpaceStations(5,[0,4])
flatlandSpaceStations(95,[68,81,46,54,30,11,19,23,22,12,38,91,48,75,26,86,29,83,62])