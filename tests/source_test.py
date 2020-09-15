import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behavioue of the Source class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.news_source = Source('al-jazeera-english','Al Jazeera English','News, analysis from the Middle East and worldwide...','http://www.aljazeera.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Source))

    def test_init(self):
        """
        Test case to check if the Source class is initialised
        """
        self.assertEqual( self.news_source.id, 'al-jazeera-english')
        self.assertEqual( self.news_source.name, 'Al Jazeera English')
        self.assertEqual( self.news_source.description, 'News, analysis from the Middle East and worldwide...')
        self.assertEqual( self.news_source.url, 'http://www.aljazeera.com')
        self.assertEqual( self.news_source.category, 'general')
