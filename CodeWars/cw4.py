def maskify(cc):
    string = str(cc)
    numbers = str('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    string = '#'*(len(numbers) - 4)+numbers[-4:]
    return(string)
    print(string)







print(maskify('123456925'))