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
