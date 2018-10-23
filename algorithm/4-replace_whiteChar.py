import re
import time

def replace_whiteChar(str):
    start = time.time()
    new_str = str.replace(' ', '%20')
    end = time.time()
    print(end - start)
    start = time.time()
    new_str = re.sub(' ', '%20', str)
    end = time.time()
    print(end - start)
    return new_str

print(replace_whiteChar('We are happy.'))

