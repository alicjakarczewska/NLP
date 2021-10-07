# 1 . Sentence Tokenization

import nltk

nltk.download('punkt')

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.

The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text = nltk.sent_tokenize(text)

print(tokenized_text)

# 2 . Word Tokenization

tokenized_word = nltk.word_tokenize(text)

print(tokenized_word)

# 3 . Frequency Distribution

fdist = nltk.probability.FreqDist(tokenized_word)

print(fdist.most_common(2))

# 4 . Stopwords

nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words("english"))
print(stop_words)

# 5 . Removing Stopwords

filtered_sent=[]

for w in tokenized_word:

    if w not in stop_words:

        filtered_sent.append(w)

print("Tokenized Sentence:",tokenized_word)

print("Filterd Sentence:",filtered_sent)

# 6 . Stemming and lemmatization

nltk.download('wordnet')
lem = nltk.stem.wordnet.WordNetLemmatizer()
stem = nltk.stem.porter.PorterStemmer()
word = "better"
print("Lemmatized Word:",lem.lemmatize(word,"a"))
print("Stemmed Word:",stem.stem(word))

# 7 . POS Tagging

nltk.download('averaged_perceptron_tagger')
sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)
print(nltk.pos_tag(tokens))