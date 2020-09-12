from flask import render_template
from app import app
from .request import get_sources
#views 
@app.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    """
    title = "Home- Welcome to the News Highlights Website"
   
    # Getting the news sources
    news_sources = get_sources('general')
    tag_line = '"Never miss on the headlines"'
    return render_template('index.html', title=title, sources=news_sources ,statement = tag_line)


# @app.route('/source/<source_id>')  
# def source(source_id):
#     '''
#     View topic page fuction that returns the topic details page and its data 
#     '''
#     return render_template('source.html',id = source_id)