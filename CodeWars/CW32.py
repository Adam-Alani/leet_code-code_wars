def namelist(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    else:
        str = ''
        temp = []
        for i in range(0,len(names)-1): temp.append(names[i]['name'])
        str = ', '.join(temp)
        return str + ' & ' + names[-1]['name']


print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
