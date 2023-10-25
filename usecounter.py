# Tally occurrences of words in a list
import re
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
cnt

num = 1000
url = ".\\docs\\iliad_mb.txt"

# Find the ten most common words in Iliad


def MostCommonWords(url, num):
    words = re.findall(r'\w+', open(url).read())
    findresult = Counter(words).most_common(num)
    print(Counter(words).most_common(num))
    print()
    print("The type of findresult = ", type(findresult))
    if num > 988:
        print("Item 988 in the list = ", findresult[988])
    for key, value in findresult:
        if key[0].isupper() and key[0] == 'U':
            print(f"The name {key} has {value} occurrences.")


if __name__ == '__main__':
    MostCommonWords(url, 1000)
