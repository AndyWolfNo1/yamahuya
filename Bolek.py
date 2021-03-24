import requests
from bs4 import BeautifulSoup as bs
import pymysql.cursors
import os.path
from os import path
from request_ts import get_soup, save_image
from datetime import datetime
import datetime

class Hero:
    def __init__(self, hero_dict, JWT, timee):
        self.JWT = JWT
        self.status = ''
        self.name = hero_dict['name']
        self.link = hero_dict['gamer_link']
        self.soup = get_soup(JWT, self.link)
        self.time = timee
        self.date = datetime.date.today()
        self.create_html_soup()
        self.image_link = self.get_image_link()
        self.il = ''
        self.download_image()
        self.statistics = self.take_statistics()
        self.insert_stat()
        self.destruction()
        self.last_scan = self.take_scans()
        self.status_last_scan = 'Bez_zmian'
        self.check_chage_stat()

        # self.convertToBinaryData('')

    def create_html_soup(self):
        data_teraz = str(self.date)
        link = "soups/"+data_teraz
        if(path.exists(link)):
            time = datetime.datetime.now().time()
            time = str(time)
            time = time[0:8]
            link = 'soups/'+data_teraz+'/'+self.name+'_'+time
            file = open(link, 'w')
            file.write(str(self.soup.contents))
            file.close()
        else:
            os.mkdir(link)
            self.create_html_soup()

    def get_image_link(self):
        list_img = list()
        divs = self.soup.find_all('img')
        link = 'https://ts3.travian.pl/'
        for i in range(len(divs)):
            if (divs[i].attrs['src']):
                # print('dodano do list_img', i)
                list_img.append(divs[i])
        list_hero = list()
        for i in list_img:
            dat = i.attrs['src'][0:5]
            if (dat == '/hero'):
                # print('dodano do list_hero', i)
                list_hero.append(i.attrs['src'])
        if (len(list_hero) != 0):
            # print('jest')
            dat = link + list_hero[1]
            return dat
        else:
            self.status = 'Sprawdź ciasteczka, zdjęcia się nie zapisują'
            return False

    def download_image(self):
        if(self.image_link != False):
           save_image(self.JWT, self.image_link, self.name, self.time, self.date)
           self.il = self.image_link
           self.image_link = ''
           self.status = 'Zapisano zdjęcie Bolka'
        else:
            self.status = 'Sprawdź ciasteczka, zdjęcia się nie zapisują'

    def take_statistics(self):
        table = self.soup.find_all('table')
        td = table[0].find_all('td')
        stat = list()
        stat2 = list()
        for i in td:
            stat.append(i.text)
        stat.pop()
        stat.pop()
        for i in stat[0:2]:
            stat2.append(i)
        for i in stat[3:]:
            stat2.append(i[0:-1])
        stat2[5] = stat2[5][0:-14]+'exp )'
        return stat2


    def insert_stat(self):
        to_db = [self.name, self.il, self.statistics[2], self.statistics[3]]
        connection = pymysql.connect(host="serwer1970558.home.pl",
                                     user="30795976_ataki",
                                     passwd="D_mMRNmz",
                                     database="30795976_ataki",
                                     cursorclass=pymysql.cursors.DictCursor,
                                     charset='utf8')

        with connection:
            with connection.cursor() as cursor:
                # sql = "UPDATE `cookies` SET`cookie` = %s WHERE `ID` = 1"
                sql = "INSERT INTO `skany` (`id`, `name`, `link_img`, `pop`, `off`, `deff`, `herolvl`, `czas`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"

                update = (self.name, self.il, self.statistics[2], self.statistics[3], self.statistics[4], self.statistics[5], self.time)
                # sql = "Select * FROM yamahuya"
                cursor.execute(sql, update)

            connection.commit()


    def destruction(self):
        # self.JWT = ''
        # self.status = ''
        # self.name = ''
        # self.link = ''
        # self.image = ''
        self.soup = ''
        # self.time = ''
        # self.date = ''
        self.image_link = ''
        # self.statistics = ''

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def take_scans(self):
        connection = pymysql.connect(host="serwer1970558.home.pl",
                                     user="30795976_ataki",
                                     passwd="D_mMRNmz",
                                     database="30795976_ataki",
                                     cursorclass=pymysql.cursors.DictCursor,
                                     charset='utf8')

        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM `skany` where name = %s'
                cursor.execute(sql, (self.name,))
                result = cursor.fetchall()
                res = result[-2]
        return res

    def check_chage_stat(self):
        l_off = self.last_scan['off']
        l_l_i = self.last_scan['link_img']
        now_off = self.statistics[3]
        now_hero_exp = self.statistics[5]

        if (l_l_i != self.il and l_off != now_off):
            self.status_last_scan = "Zmieniły się punkty off oraz bohater gracza"
        # else:
        #     self.status_last_scan = "Bez zmian"

        if(l_off != now_off):
            self.status_last_scan = "Zmieniły się punkty off gracza"
        # else:
        #     self.status_last_scan = "Bez zmian"

        if (l_l_i != self.il):
            self.status_last_scan = "Gracz majstrował przy Bolku"
        # else:
        #     self.status_last_scan = "Bez zmian"
        # self.status_last_scan = l_l_i+'\n'+now_hero
