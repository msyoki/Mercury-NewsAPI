import unittest
from app.models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Artcle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_article = Article('BBC News','2020-09-13T19:37:20.5761889Z','Coronavirus: Israeli minister resigns over plans for second lockdown','https://ichef.bbci.co.uk/news/1024/branded_news/068B/production/_114357610_gettyimages-1205060062-2.jpg','Housing Minister Yaacov Litzman says the measure will affect key religious holidays later this month.','http://www.bbc.co.uk/news/world-middle-east-54134869')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_article,Article))



    def test_init(self):
        """
        Test case to check if the Article class is initialised
        """
        self.assertEqual( self.news_article.author, 'BBC News')
        self.assertEqual( self.news_article.publishedAt, '2020-09-13T19:37:20.5761889Z')
        self.assertEqual( self.news_article.title, 'Coronavirus: Israeli minister resigns over plans for second lockdown')
        self.assertEqual( self.news_article.urlToImage, 'https://ichef.bbci.co.uk/news/1024/branded_news/068B/production/_114357610_gettyimages-1205060062-2.jpg')
        self.assertEqual( self.news_article.description, 'Housing Minister Yaacov Litzman says the measure will affect key religious holidays later this month.')
        self.assertEqual( self.news_article.url, 'http://www.bbc.co.uk/news/world-middle-east-54134869')


if __name__ == '__main__':
    unittest.main()


