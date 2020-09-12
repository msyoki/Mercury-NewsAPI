import unittest
from app.models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behavioue of the Source class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()