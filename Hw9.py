import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("h3")

    for book in books:
        title = book.find("a")["title"]
        print(title)
else:
    print("error")