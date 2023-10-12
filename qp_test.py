import pg8000
import datetime

dbname = 'postgres'
user = 'ivanov'
password = 'r2q4e'
host = '192.168.77.21'
port = 5432

counter = 0

conn = pg8000.connect(
        database = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )

cursor = conn.cursor()
cursor.execute('SELECT message, recieved FROM ivanov_traps_raw WHERE date=%s LIMIT 2', (datetime.date(2023, 10, 10),))

device_sql = 'INSERT INTO ivanov_traps_devices VALUES (%s, %s)'
message_sql = 'INSERT INTO ivanov_traps_messages VALUES (%s, %s, %s)'
oids_sql = 'INSERT INTO ivanov_traps_oids VALUES (%s, %s, %s, %s)'

while True:
    rows = cursor.fetchmany(100)
    if not rows:
        break
    for row in rows:
        counter+=1
        #print(counter)
        #print(row[0])
        
        message = row[0]
        device = {'id': message['device_id'], 'remote_device_id': message['remote_device_id']}
        
        #check devices
        cursor2 = conn.cursor()
        cursor2.execute('SELECT id FROM ivanov_traps_devices WHERE id=%s', (message['device_id'],))
        devices = cursor2.fetchone()
        if devices == None:
            #creating device
            cursor2.execute(device_sql, (message['device_id'], message['remote_device_id'],))
            conn.commit()
        
        #check messages
        cursor2.execute('SELECT id FROM ivanov_traps_messages WHERE id=%s', (message['id'],))
        messages = cursor2.fetchone()
        if messages == None:
            #creating message
            cursor2.execute(message_sql, (message['id'], message['device_id'], row[1],))
            conn.commit()
        
        #check oids
        cursor2.execute('SELECT id FROM ivanov_traps_oids WHERE message_id=%s', (message['id'],))
        if messages == None:
            for oid in message['oids']:
                cursor2.execute(oids_sql, (oids['oid'], oids['value'], oids['value_raw'], message['id']))
        
        #print(device)
        #trap = {'id': message['id'], 'time': 'null'}
        #print(trap)
        #for oid in message['oids']:
            #t_oid = {'id': 'null', 'trap_id': message['id'], 'oid': oid['oid'], 'value': oid['value'], 'value_raw': oid['value_raw']}
            #print(t_oid)
conn.close()