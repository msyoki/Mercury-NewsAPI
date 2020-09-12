import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behavioue of the Article class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_article = Article(1234,'https://image.newsapi.org/t/p/w500/khsjha27hbs','Upcoming Envents','Checkout upcoming events this weekend','8/9/2020','15:44hrs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()