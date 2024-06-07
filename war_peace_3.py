target_word = "гостья"
target_chapter = 15

def read_data():
    data = open('war_peace_processed.txt', 'rt').read()
    return data.split('\n')

data = read_data()
chapter, count, chapter_count = {}, 0, 0

for word in data + ['[new chapter]']:
    if word == '[new chapter]':
        if chapter_count == target_chapter:
            print(chapter[target_word] / count)
        chapter, count = {}, 0
        chapter_count += 1
        continue
    if word not in chapter:
        chapter[word] = 1
    else:
        chapter[word] += 1
    count += 1