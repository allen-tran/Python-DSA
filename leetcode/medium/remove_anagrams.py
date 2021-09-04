'''
Amazon variation of group anagrams
'''

def remove(strs):
    setList = set()
    result = []
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in setList:
            setList.add(sortedWord)
            result.append(word)
            
    return result