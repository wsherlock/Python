#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymssql

server = "10.181.100.4"    # 连接服务器地址
user = "cwtobt"            # 连接帐号
password = "Carlson@123"   # 连接密码

# conn = pymssql.connect(server, user, password, "Hippo_Static")  #获取连接
# cursor = conn.cursor() # 获取光标
# cursor.execute('SELECT * FROM AIRLINE_CODE WHERE JS_CODE<>%s', '170')
# row = cursor.fetchone()
# while row:
#     print("ID=%d, Name=%s" % (row[0], row[5]))
#     row = cursor.fetchone()

#for row in cursor:
#    print('row = %r' % (row,))
#conn.close()

with pymssql.connect(server, user, password, "Hippo_Static") as conn:
    with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
        cursor.execute('SELECT * FROM AIRLINE_CODE WHERE JS_CODE<>%s', '170')
        for row in cursor:
            print("JS_CODE=%s, NameEn=%s" % (row["JS_CODE"], row["NameEn"]))

#ticketNo = input("TicketNo:")

# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.')])
#conn.commit()

#dbcursor.execute("update test_student set name =%s where sno =1",'peter pan')
#dbcursor.execute("delete from test_student  where sno =1",'peter pan')
#dbcursor.execute("insert into test_teacher values(%d,%s,%s)",(2,'xingxing','111111'))

#dbcursor.execute("insert into test_teacher values(%d,%s,%s)",(6,'xingxing6','111111'))
#dbcursor.execute("update test_student set name =%s where sno =2",'peter Panpan')
#dbconnect.commit() #提交多个