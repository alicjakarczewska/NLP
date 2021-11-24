import string
import sklearn
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.pipeline import Pipeline
import nltk
import nltk.stem
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


def tokenize(text):
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]


categories = ['business', 'entertainment', 'politics', 'sport', 'tech']

docs_data = sklearn.datasets.load_files(container_path='bbc', description=None, categories=categories,
                                        load_content=True, encoding='unicode_escape', shuffle=True, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(docs_data.data, docs_data.target, test_size=0.5)

# TRANSFORM THE TEST DATA INTO A FORM THE CLASSIFIER CAN WORK WITH

count_vect = CountVectorizer(tokenizer=tokenize, stop_words='english')
X_test_counts = count_vect.fit_transform(raw_documents=X_test)

tfidf_transformer = TfidfTransformer(use_idf=True)
X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)

#  PIPELINE

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer(use_idf=True)),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, verbose=1)), ])

text_clf.fit(X_train, y_train)

# TEST THE MODEL WE’VE JUST TRAINED USING THE TEST DATA

predicted = text_clf.predict(X_test)

print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test, predicted, target_names=docs_data.target_names))

print(metrics.confusion_matrix(y_test, predicted))

