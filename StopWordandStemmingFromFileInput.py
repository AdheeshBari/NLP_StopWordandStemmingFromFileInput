import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('stopwords')

if __name__ == "__main__":
    # Prompt the user to enter the file path
    file_path = input("Enter the path to the file: ")
    
    # Read the content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Tokenize words from the file content
    word_tokens = word_tokenize(file_content)
    
    # Define stop words in English
    stop_words = set(stopwords.words('english'))
    
    # Remove stop words
    filtered_words = [word for word in word_tokens if word.lower() not in stop_words]
    
    # Initialize the stemmer
    stemmer = PorterStemmer()
    
    # Apply stemming to the filtered words
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    
    # Output the results
    print("Filtered Words (without stop words):\n", filtered_words)
    print("Stemmed Words:\n", stemmed_words)

# OUTPUT
# Enter the path to the file: Textfile.txt
# Filtered Words (without stop words):
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'centuries', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum', '.']
# Stemmed Words:
#  ['lorem', 'ipsum', 'simpli', 'dummi', 'text', 'print', 'typeset', 'industri', '.', 'lorem', 'ipsum', 'industri', "'s", 'standard', 'dummi', 'text', 'ever', 'sinc', '1500', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambl', 'make', 'type', 'specimen', 'book', '.', 'surviv', 'five', 'centuri', ',', 'also', 'leap', 'electron', 'typeset', ',', 'remain', 'essenti', 'unchang', '.', 'popularis', '1960', 'releas', 'letraset', 'sheet', 'contain', 'lorem', 'ipsum', 'passag', ',', 'recent', 'desktop', 'publish', 'softwar', 'like', 'aldu', 'pagemak', 'includ', 'version', 'lorem', 'ipsum', '.']