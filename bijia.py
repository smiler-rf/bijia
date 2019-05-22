from flask import Flask,render_template,url_for,request,redirect,session,g
from exts import db
import config
from models import City_Movie
from models import MaoYan_cinema
from models import Tickets
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

cities = City_Movie.objects.all()

"""首页"""
@app.route('/')
def index():
    city = "北京"
    maoCinemas = MaoYan_cinema.objects(city=city)[: 12]
    cinemaCount = MaoYan_cinema.objects(city=city).count()
    Movies = City_Movie.objects.all()
    movies = ""
    for line in Movies:
        if city in line.cities:
            movies = line.c_m[city]
    groups = cinemaCount // 12 if cinemaCount % 12 == 0 else cinemaCount // 12 + 1
    return render_template('main.html', city=city,movies=movies, cities=cities,cinemas=maoCinemas,groups=groups)


"""城市"""
@app.route('/<city>/')
def city(city):
    maoCinemas = MaoYan_cinema.objects(city=city)[: 12]
    cinemaCount = MaoYan_cinema.objects(city=city).count()
    Movies = City_Movie.objects.all()
    movies = ""
    for line in Movies:
        if city in line.cities:
            movies = line.c_m[city]
    if movies == {}:
        Movies = City_Movie.objects.all()
        for line in Movies:
            if "北京" in line.cities:
                movies = line.c_m["北京"]  # 没有热映电影的话就拿北京的热映电影充数
    groups = cinemaCount // 12 if cinemaCount % 12 == 0 else cinemaCount // 12 + 1
    return render_template('main.html', city=city,movies=movies, cities=cities,cinemas=maoCinemas,groups=groups)

@app.route('/js_getCinema/',methods=['GET'])
def js_cinema():
    city = request.args.get('city')
    offset = int(request.args.get('offset'))
    maoCinemas = MaoYan_cinema.objects(city=city)[offset:offset + 12]
    cinemas = {}
    for cinema in maoCinemas:
        cinemas[cinema.name] = cinema.address
    cinemas = json.dumps(cinemas)
    return cinemas

@app.route('/<curCity>/cinema/<name>')
def cinema(curCity, name):
    cinema = MaoYan_cinema.objects(name=name).first()
    movies = Tickets.objects(cinema_name=name)
    tickets = Tickets.objects(cinema_name=name)
    return render_template('cinema.html', city=curCity, cities=cities, cinema=cinema, movies=movies, tickets=tickets)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9000', debug=True)

