import requests
from bs4 import BeautifulSoup


with open('index.html') as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')


#find_a = soup.find_all("a")
#for item in find_a:
 #   item_text = item.text
  #  item_url = item.get("href")
   # print(f"{item_text}: {item_url}")




#find_all = soup.find(class_= "social__networks").find("ul").find_all("a")

#for item in find_all:
#    print(f"{item.text}: {item}")

#find = soup.find("div").find("p").text
#print(find)

#title = soup.title
#print(title.string)

#for item in find:
 #   print(item.text)
#   post_title = soup.find(class = "movie").find_previous_sibling().find_next().text
#print(post_title)
