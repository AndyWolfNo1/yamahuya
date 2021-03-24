import pymysql.cursors

connection = pymysql.connect(host="serwer1970558.home.pl",
                                     user="30795976_ataki",
                                     passwd="D_mMRNmz",
                                     database="30795976_ataki",
                                     cursorclass=pymysql.cursors.DictCursor)


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

with connection.cursor() as cursor:
    sql = "SELECT `img` FROM `img` WHERE 1"
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    write_file(result['img'], 'transfer.png')


#file = open('zapisany.png', 'wb')

#file.write(result)
#file.close()
