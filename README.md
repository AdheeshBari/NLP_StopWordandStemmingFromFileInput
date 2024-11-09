# NLP_StopWordandStemmingFromFileInput
A script that reads a text file, tokenizes it, removes stop words, and applies stemming to simplify word forms.

This Python program takes a file path as input, reads the file's contents, and processes the text by removing common stop words and applying stemming to each word.
Steps:
1. Setup and Downloads: Ensures necessary NLTK resources for tokenization and stop word removal are downloaded.
2. File Input: Prompts the user to enter the path of the file to be processed.
3. Reading File Content: Opens and reads the file's text content.
4. Tokenization: Splits the file content into individual word tokens.
5. Stop Word Removal: Filters out common English stop words to retain only significant words.
6. Stemming: Initializes the Porter Stemmer and applies it to each filtered word, reducing words to their base forms.
Output: Prints both the list of filtered words and their stemmed forms, showing the simplified text representation.
