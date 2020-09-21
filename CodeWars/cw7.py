def number(bus_stops):
    total_on,total_off= 0,0
    for i in bus_stops:
        total_on += i[0]
        total_off += i[1]
    return(total_on - total_off)






print((number([[10,0],[3,5],[5,8]])))