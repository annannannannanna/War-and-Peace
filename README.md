# "War and Peace", by Leo Tolstoy
I took the text from the work from the library [lib.ru](http://http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml "lib.ru") and carried out the initial processing. The goal was to process the words from this work. I broke the text into individual words and output each one on a separate line. Additionally, in places where chapters begin, I added a line indicating the new chapter.

First, let's calculate the frequency of individual words used in the work. To do this, I will use a dictionary. I'm going to write a program that sorts all the words in the text and puts them in the dictionary. The counter will increase with each new word to keep track of how many times it occurs in the text.

The get method will help you find out which value corresponds to a specific key (word) in a dictionary. For example, words.get("word", 0) will either return a value from the dictionary or 0 if there is no such word in the dictionary yet.

The result will show the number of times the target word was found in the text. For example, if the target word is "**князь**", the answer will be 1,289.

Document frequency (df) is the percentage of documents in which a search word occurs. In this case, we are talking about the chapters of a book, not documents. Each chapter is separated by a line with the text "[new chapter]". Let's write a program that calculates the document frequency of a target word in the book.

The text consists of 171 chapters, and the word "человек" occurs in 115 of them (number_of_documents_with_target_word).
The df for the word "человек" is therefore 115/171 = 0.67251462
