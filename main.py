# Alicja Karczewska

# https://www.machinelearningplus.com/spacy-tutorial-nlp/

# Before run code install:
# pip3 install spacy
# python -m spacy download en_core_web_sm

import spacy
nlp=spacy.load("en_core_web_sm")
# print(nlp)

# Parse text through the `nlp` model
my_text = """A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks. A "complete" computer including the hardware, the operating system (main software), and peripheral equipment required and used for "full" operation can be referred to as a computer system. This term may as well be used for a group of computers that are connected and work together, in particular a computer network or computer cluster.

Computers are used as control systems for a wide variety of industrial and consumer devices. This includes simple special purpose devices like microwave ovens and remote controls, factory devices such as industrial robots and computer-aided design, and also general purpose devices like personal computers and mobile devices such as smartphones. The Internet is run on computers and it connects hundreds of millions of other computers and their users.

Early computers were only conceived as calculating devices. Since ancient times, simple manual devices like the abacus aided people in doing calculations. Early in the Industrial Revolution, some mechanical devices were built to automate long tedious tasks, such as guiding patterns for looms. More sophisticated electrical machines did specialized analog calculations in the early 20th century. The first digital electronic calculating machines were developed during World War II. The first semiconductor transistors in the late 1940s were followed by the silicon-based MOSFET (MOS transistor) and monolithic integrated circuit (IC) chip technologies in the late 1950s, leading to the microprocessor and the microcomputer revolution in the 1970s. The speed, power and versatility of computers have been increasing dramatically ever since then, with MOS transistor counts increasing at a rapid pace (as predicted by Moore's law), leading to the Digital Revolution during the late 20th to early 21st centuries.

Conventionally, a modern computer consists of at least one processing element, typically a central processing unit (CPU) in the form of a metal-oxide-semiconductor (MOS) microprocessor, along with some type of computer memory, typically MOS semiconductor memory chips. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices include input devices (keyboards, mice, joystick, etc.), output devices (monitor screens, printers, etc.), and input/output devices that perform both functions (e.g., the 2000s-era touchscreen). Peripheral devices allow information to be retrieved from an external source and they enable the result of operations to be saved and retrieved. """

my_doc = nlp(my_text)
print(type(my_doc))

# Zadanie 1. Liczba zdan
print("Zadanie 1. Liczba zdan: {}".format(len(list(my_doc.sents))))

# Zadanie 2. Liczba tokenow
tokenizer = nlp.tokenizer
tokens = tokenizer(my_text)
print("Zadanie 2. Liczba tokenow: {}".format(len(tokens)))

# Zadanie 3. Srednia liczba tokenow w zdaniu
print("Zadanie 3. Srednia liczba tokenow w zdaniu: {}".format(
  (len(tokens) / len(list(my_doc.sents)))
))

# Zadanie 4. Liczba rzeczowników, czasowników, przymiotników i przysłówków

nounNumber = 0
verbNumber = 0
adjNumber = 0
advNumber = 0

for token in my_doc:
    if token.pos_ == 'NOUN':
        nounNumber = nounNumber + 1
    if token.pos_ == 'VERB':
        verbNumber = verbNumber + 1
    if token.pos_ == 'ADJ':
        adjNumber = adjNumber + 1
    if token.pos_ == 'ADV':
        advNumber = advNumber + 1

print("Zadanie 4.")
print("Liczba rzeczownikow: {}".format(nounNumber))
print("Liczba czasownikow: {}".format(verbNumber))
print("Liczba przymiotnikow: {}".format(adjNumber))
print("Liczba przysłowkow: {}".format(advNumber))


# Zadanie. 5
# 5 najczęściej występujących rzeczowników w podstawowej formie (lematyzacja)
words = [token.text
         for token in my_doc
         if not token.is_stop and not token.is_punct]

# noun tokens that arent stop words or punctuations
nouns = [token.text
         for token in my_doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]
