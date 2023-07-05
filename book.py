class Book:
    id = 0
    title = ""
    author = ""
    publishing_house = ""
    publication_year = ""
    genre = ""
    description = ""

    def __init__(self, title, author, publishing_house, publication_year, genre, description):
        self.title = title
        self.author = author
        self.publishing_house = publishing_house
        self.publication_year = publication_year
        self.genre = genre
        self.description = description
        Book.id += 1
        print("Book registered successfully")

