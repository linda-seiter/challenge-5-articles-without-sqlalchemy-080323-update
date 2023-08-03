class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str)
            and 5 <= len(title) <= 50
            and not hasattr(self, "title")
        ):
            self._title = title
        else:
            return None
            # raise Exception("Title must be a string between 5 and 50 characters long")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return None
            # raise Exception("Author must be of type Author")
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            return None
            # raise Exception("Magazine must be of type Magazine")


from classes.author import Author
from classes.magazine import Magazine
