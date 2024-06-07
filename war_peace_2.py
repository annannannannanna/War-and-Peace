target_word = "человек"

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
        
print(df[target_word] / chapter_count)