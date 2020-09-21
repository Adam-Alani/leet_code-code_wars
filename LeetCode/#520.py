def detectCapitalUse(word):
    if word.isupper() or word.islower() or word.istitle() :
        return True
    return False

print(detectCapitalUse("aAssda"))
