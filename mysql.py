import pymysql

db = pymysql.connect(host='localhost', user='root', password='19961125', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
#sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'

# id = '20190305'
# user = 'Bob'
# age = 20

# sql = 'INSERT INTO students (id, name, age) VALUES (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()

# data = {
#     'id': '20190306',
#     'name': 'Bob',
#     'age': 21
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# #sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values =values)
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values =values)
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

sql = 'SELECT * FROM students WHERE age >= 20'

# try:
#     cursor.execute(sql)
#     print("Count", cursor.rowcount)
#     one = cursor.fetchone()
#     print('One:', one)
#     results = cursor.fetchall()
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except BaseException as e:
    print("Error" , e)