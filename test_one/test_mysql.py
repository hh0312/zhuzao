import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='huihui000312...', charset='utf8')
cursor = conn.cursor()

# 查看数据库
cursor.execute("show databases")
result = cursor.fetchall()
print(result)

# 创建数据库
cursor.execute("")
