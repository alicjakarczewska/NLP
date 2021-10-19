# Alicja Karczewska PS3

# Zadanie. Napisz program który z wykorzystaniem wyrażeń regularnych znajdzie wszystkie czasy przebiegnięcia maratonu wymienione w tym artykule. 

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://bieganie.pl/sport/kipchoge-is-limited-relacja-z-40-london-marathon/"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

import re
regex = '\d:\d{2}:\d{2}'
results = re.findall(regex, text)

print(results)