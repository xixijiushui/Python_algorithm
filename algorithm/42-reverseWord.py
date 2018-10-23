def reverseWords(str):
    arr = str.split(' ')
    arr.reverse()
    return ' '.join(arr)

print(reverseWords('I am a student.'))

def leftRotateString(s, n):
    if s == '':
        return s

    n = n % len(s)

    return s[n:] + s[:n]

print(leftRotateString('abcdefghijklmnopqrstuvwxyz', 3))