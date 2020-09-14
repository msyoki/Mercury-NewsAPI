from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key 
api_key = app.config['NEWS_API_KEY']

# Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources(category):
    '''
    Function that gets news sources list from the News API
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_results(sources_results_list)

    return sources_results

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

def get_articles(id):
    '''
    Function that gets sources and their articles
    '''

    get_articles_url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(id,api_key)


    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


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