import pymysql.cursors
from Bolek import Hero
from datetime import datetime
import datetime



def take_one_hero(all_users, name, JWT, timee):
    for i in all_users:
        if(i['name'].lower() == name.lower()):
            obj = Hero(i, JWT, timee)
            return obj


def bazaDanych():
    global all_users
    all_users = list()
    global cookies_user
    connection = pymysql.connect(host="serwer1970558.home.pl",
                         user="30795976_ataki",
                         passwd="D_mMRNmz",
                         database="30795976_ataki",
                         cursorclass=pymysql.cursors.DictCursor,
                         charset='utf8')


    with connection:
        with connection.cursor() as cursor:
            #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            sql = "Select * FROM yamahuya"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                all_users.append(i)
            sql = "Select `cookie` FROM cookies Where `id` = '1'"
            cursor.execute(sql)
            cookies_user = cursor.fetchone()

        connection.commit()

    return all_users, cookies_user

def addCookie(cookie):
    connection = pymysql.connect(host="serwer1970558.home.pl",
                         user="30795976_ataki",
                         passwd="D_mMRNmz",
                         database="30795976_ataki",
                         cursorclass=pymysql.cursors.DictCursor)


    with connection:
        with connection.cursor() as cursor:
            # sql = "INSERT INTO `cookies` (`name`, `cookie`) VALUES (%s, %s)"
            sql = "UPDATE `cookies` SET`cookie` = %s WHERE `ID` = 1"

            update = (cookie,)
            # sql = "Select * FROM yamahuya"
            cursor.execute(sql, update)

        connection.commit()







def insertBLOB(name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = pymysql.connect(host="serwer1970558.home.pl",
                                     user="30795976_ataki",
                                     passwd="D_mMRNmz",
                                     database="30795976_ataki",
                                     cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO images
                          ( name, photo, biodata) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# resul = take_scans('oprawca')
#
# for i in resul:
#     print(i)
