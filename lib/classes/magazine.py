class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            return None
            # raise Exception("Name must be a string between 2 and 16 characters long")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and category:
            self._category = category
        else:
            return None
            # raise Exception("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None

    def contributing_authors(self):
        non_unique_authors = [article.author for article in self.articles()]
        if unique_contributors := list(
            {
                author
                for author in non_unique_authors
                if non_unique_authors.count(author) > 2
            }
        ):
            return unique_contributors
        else:
            None


from classes.article import Article
