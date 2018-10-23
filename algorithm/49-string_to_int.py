
def strToInt(str):
    if str == None or str == '':
        return 0
    pos = 1
    num = 0
    for idx, char in enumerate(str):
        if char == '+' or char == '-':
            if idx == 0:
                pos = 1 if char == '+' else -1
            else:
                return 0
        elif char >= '0' and char <= '9':
            num = num * 10 + int(char)
        else:
            return 0
    return pos * num if num else 0

print(strToInt('12+12'))
print(strToInt('+1212'))
print(strToInt(''))