def disemvowel(string):
    vowels = 'aeiouAEIOU'
    newstring = string
    for char in vowels:
        newstring = newstring.replace(char, '')
    return(newstring)









print(disemvowel('This website is for losers LOL!'))
