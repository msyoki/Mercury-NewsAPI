from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key 
api_key = app.config['NEWS_API_KEY']

# Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    """
    Function that receives news sources list from the News API
    """
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