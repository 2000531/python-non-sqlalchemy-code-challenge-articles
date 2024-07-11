'''class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__name = name
        self.__category = category
        self.__articles = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__category = new_category

    def articles(self):
        return self.__articles

    def contributors(self):
        return list({article.author for article in self.__articles})

    def article_titles(self):
        return [article.title for article in self.__articles] if self.__articles else None

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.__articles)
        return [author for author, count in author_counts.items() if count > 2] if self.__articles else None

    @classmethod
    def top_publisher(cls):
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()), default=None)'''

'''class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__name = name
        self.__category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        if not self._articles:
            return None
        author_counts = Counter(article.author for article in self._articles)
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))'''

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__name = name
        self.__category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.__category = new_category

    def add_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise ValueError("Argument must be an instance of Article.")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        if not self._articles:
            return None
        author_counts = Counter(article.author for article in self._articles)
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))

