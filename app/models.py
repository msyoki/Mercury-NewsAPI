class Source:
    '''
    Source class to define Source Objects 
    '''


    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category


class Article:
    '''
    Article class that defu=nes an article object
    '''

    def __init__(self,author,publishedAt,title,urlToImage,description,url):
        self.author = author
        self.publishedAt = publishedAt
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.url = url
        
class Headlines:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,description,publishedAt,url,urlToImage,title):
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title      