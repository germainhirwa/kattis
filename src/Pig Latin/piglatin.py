def process(word):
    if word[0] in 'aeiouy': return word + 'yay'
    else:
        while word[0] not in 'aeiouy': word = word[1:] + word[0]
        return word + 'ay'

import sys
for l in sys.stdin: print(' '.join(map(process, l.strip().split())))