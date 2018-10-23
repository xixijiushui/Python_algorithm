def firstNotRepeatingChar(str):
    if str == None:
        return -1

    memories = {}
    for char in str[:]:
        count = memories.get(char, 0)
        memories[char] = count + 1
    for char in str[:]:
        if memories[char] == 1:
            return char
    return -1

print(firstNotRepeatingChar('abcfabcf'))
print(firstNotRepeatingChar('acdadb'))
print(firstNotRepeatingChar(None))
print(firstNotRepeatingChar(''))