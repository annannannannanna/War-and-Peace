import math
from operator import itemgetter

target_chapter = 4

def read_data():
    data = open('war_peace_processed.txt', 'rt').read()
    return data.split('\n')

data = read_data()
df, chapter_count = {}, 0
chapter = {}

for word in data + ['[new chapter]']:
    if word == '[new chapter]':
        chapter = {}
        chapter_count += 1
        continue
    if word not in chapter:
        chapter[word] = 1
        df[word] = df.get(word, 0) + 1
    else:
        chapter[word] += 1
        
chapter, count, current_chapter = {}, 0, 0

for word in data + ['[new chapter]']:
    if word == '[new chapter]':
        if current_chapter == target_chapter:
            words = []
            for w in chapter:
                words.append((w, chapter[w], df[w], -math.log(1 + chapter[w] / count) * math.log(chapter_count / df[w])))
                #words.append((w, chapter[w], df[w], -chapter[w] / count * chapter_count / df[w]))
            words = sorted(words, key = itemgetter(3))
            print(' '.join([w[0] for w in words[:3]]))
        chapter, count = {}, 0
        current_chapter += 1
        continue
    if word not in chapter:
        chapter[word] = 1
    else:
        chapter[word] += 1
    count += 1