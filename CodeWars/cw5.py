def openOrSenior(data):
    league = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            league.append("Senior")
        else:
            league.append("Open")
    return(league)












print(openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))