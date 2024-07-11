#!/usr/bin/env python3
'''import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()'''
# lib/debug.py

'''if __name__ == "__main__":
    # Create some sample instances
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    
    # Create articles
    article1 = author1.add_article(magazine1, "The Rise of AI")
    article2 = author2.add_article(magazine2, "Healthy Living Tips")
    article3 = author1.add_article(magazine2, "Mental Health Matters")
    
    # Test methods
    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())
    
    print(magazine1.articles())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())
    
    print(Magazine.top_publisher())'''

# lib/debug.py

'''if __name__ == "__main__":
    # Create some sample instances
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    
    # Create articles
    article1 = author1.add_article(magazine1, "The Rise of AI")
    article2 = author2.add_article(magazine2, "Healthy Living Tips")
    article3 = author1.add_article(magazine2, "Mental Health Matters")
    
    # Test methods
    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())
    
    print(magazine1.articles())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())
    
    print(Magazine.top_publisher())'''

# lib/debug.py

if __name__ == "__main__":
    # Create some sample instances
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    
    # Create articles
    article1 = author1.add_article(magazine1, "The Rise of AI")
    article2 = author2.add_article(magazine2, "Healthy Living Tips")
    article3 = author1.add_article(magazine2, "Mental Health Matters")
    
    # Test methods
    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())
    
    print(magazine1.articles())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())
    
    print(Magazine.top_publisher())
