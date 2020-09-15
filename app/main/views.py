from flask import render_template
from . import main
from ..request import get_sources,get_articles


#views 
@main.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    """
    title = "Home- Welcome to the News Highlights Website"
   
    # Getting the news sources
    news_sources=get_sources('general')
    tag_line = '"Never miss on the headlines"'
    return render_template('index.html', title = title, sources = news_sources ,statement = tag_line)


@main.route('/articles/<source_id>')  
def articles(source_id):
    '''
    View function that retuns that renders the source articles
    '''
    tag = f'{source_id}'
    news_articles = get_articles(source_id)
    return render_template('articles.html',articles = news_articles,tag = tag)