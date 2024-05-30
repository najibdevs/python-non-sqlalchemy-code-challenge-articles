class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title
        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        frequent_authors = [author for author in set(authors) if authors.count(author) > 2]
        return frequent_authors if frequent_authors else None

