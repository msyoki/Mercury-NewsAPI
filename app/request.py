from urllib.request import urlopen
import json
from .models import Source,Article,Category


def configure_request(app):
    global api_key,art_url,base_url,cat_url,p_url
    api_key = app.config['NEWS_API_KEY']         
    base_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['ARTICLE_API_URL']
    cat_url= app.config['CAT_API_URL']



def process_results(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

       
        source_object = Source(id, name, description,url, category)
        source_results.append(source_object)

    return source_results

def get_sources(category):
    '''
    Function that gets news sources list from the News API
    '''
    get_sources = base_url.format(category,api_key)

    with urlopen(get_sources) as url:
        data = url.read()
        response=json.loads(data)

        sources_results = None

        if  response["sources"]:
            sources_list = response["sources"]
            sources_results = process_results(sources_list)

    return sources_results

def process_articles(article_list):
    """
    Function that processes the article results and transforms them into a list of objects
    Args:
        article_list: A list of dictionaries that contains article details
    Returns:
        article_results: A list of article objects
    """
    article_results = []

    for article_item in article_list:
        author = article_item.get('author')
        publishedAt = article_item.get('publishedAt')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        url = article_item.get('url')

        article_object = Article(author,publishedAt,title,urlToImage,description,url)
        article_results.append(article_object)

    return article_results

def get_articles(id):
    '''
    Function that gets sources and their articles
    '''

    articles_url = art_url.format(id,api_key)


    with urlopen(articles_url) as url:
        data = url.read()
        response = json.loads(data)

        articles_results = None

        if  response['articles']:
            articles_list = response['articles']
            articles_results = process_articles(articles_list)

    return articles_results




def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    category_url = cat_url.format(cat_name,api_key)
    with urlopen(category_url) as url:
        data = url.read()
        response = json.loads(data)

        cartegory_results = None

        if response['articles']:
            cartegory_list = response['articles']
            cartegory_results = process_articles(cartegory_list)

    return cartegory_results




