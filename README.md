# "War and Peace", by Leo Tolstoy
I took the text from the work from the library [lib.ru](http://http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml) and carried out the initial processing. The goal was to process the words from this work. I broke the text into individual words and output each one on a separate line. Additionally, in places where chapters begin, I added a line indicating the new chapter.

First, let's calculate the frequency of individual words used in the work. To do this, I will use a dictionary. I'm going to write a program that sorts all the words in the text and puts them in the dictionary. The counter will increase with each new word to keep track of how many times it occurs in the text.

The get method will help you find out which value corresponds to a specific key (word) in a dictionary. For example, words.get("word", 0) will either return a value from the dictionary or 0 if there is no such word in the dictionary yet.

The result will show the number of times the target word was found in the text. For example, if the target word is "**князь**", the answer will be 1,289.

[war_peace_1.py](http://https://github.com/annannannannanna/War-and-Peace/blob/main/war_peace_1.py)

**Document frequency** (df) is the percentage of documents in which a search word occurs. In this case, we are talking about the chapters of a book, not documents. Each chapter is separated by a line with the text "[new chapter]". Let's write a program that calculates the "document frequency" of a "target word" in the book.

You can calculate the document frequency (df) using the following formula:

"number of documents with target word"/ "total number of documents"

- "total number of documents" is the total number of chapters
- "number of documents with target word" is the number of times the "target word" occurs in the chapters.

The text consists of 171 chapters, and the word "человек" occurs in 115 of them (number_of_documents_with_target_word).

The df for the word "человек" is therefore 115/171 = 0.67251462


[war_peace_2.py](http://https://github.com/annannannannanna/War-and-Peace/blob/52e407294c03df284220d13d53f24c89996ab01f/war_peace_2.py)


 calculate the frequency of a single word's use in a document (**term frequency**, or tf).
 
The easiest way to understand what term frequency (tf) is, is to use an example. 

tf of the word "война" can be defined as the number of times that the word "война" appears in the text of a chapter, divided by the total number of words in that chapter.

Let's try to calculate the frequency of the word "гостья" in chapter 15. As a reminder, our chapters are numbered starting from 0. The word "гостья" occurs 10 times in this chapter, and there are a total of 1,359 words in the chapter.

The frequency of the word "гостья" in chapter 15 is 101,359, which is equal to 0.007358351729213.

Let's write a program to calculate the frequency of a given word "target_word" in a specific chapter "target_chapter"

[war_peace_3.py](http://https://github.com/annannannannanna/War-and-Peace/blob/52e407294c03df284220d13d53f24c89996ab01f/war_peace_3.py)

If a word is frequently used in a text, it is likely that the text is about the subject or action described by that word. For instance, if a book uses the word "cat" repeatedly, it is probably about these animals. 

However, the word "and" may appear in almost every text, so it may not be useful to include it in our analysis. Therefore, when analyzing a text for significant words, we need to consider both the frequency of words and their relevance to the subject matter. We want to identify the most common words, but also exclude those that are not informative because they are used so often.

This task can be solved effectively using tf * idf, a statistical measure for assessing the significance of a word in a text. To put it simply, tf * idf is a measure of how unique a word is in a document compared to other words. 

It is calculated as the product of two factors: term frequency (tf) and inverse document frequency (idf). 

Term frequency (tf) measures how often a word occurs in a document, while inverse document frequency (idf) measures the importance of a word across all documents in a collection.

To calculate the IDF, you need to divide 1 by the document frequency.

We will not use the raw values of TF and IDF, but their log transformations, that is, the logarithm of (1 + tf) and the logarithm of (idf).

As an example, let's calculate the tf * idf score for the word "Анна" in chapter 4. The word "Анна" appears 7 times in this chapter (tf), while there are 1,060 words in chapter 4 (chapter_size), and the word "Anna" is mentioned 32 times out of 171 chapters in total (df).

Thus, the tf * idf of the given word in this chapter will be equal to: math.log (1 + (tf / chapter_size)) * math.log (1 / df), which is approximately 0.01103. Let's write a program that calculates and displays the tf * idf value of a given word (target_word) in a specific chapter (target_chapter).

[war_peace_4.py](http://https://github.com/annannannannanna/War-and-Peace/blob/52e407294c03df284220d13d53f24c89996ab01f/war_peace_4.py)

Now that we know how to calculate the tf * idf value for each word in a chapter, we can identify those words that are most "distinctive" for that chapter. These words could serve as a kind of title for the chapter. Let's write some code that will display the three words with the highest tf * idf values in a given chapter in descending order. For example, if we were to analyze chapter 4, the output would be "павловна анна тетушку".

[war_peace_5.py](http://https://github.com/annannannannanna/War-and-Peace/blob/52e407294c03df284220d13d53f24c89996ab01f/war_peace_4.py)
