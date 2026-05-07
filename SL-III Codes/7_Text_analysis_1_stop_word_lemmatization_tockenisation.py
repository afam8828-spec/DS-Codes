# Text Analytics 1. Extract Sample 
# document and apply following document 
# preprocessing methods: Tokenization, 
# POS Tagging, stop words removal, 
# Stemming and Lemmatization. 
# 2. Create representation of documents by 
# calculating Term Frequency and Inverse 
# DocumentFrequency. 

# Practical 7: Text Analytics

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required data
nltk.download('punkt')
nltk.download('punkt_tab')   # ✅ FIX
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "Text analytics is a crucial step in analyzing unstructured data."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopwords removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered_tokens]
print("Stemmed Words:", stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Lemmatized Words:", lemmatized)

# TF-IDF
corpus = [text]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)

print("TF-IDF Matrix:\n", tfidf.toarray())
print("Feature Names:", vectorizer.get_feature_names_out())