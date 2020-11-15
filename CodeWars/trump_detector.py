def trump_detector(trump_speech):
    trump_speech = trump_speech.lower()
    trumpVowel = 0
    vowels = "aeiou"
    if trump_speech[0] in vowels:
        vowelCount = 1
    else:
        vowelCount = 0
    for i in range(1, len(trump_speech)):
        if trump_speech[i-1] != trump_speech[i] and trump_speech[i] in vowels :
            vowelCount += 1
        if trump_speech[i-1] in vowels and trump_speech[i] == trump_speech[i-1]:
            trumpVowel += 1
    return(round(trumpVowel/vowelCount , 2))




print(trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa"))

def disemvowel(string):
    vowels = 'aeiouAEIOU'
    newstring = string
    for char in vowels:
        newstring = newstring.replace(char, '')
    return(newstring)
