def removeSpace(word):
    return word.replace(" ","")

def anagramCheck(word1, word2):
    word1 = [*word1]
    word2 = [*word2]
    
    return (word1.sort() == word2.sort())

print(anagramCheck("sandeep","peednas"))
