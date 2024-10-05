target_word = "князь"

def read_data():
    data = open('war_peace_processed.txt', 'rt').read()
    return data.split('\n')

data = read_data()

word_counts = {}

for word in data:
    word_counts[word] = word_counts.get(word, 0) + 1
    
print(word_counts[target_word])
