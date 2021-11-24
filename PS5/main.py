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
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


def tokenize(text):
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

# Nazwy kategorii (nazwy folderów z pogrupowanymi artykułami)
categories = ['business', 'entertainment', 'politics', 'sport', 'tech']

# Załadowanie zbioru danych artykułów i kategoryzowanie ich zgodnie z nazwą folderu
docs_data = sklearn.datasets.load_files(container_path='bbc', description=None, categories=categories,
                                        load_content=True, encoding='unicode_escape', shuffle=True, random_state=42)

# Podzielenie zbioru danych na zbiór treningowy i testowy (50:50)
#
# Obiekty X będą przechowywać dane, zawartość plików tekstowych.
# X_train będzie zawierał dane plików tekstowych do uczenia klasyfikatora.
# X_test będzie zawierał dane plików tekstowych do przetestowania klasyfikatora.
#
# Obiekty Y posiadają nazwy kategorii ('business', 'entertainment', 'politics', 'sport', 'tech')
# y_train będzie przechowywać nazwy kategorii, które odpowiadają danym tekstowym w X_train
# y_test będzie przechowywać nazwy kategorii, które odpowiadają danym tekstowym w X_test
X_train, X_test, y_train, y_test = train_test_split(docs_data.data, docs_data.target, test_size=0.5)

# Konwersja danych treningowych do postaci, z którą klasyfikator może pracować

# Konfigurowanie wektoryzatora, CountVectorizer() - zamiana kolekcji dokumentów tekstowych na macierz liczby tokenów.
# Funkcja zliczy, ile razy każde słowo w zbiorze danych wystąpi i zaprojektuje, które zliczą się do wektora.
# opcja tokenizer - nadpisuje słowa, zastępuje je lematami
# opcja stop_words - usuwa stop word
count_vect = CountVectorizer(tokenizer=tokenize, stop_words='english')
# X_train_counts - przechowuje wektory wystąpień
X_test_counts = count_vect.fit_transform(raw_documents=X_test)
# przekształcnie liczby wystąpień w wartość częstotliwości odwrotnej częstotliwości dokumentu
tfidf_transformer = TfidfTransformer(use_idf=True)
X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)

# Analogiczne przekształcenia (jak powyżej) dla zbioru testowego
count_vect = CountVectorizer(stop_words='english')
X_test_counts = count_vect.fit_transform(raw_documents=X_test)

tfidf_transformer = TfidfTransformer(use_idf=True)
X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)

#  PIPELINE
# Faza 1. tworzy wektoryzator —  zamienia tekst na liczbę wystąpień
# Faza 2. przekształcenie wektoryzatora na opartą na częstotliwości reprezentację danych
# Faza 3. tworzy klasyfikator

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer(use_idf=True)),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, verbose=1)), ])

# Trenowanie modelu stosując pipeline
# Pobieranie danych treningowych (X_train) i odpowiednich etykiet treningowych (y_train)
# i przekazywanie ich do funkcji fit, która jest wbudowana w pipeline
text_clf.fit(X_train, y_train)

# Uruchomienie przeszkolonego modelu na danych testowych X_test,
# by przewidział kategorie do jakich należą artykuły ze zbioru testowego
predicted = text_clf.predict(X_test)

# Dokładność modelu - średnia dokładność predykcyjna klasyfikatora
print("Trafność klasyfikacji (dla części testowej zbioru danych):")
print(np.mean(predicted == y_test))

# Szczegółowe statystyki według kategorii,
# wynik precyzji dla każdej kategorii i ogólną średnią wydajność modelu od 0 do 1.
print("Szczegółowe statystyki:")
print(metrics.classification_report(y_test, predicted, target_names=docs_data.target_names))

# Macierz pomyłek dla części testowej zbioru danych
print("Macierz pomyłek dla części testowej zbioru danych")
cf_matrix = metrics.confusion_matrix(y_test, predicted)
print(cf_matrix)

# Porównanie z testowaniem na zbiorze treningowym
predicted_train = text_clf.predict(X_train)

# Dokładność modelu - średnia dokładność predykcyjna klasyfikatora
print("Trafność klasyfikacji (dla części treningowej zbioru danych):")
print(np.mean(predicted_train == y_train))

# Macierz pomyłek dla części treningowej zbioru danych
print("Macierz pomyłek dla części treningowej zbioru danych")
cf_matrix_train = metrics.confusion_matrix(y_train, predicted_train)
print(cf_matrix_train)

# Macierz pomyłek dla części testowej zbioru danych - plot
c1 = ConfusionMatrixDisplay.from_predictions(y_test, predicted)
# plt.show()

# Macierz pomyłek dla części treningowej zbioru danych - plot
c2 = ConfusionMatrixDisplay.from_predictions(y_train, predicted_train)

plt.show()


