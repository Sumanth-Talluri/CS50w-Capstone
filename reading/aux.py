import requests
import urllib

## Google Books API

apiKey = 'AIzaSyDaLqgrHCuhhMy3J3nvSZholYAR-4Z88Bo'

class Book():

    def __init__(self, gid, title, authors, thumbnail):
        self.gid = gid
        self.title = title
        self.authors = authors
        self.thumbnail = thumbnail

class BookInfo():

    def __init__(self, gid, title, authors, publisher, publishedDate, description, isbn10, isbn13, pageCount, categories, averageRating, ratingsCount, language, buyLink, thumbnail):
        self.gid = gid
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.description = description
        self.isbn10 = isbn10
        self.isbn13 = isbn13
        self.pageCount = pageCount
        self.categories = categories
        self.averageRating = averageRating
        self.ratingsCount = ratingsCount
        self.language = language
        self.buyLink = buyLink
        self.thumbnail = thumbnail


def getBooksByTitle(title):

    query = urllib.parse.quote(title)
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={apiKey}')
    data = response.json()

    books = []

    try:
        for item in data['items']:
            try:
                book = Book(item['id'], item['volumeInfo']['title'],
                    item['volumeInfo']['authors'],
                    item['volumeInfo']['imageLinks']['thumbnail'])

                books.append(book)
            except:
                pass
    except:
        pass

    return books


def getBookById(id):

    response = requests.get(f'https://www.googleapis.com/books/v1/volumes/{id}?key={apiKey}')
    data = response.json()

    book = BookInfo(id,
    data.get('volumeInfo').get('title'),
    data.get('volumeInfo').get('authors'),
    data.get('volumeInfo').get('publisher'),
    data.get('volumeInfo').get('publishedDate'),
    data.get('volumeInfo').get('description'),
    data.get('volumeInfo').get('industryIdentifiers')[0].get('identifier'),
    data.get('volumeInfo').get('industryIdentifiers')[1].get('identifier'),
    data.get('volumeInfo').get('pageCount'),
    data.get('volumeInfo').get('categories'),
    data.get('volumeInfo').get('averageRating'),
    data.get('volumeInfo').get('ratingsCount'),
    data.get('volumeInfo').get('language'),
    data.get('volumeInfo').get('infoLink'),
    data.get('volumeInfo').get('imageLinks').get('thumbnail'))

    return book


## Quotes for the index page

quotes = [
    ["That's the thing about books. They let you travel without moving your feet.", "Jhumpa Lahiri"],
    ["A book is a dream that you hold in your hands.", "Neil Gaiman"],
    ["Books are mirrors: you only see in them what you already have inside you.", "Carlos Ruiz Zafón"],
    ["Books are a uniquely portable magic.", "Stephen King"],
    ["There is no friend as loyal as a book.", "Ernest Hamingway"],
    ["A room without books is like a body without soul.", "Cicero"],
    ["Once you learn to read, you will be forever free.", "Frederick Douglass"],
    ["A reader lives a thousand lives before she dies.", "George R. R. Martin"],
    ["Books are the plane, the train and the road. They are the destination and the journey. They are home.", "Anna Quindlen"],
    ["A book is a gift you can open again and again.", "Garrison Keillor"]
]
