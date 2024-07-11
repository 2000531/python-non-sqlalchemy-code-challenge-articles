'''class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list({article.magazine for article in self.__articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.__articles.append(article)
        return article

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) if self.__articles else None'''

'''class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name
        self._articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})'''

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name
        self._articles = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable.")

    def add_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise ValueError("Argument must be an instance of Article.")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

