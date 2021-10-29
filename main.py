# Alicja Karczewska PS4

# Before run code install:
# pip3 install spacy
# python -m spacy download en_core_web_sm

# Zadanie.Napisz program, który na podstawie załączonego pliku przyklad.txt:
# - utworzy słownik wszystkich słów i zapisze go w pliku slownik.txt, każde słowo w nowej linii
# - w 20% wylosowanych słów w pliku przyklad.txt dokona od jednej do trzech modyfikacji w postaci: zamiany litery, usunięcia litery, dodania litery. Zamieniony tekst zapisze do pliku przyklad_z_bledami.txt
# - poprawi błędy w pliku przyklad_z_bledami.txt wyszukując słowa najbliższe w pliku slownik.txt używając odległości edycyjnej i zapisze wynik do pliku przyklad_poprawiony.txt
# - obliczy ilość błędów które pozostaly po poprawieniu porównując wynik z plikiem oryginalnym
# Do podziału tekstu na słowa wykorzystaj jedną z bibliotek NLP.  Jako rozwiązanie wgraj tylko swój program.

import spacy
nlp=spacy.load("en_core_web_sm")

# Parse text through the `nlp` model
my_text = """The first published stemmer was written by Julie Beth Lovins in 1968.[1] This paper was remarkable for its early date and had great influence on later work in this area. Her paper refers to three earlier major attempts at stemming algorithms, by Professor John W. Tukey of Princeton University, the algorithm developed at Harvard University by Michael Lesk, under the direction of Professor Gerard Salton, and a third algorithm developed by James L. Dolby of R and D Consultants, Los Altos, California.

A later stemmer was written by Martin Porter and was published in the July 1980 issue of the journal Program. This stemmer was very widely used and became the de facto standard algorithm used for English stemming. Dr. Porter received the Tony Kent Strix award in 2000 for his work on stemming and information retrieval.

Many implementations of the Porter stemming algorithm were written and freely distributed; however, many of these implementations contained subtle flaws. As a result, these stemmers did not match their potential. To eliminate this source of error, Martin Porter released an official free software (mostly BSD-licensed) implementation[2] of the algorithm around the year 2000. He extended this work over the next few years by building Snowball, a framework for writing stemming algorithms, and implemented an improved English stemmer together with stemmers for several other languages.

The Paice-Husk Stemmer was developed by Chris D Paice at Lancaster University in the late 1980s, it is an iterative stemmer and features an externally stored set of stemming rules. The standard set of rules provides a 'strong' stemmer and may specify the removal or replacement of an ending. The replacement technique avoids the need for a separate stage in the process to recode or provide partial matching. Paice also developed a direct measurement for comparing stemmers based on counting the over-stemming and under-stemming errors.
"""

my_doc = nlp(my_text.replace("\n", ""))
# Removing StopWords and punctuations
my_doc_cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]

f = open("slownik.txt", "w")
for token in my_doc_cleaned:
  f.write(token.text+"\n")
f.close()

changed_dict=[]
with open('slownik.txt','r') as file: 
    for line in file:   
        for word in line.split():         
            changed_dict.append(word) 

# losowanie 20% slow do zmiany
import random

bef_indices = [0]
for i in range(1, len(changed_dict)):
  bef_indices.append(bef_indices[i-1] + 1)

percentage = 0.2
k = len(changed_dict)*percentage 
indicies = random.sample(bef_indices, int(k))

import string

def replace(s, position, character):
    return s[:position] + character + s[position+1:]

def charge_char_in_word(word):
  word[random.randrange(len(word))] = random.choice(string.ascii_letters)

# zmiana w wyrazach pod wylosowanymi indeksami (1-3 modyfikacje)
for i in indicies:  
  how_many = random.randrange(3)  
  # dodanie znaku  
  character = random.choice(string.ascii_letters)
  word = changed_dict[i]
  changed_dict[i] = ''.join((word, character))
  # usuniecie znaku
  if how_many > 0:
    changed_dict[i] = changed_dict[i][:-2]
  # zmiana znaku
  if how_many > 1:
    character = random.choice(string.ascii_letters)
    word = changed_dict[i][:-1]
    changed_dict[i] = ''.join((word, character))
  
f = open("przyklad_z_bledami.txt", "w")
for word in changed_dict:
  f.write(word+"\n")
f.close()