print(len(nouns))

nouns_lemma = [token.lemma_
              for token in my_doc
              if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]

from collections import Counter

# five most common noun tokens
nouns_lemma_freq = Counter(nouns_lemma)
common_nouns_lemma = nouns_lemma_freq.most_common(5)

print(common_nouns_lemma)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)

print(common_nouns)

# # Printing tokens and boolean values stored in different attributes
# for token in my_doc:
#   print(token.text,'--',token.is_stop,'---',token.is_punct)

# # Removing StopWords and punctuations
# my_doc_cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]

# for token in my_doc_cleaned:
#   print(token.text)

# # Reading a huge text data on robotics into a spacy doc
# robotics_data= """A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks. A "complete" computer including the hardware, the operating system (main software), and peripheral equipment required and used for "full" operation can be referred to as a computer system. This term may as well be used for a group of computers that are connected and work together, in particular a computer network or computer cluster.

# Computers are used as control systems for a wide variety of industrial and consumer devices. This includes simple special purpose devices like microwave ovens and remote controls, factory devices such as industrial robots and computer-aided design, and also general purpose devices like personal computers and mobile devices such as smartphones. The Internet is run on computers and it connects hundreds of millions of other computers and their users.

# Early computers were only conceived as calculating devices. Since ancient times, simple manual devices like the abacus aided people in doing calculations. Early in the Industrial Revolution, some mechanical devices were built to automate long tedious tasks, such as guiding patterns for looms. More sophisticated electrical machines did specialized analog calculations in the early 20th century. The first digital electronic calculating machines were developed during World War II. The first semiconductor transistors in the late 1940s were followed by the silicon-based MOSFET (MOS transistor) and monolithic integrated circuit (IC) chip technologies in the late 1950s, leading to the microprocessor and the microcomputer revolution in the 1970s. The speed, power and versatility of computers have been increasing dramatically ever since then, with MOS transistor counts increasing at a rapid pace (as predicted by Moore's law), leading to the Digital Revolution during the late 20th to early 21st centuries.

# Conventionally, a modern computer consists of at least one processing element, typically a central processing unit (CPU) in the form of a metal-oxide-semiconductor (MOS) microprocessor, along with some type of computer memory, typically MOS semiconductor memory chips. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices include input devices (keyboards, mice, joystick, etc.), output devices (monitor screens, printers, etc.), and input/output devices that perform both functions (e.g., the 2000s-era touchscreen). Peripheral devices allow information to be retrieved from an external source and they enable the result of operations to be saved and retrieved. 
# """

# # Pass the Text to Model
# robotics_doc = nlp(robotics_data)

# print('Before PreProcessing n_Tokens: ', len(robotics_doc))

# # Removing stopwords and punctuation from the doc.
# robotics_doc=[token for token in robotics_doc if not token.is_stop and not token.is_punct]

# print('After PreProcessing n_Tokens: ', len(robotics_doc))

# # Lemmatizing the tokens of a doc
# text='she played chess against rita she likes playing chess.'
# doc=nlp(text)
# for token in doc:
#   print(token.lemma_)

# # Strings to Hashes and Back
# doc = nlp("I love traveling")

# # Look up the hash for the word "traveling"
# word_hash = nlp.vocab.strings["traveling"]
# print(word_hash)

# # Look up the word_hash to get the string
# word_string = nlp.vocab.strings[word_hash]
# print(word_string)

# # Create two different doc with a common word
# doc1 = nlp('Raymond shirts are famous')
# doc2 = nlp('I washed my shirts ')

# # Printing the hash value for each token in the doc

# print('-------DOC 1-------')
# for token in doc1:
#   hash_value=nlp.vocab.strings[token.text]
#   print(token.text ,' ',hash_value)

# print('-------DOC 2-------')
# for token in doc2:
#   hash_value=nlp.vocab.strings[token.text]
#   print(token.text ,' ',hash_value)

