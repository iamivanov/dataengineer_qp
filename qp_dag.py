import pg8000
import datetime

dbname = 'postgres'
user = 'ivanov'
password = 'r2q4e'
host = '192.168.77.21'
port = 5432

counter = 0

try:
    # пытаемся подключиться к базе данных
    conn = pg8000.connect(
        database = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )
    cursor = conn.cursor()
    #cursor.execute('SELECT message, recieved FROM ivanov_traps_raw WHERE date=%s', (datetime.date(2023, 10, 10),))
    cursor.execute('SELECT message, recieved FROM ivanov_traps_raw WHERE date=%s LIMIT 10', (datetime.date(2023, 10, 10),))
    while True:
        rows = cursor.fetchmany(100)
        if not rows:
            break
        for row in rows:
            counter+=1
            print(counter)
            print(row)

except:
    print('Can`t establish connection to database')

finally:
    conn.close()
