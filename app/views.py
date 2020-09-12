from flask import render_template
from app import app

#views 
@app.route('/')  
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to NEWS API'
    statement = '"Never miss out on the highlights"'
    return render_template('index.html',title = title,statement = statement)


@app.route('/articles/<sources_id>')  
def topic(sources_id):
    '''
    View topic page fuction that returns the topic details page and its data 
    '''
    return render_template('topic.html',id = sources_id)