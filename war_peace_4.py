import math

target_word = "анна"
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
        if target_chapter == current_chapter:
            print(math.log(1 + chapter[target_word] / count) * math.log(chapter_count / df[target_word]))
        chapter, count = {}, 0
        current_chapter += 1
        continue
    if word not in chapter:
        chapter[word] = 1
    else:
        chapter[word] += 1
    count += 1