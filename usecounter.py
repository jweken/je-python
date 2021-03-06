# Tally occurrences of words in a list
import re
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
cnt


# Find the ten most common words in Hamlet
words = re.findall(r'\w+', open('iliad_mb.txt').read())
findresult = Counter(words).most_common(1000)
#print(Counter(words).most_common(1000))
print(type(findresult))
print(findresult[980])
for key, value in findresult:
    if key[0].islower() and key[0] == 'o':
        print(key, value)
