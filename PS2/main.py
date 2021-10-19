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
print("\nZadanie 1. Liczba zdan: {}".format(len(list(my_doc.sents))))

# Zadanie 2. Liczba tokenow
tokenizer = nlp.tokenizer
tokens = tokenizer(my_text)
print("\nZadanie 2. Liczba tokenow: {}".format(len(tokens)))

# Zadanie 3. Srednia liczba tokenow w zdaniu
print("\nZadanie 3. Srednia liczba tokenow w zdaniu: {}".format(
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

print("\nZadanie 4.")
print("Liczba rzeczownikow: {}".format(nounNumber))
print("Liczba czasownikow: {}".format(verbNumber))
print("Liczba przymiotnikow: {}".format(adjNumber))
print("Liczba przysłowkow: {}".format(advNumber))

print("\nZadanie 5.")
# Zadanie. 5
# 5 najczęściej występujących rzeczowników w podstawowej formie (lematyzacja)

nouns = [token.text
         for token in my_doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]

nouns_lemma = [token.lemma_
              for token in my_doc
              if (not token.is_stop and
              not token.is_punct and
              token.pos_ == "NOUN")]

from collections import Counter

# five most common noun tokens
nouns_lemma_freq = Counter(nouns_lemma)
common_nouns_lemma = nouns_lemma_freq.most_common(5)

print("5 najczęściej występujących rzeczowników w podstawowej formie (lematyzacja):")
print(common_nouns_lemma)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)

text_nouns = ""
for noun in common_nouns:
  text_nouns += noun[0]
  text_nouns += " "

doc_nouns = nlp(text_nouns)

print("\n5 najczęściej występujących rzeczowników i ich podstawowe formy (po lematyzacji):")
print(common_nouns)

for token in doc_nouns:
  print("rzeczownik: {}".format(token) + "\t po lematyzacji: {}".format(token.lemma_))

print("\nZadanie 6.")
# Zadanie. 6
# Dla dwóch najczęściej występujących rzeczowników wyświetli określające go przymiotniki występujące w tekście (dependencies)

# dependencies to first most common word
dep1 = [token.text for token in my_doc 
  if(
    str(token.head) == str(doc_nouns[0]) and
    token.pos_ == "ADJ"    
    )]

# dependencies to second most common word
dep2 = [token.text for token in my_doc 
  if(
    str(token.head) == str(doc_nouns[1]) and
    token.pos_ == "ADJ"    
    )]

# dependencies to second most common word
dep3 = [token.text for token in my_doc 
  if(
    str(token.head) == str(doc_nouns[2]) and
    token.pos_ == "ADJ"    
    )]

print("Przymiotniki do {}: {}".format(doc_nouns[0], dep1))
print("Przymiotniki do {}: {}".format(doc_nouns[1], dep2))
print("Przymiotniki do {}: {}".format(doc_nouns[2], dep3))
