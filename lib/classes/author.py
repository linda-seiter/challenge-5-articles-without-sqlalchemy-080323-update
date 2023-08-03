class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name
        else:
            return None
            # raise Exception("Name must be a non-empty string and it cannot be changed")

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})


from classes.article import Article
