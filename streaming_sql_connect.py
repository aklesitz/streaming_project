import psycopg2

hostname = input('hostname: ')
database = input('database: ')
username = input('username: ')
pwd = input('password: ')
port_id = input('port number: ')
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS streaming')

    create_script = ''' CREATE TABLE IF NOT EXISTS streaming (
                       #columns#
                       #columns#
                       #columns#'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO streaming (#columns#) VALUES (#values#)'
    insert_value = 
    for record in insert_value:
        cur.execute(insert_script, record)

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
    conn.close()