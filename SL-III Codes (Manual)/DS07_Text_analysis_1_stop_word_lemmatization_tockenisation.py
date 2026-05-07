# Text Analytics 1. Extract Sample 
# document and apply following document 
# preprocessing methods: Tokenization, 
# POS Tagging, stop words removal, 
# Stemming and Lemmatization. 
# 2. Create representation of documents by 
# calculating Term Frequency and Inverse 
# DocumentFrequency. 


# # 1. Import Libraries
# 


import nltk


from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# # 2. Download Required Data (FIXED)
# 


nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')  # ✅ FIX

# # 3. Sample Document



document = """Text Analytics is a crucial step in analyzing unstructured data.
It involves tokenization, lemmatization, and stop words removal."""

# # 4. Tokenization
# 


tokens = wordpunct_tokenize(document)
print("\nTokens:\n", tokens)

# # 5. POS Tagging (NOW WORKS)


pos_tags = nltk.pos_tag(tokens)
print("\nPOS Tags:\n", pos_tags)

# # 6. Stop Words Removal



stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nFiltered Tokens:\n", filtered_tokens)

# # 7. Stemming
# 


stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print("\nStemmed Words:\n", stemmed_words)

# # 8. Lemmatization
# 


lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\nLemmatized Words:\n", lemmatized_words)

# # 9. TF-IDF
# 


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([document])
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())
print("\nFeature Names:\n", vectorizer.get_feature_names_out())

#