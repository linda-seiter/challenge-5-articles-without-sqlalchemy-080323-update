import pytest

from classes.article import Article
from classes.magazine import Magazine
from classes.author import Author


class TestArticle:
    """Article in article.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == 2000
        assert article_2.title == 5000

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        # comment out the next three lines if using Exceptions
        article_1.title = 500
        assert article_1.title == "How to wear a tutu with style"
        assert isinstance(article_1.title, str)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Article(author, magazine, 500)

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= article_1.title <= 50

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Article(author, magazine, "Test")

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")

    def test_has_an_author(self):
        """article has an author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert article_1.author == author_1
        assert article_2.author == author_2

    def test_author_of_type_author(self):
        """author is of type Author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert isinstance(article_1.author, Author)
        assert isinstance(article_2.author, Author)

    def test_has_a_magazine(self):
        """article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine(self):
        """magazine is of type Magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert isinstance(article_1.magazine, Magazine)
        assert isinstance(article_2.magazine, Magazine)

    def test_get_all_magazines(self):
        """Magazine class has all attribute"""
        Magazine.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "Dating life in NYC")

        assert len(Magazine.all) == 2
        assert magazine_1 in Magazine.all
        assert magazine_2 in Magazine.all
