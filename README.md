# "War and Peace", by Leo Tolstoy
I took the text from the work from the library [lib.ru](http://http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml "lib.ru") and carried out the initial processing. The goal was to process the words from this work. I broke the text into individual words and output each one on a separate line. Additionally, in places where chapters begin, I added a line indicating the new chapter.

First, let's calculate the frequency of individual words used in the work. To do this, I will use a dictionary. I'm going to write a program that sorts all the words in the text and puts them in the dictionary. The counter will increase with each new word to keep track of how many times it occurs in the text.

The get method will help you find out which value corresponds to a specific key (word) in a dictionary. For example, words.get("word", 0) will either return a value from the dictionary or 0 if there is no such word in the dictionary yet.

The result will show the number of times the target word was found in the text. For example, if the target word is "**князь**", the answer will be 1,289.

**Document frequency** (df) is the percentage of documents in which a search word occurs. In this case, we are talking about the chapters of a book, not documents. Each chapter is separated by a line with the text "[new chapter]". Let's write a program that calculates the document frequency of a target word in the book.

The text consists of 171 chapters, and the word "человек" occurs in 115 of them (number_of_documents_with_target_word).
The df for the word "человек" is therefore 115/171 = 0.67251462

```python
def read_data():
    data = open('/Users/imac/Downloads/war_peace/war_peace_processed.txt', 'rt').read()
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
```


 calculate the frequency of a single word's use in a document (**term frequency**, or TF).
 
The easiest way to understand what term frequency (TF) is, is to use an example. TF of the word "война" can be defined as the number of times that the word "война" appears in the text of a chapter, divided by the total number of words in that chapter.

```python
def read_data():
    data = open('/Users/imac/Downloads/war_peace/war_peace_processed.txt', 'rt').read()
    return data.split('\n')

data = read_data()

word_counts = {}
for word in data:
    word_counts[word] = word_counts.get(word, 0) + 1
    
target_word = "князь"
print(word_counts[target_word])

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
```

Let's try to calculate the frequency of the word "гостья" in chapter 15. As a reminder, our chapters are numbered starting from 0. The word "гостья" occurs 10 times in this chapter, and there are a total of 1,359 words in the chapter.

The frequency of the word "гостья" in Chapter 15 is 101,359, which is equal to 0.007358351729213.
