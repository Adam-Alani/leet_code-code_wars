def is_valid_walk(walk):
    north = south = west = east = 0
    c = len(walk)
    if c != 10:
        return False
    for i in walk:
        if i == 'n': north += 1
        if i == 's': south += 1
        if i == 'w': west += 1
        if i == 'e': east += 1
    if north - south != 0 or west - east != 0: return False
    else: return True







print(is_valid_walk(['w', 'e', 's', 'w', 'e', 'e', 'w', 'n', 'e', 'w']))
