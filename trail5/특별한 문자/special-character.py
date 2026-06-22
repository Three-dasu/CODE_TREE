str = input()

from collections import defaultdict
qwer = defaultdict(int)

for c in str:
    qwer[c] += 1

def myp():
    for c in qwer:
        if qwer[c] == 1:
            return c
    
    return 'None'

print(myp())

