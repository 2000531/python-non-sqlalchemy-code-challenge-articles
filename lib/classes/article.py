'''class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

    @property
    def title(self):
        return self.__title'''

'''class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author.")
        self.__author = new_author

    @property
    def magazine(self):
        return self.__magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self.__magazine = new_magazine

    @property
    def title(self):
        return self.__title'''

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        author.add_article(self)
        magazine.add_article(self)
        Article.all.append(self)

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable.")
