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
regex = '2:\d{2}:\d{2}'
results = re.findall(regex, text)

print(results)

# results = ['2:05:41', '2:06:49', '2:18:58', '2:19:10', '2:17:08', '2:17:01', '2:18:58', '2:22:01', '2:22:05', '2:18:58', '2:22:01', '2:22:05', '2:22:51', '2:24:23', '2:25:13', '2:26:51', '2:27:07', '2:27:29', '2:28:18', '2:05:41', '2:05:42', '2:05:45', '2:06:49', '2:09:01', '2:10:38', '2:11:20', '2:05:41', '2:05:42', '2:05:45', '2:06:04', '2:06:08', '2:06:41', '2:06:42', '2:06:49', '2:09:01', '2:09:25']