import requests
from bs4 import BeautifulSoup


#with open('index.html') as file:
 #  src = file.read()

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

root = soup.html

root_childs = [e.name for e in root.children if e.name is not None]
print(root_childs)


#for item in find:
 #   print(item.text)
#   post_title = soup.find(class = "movie").find_previous_sibling().find_next().text
#print(post_title)

print("Hello world")