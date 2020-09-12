class Article:
    '''
    Article class to define Article Objects 
    '''


    def __init__(self,id,poster,title,description,date_posted,time_posted):
        self.id = id
        self.poster = 'https://image.newsapi.org/t/p/w500/khsjha27hbs'+ poster
        self.source = title
        self.description = description
        self.date_posted = date_posted
        self.time_posted = time_posted