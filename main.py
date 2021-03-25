from flask import Flask, redirect, url_for, render_template, request
from function import *
import pymysql.cursors
from Bolek import *
from datetime import datetime
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title='Bolek' )


@app.route("/<name>", methods = ['GET', 'POST', 'DELETE'])
def print_data(name):
        all_users, cookies_user = bazaDanych()
        timee = datetime.datetime.now()
        JWT = cookies_user['cookie']
        her_obj = take_one_hero(all_users, name, JWT, timee)
        try:
            nation = len(her_obj.statistics[0])
            sojusz = her_obj.statistics[1]
            pop = her_obj.statistics[2]
            off = her_obj.statistics[3]
            deff = her_obj.statistics[4]
            hero_lvl = her_obj.statistics[5]
            link_hero = her_obj.link
            statuss = her_obj.status
            soup = her_obj.soup
            il = her_obj.il
            name_hero = her_obj.name
            last_scan_name = her_obj.last_scan['name']
            last_scan_il = her_obj.last_scan['link_img']
            last_scan_pop = her_obj.last_scan['pop']
            last_scan_off = her_obj.last_scan['off']
            last_scan_deff = her_obj.last_scan['deff']
            last_scan_hero_lvl = her_obj.last_scan['herolvl']
            last_scan_time = her_obj.last_scan['czas']
            last_scan_time = last_scan_time
            data_time = last_scan_time.strftime("%Y-%m-%d %H:%M:%S")
            data_time2 = last_scan_time
            data_time2 = data_time2 - datetime.timedelta(0, 1)
            data_time2 = data_time2.strftime("%Y-%m-%d %H:%M:%S")
            time_now = her_obj.time.strftime("%H:%M:%S")
            link_last_image = 'https://azot-potas.pl/image/' + data_time[0:10] + '/' + her_obj.name + '_' + data_time[11:] + '.png'
            link_last_image2 = 'https://azot-potas.pl/image/' + data_time[0:10] + '/' + her_obj.name + '_' + data_time2[11:] + '.png'
            link_image_now = 'https://azot-potas.pl/image/' + data_time[0:10] + '/' + her_obj.name + '_' + time_now + '.png'
            status_last_scan = her_obj.status_last_scan
            now_scan_time = her_obj.time.strftime("%Y-%m-%d %H:%M:%S")
        except:
            nation = 'Brak danych'
            sojusz = 'Brak danych'
            pop = 'Brak danych'
            off= 'Brak danych'
            deff = 'Brak danych'
            hero = 'Brak danych'
            link_hero = 'Brak danych'
            scan1 = 'Brak danych'
            hero_lvl = 'Brak danych'
            statuss = 'Sprawdź ciasteczko JWT'
            soup = 'Brak danych'
            name_hero = 'Brak danych'
            il = 'Brak danych'
            last_scan_name = 'Brak danych'
            last_scan_il = 'Brak danych'
            last_scan_pop = 'Brak danych'
            last_scan_off = 'Brak danych'
            last_scan_deff = 'Brak danych'
            last_scan_hero_lvl = 'Brak danych'
            last_scan_time = 'Brak danych'
            data_time = 'Brak danych'
            data_time2 = 'Brak danych'
            link_last_image = 'Brak danych'
            link_image_now = 'Brak danych'
            link_last_image2 = 'Brak danych'
        return render_template('index.html',
                               hero_lvl=hero_lvl,
                               link_last_image=link_last_image,
                               now_scan_time=now_scan_time,
                               status_last_scan=status_last_scan,
                               link_last_image2=link_last_image2,
                               last_scan_time=last_scan_time,
                               link_image_now=link_image_now,
                               last_scan_hero_lvl=last_scan_hero_lvl,
                               last_scan_deff=last_scan_deff,
                               last_scan_off=last_scan_off,
                               last_scan_pop=last_scan_pop,
                               last_scan_name=last_scan_name,
                               last_scan_il=last_scan_il,
                               title='Bolek',
                               statuss=statuss,
                               off=off,
                               deff=deff,
                               nation=nation,
                               pop=pop,
                               sojusz=sojusz,
                               name_hero=name_hero,
                               link_image=il,
                               link_hero=link_hero,
                               soup=soup)

@app.route("/add/<cookie>" , methods = ['GET', 'POST', 'DELETE'])
def add_kookie(cookie):
    data = str(cookie)
    addCookie(data)
    dataa = "Dodano nowe ciasteczko: \n"+cookie
    return render_template('add.html', title='Bolek', dataa=dataa )

@app.route("/test")
def test():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host='185.243.54.35')


