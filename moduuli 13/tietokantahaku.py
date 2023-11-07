import mysql.connector


def connectDB():

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='username',
        password='password',
        autocommit=True
    )
    return connection


def get_ICAO(code):
    connection = connectDB()
    sql = "select name, municipality from airport where ident='" + code + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    if cursor.rowcount > 0:
        return result
    else:
        return 'not found' 'not found'


# pääohjelma
# icao = input('Anna ICAO, esim. EFHK: ')
# get_ICAO(icao)

