from urllib import request
import json


def fetch_book(url):
    response = request.urlopen(url).read()
    return json.loads(response)


URL_BOOK = "http://localhost:1234/book"
print(fetch_book(URL_BOOK))
