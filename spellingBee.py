import json

with open('websters_dictionary.json') as dic:
    data = dic.read()

    data = json.loads(data)

words = list(data.keys())
words.sort()

# parse out words less than 4 letters
words = [word for word in words if len(word) >= 4]

BEE = ['r', 'a', 'f', 'l', 'o', 'u', 'v']
MIDDLE = 0
potential_words = []

words = set(words)

for word in words:
    if BEE[MIDDLE] not in word:
        continue

    # We don't want leftovers
    leftovers = set(word).difference(set(BEE))
    if len(leftovers) == 0:
        potential_words += [word]

words = set(potential_words)

