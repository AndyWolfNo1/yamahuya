import pymysql.cursors
import time
import sys


connection = pymysql.connect(host="serwer1970558.home.pl",
                                     user="30795976_ataki",
                                     passwd="D_mMRNmz",
                                     database="30795976_ataki",
                                     cursorclass=pymysql.cursors.DictCursor)


with open('op.png', 'rb') as file:
        binaryData = file.read()


def wyslij():
    sql = "UPDATE `img` SET `img` = %s WHERE `img`.`id` = 1;"
    tupla = (binaryData,)
    with connection.cursor() as cursor:
        #sql = "Select * FROM yamahuya"
        cursor.execute(sql, tupla)
        #result = cursor.fetchall()
        connection.commit()
        print('wysłano')
        return True

    
wyslij()
