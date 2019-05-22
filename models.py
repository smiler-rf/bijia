from exts import db

# class City(db.Document):
#     meta = {'collection': 'cities'}
#     key = db.StringField()
#     cities = db.ListField(db.StringField(),default=list)

# class Movie(db.Document):
#     meta = {'collection': 'douban_movie'}
#     name = db.StringField()
#     actors = db.ListField(db.StringField(),default=list)
#     directors = db.ListField(db.StringField(),default=list)
#     score = db.FloatField()
#     image = db.StringField()

class City_Movie(db.Document):
    meta = {'collection': 'city_movies'}
    key = db.StringField()
    cities = db.ListField(db.StringField(), default = list)
    c_m = db.DictField(db.DictField(db.DictField(db.StringField())))

class MaoYan_cinema(db.Document):
    meta = {'collection': 'maoyan_cinema'}
    city = db.StringField()
    name = db.StringField()
    url = db.StringField()
    address = db.StringField()

class Tickets(db.Document):
    meta = {'collection': 'tickets'}
    city = db.StringField()
    url = db.StringField()
    cinema_name = db.StringField()
    address = db.StringField()
    phone = db.StringField()
    name = db.StringField()
    score = db.StringField()
    image = db.StringField()
    date = db.ListField(db.StringField(), default=list)
    plist = db.DictField(db.ListField(db.DictField(db.StringField()), default=list))