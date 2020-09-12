from flask import render_template
from app import app

#views 
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'NEWS API'
    statement = '"Never miss out on the highlights"'
    return render_template('index.html',title = title,statement = statement)


@app.route('/topic/<topic_id>')
def topic(topic_id):
    '''
    View topic page fuction that returns the topic details page and its data 
    '''
    return render_template('topic.html',id = topic_id)