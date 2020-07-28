# Inspired in https://www.instagram.com/p/CDHAZtAA8M_/

from googlesearch import search

query = "Python"
LIMIT= 10

# tld refers to the top level domain, like .io or .com
# num refers to the max results you want

for i in search(query, tld="com", num=LIMIT, stop=10, pause=2):
  print(i)
