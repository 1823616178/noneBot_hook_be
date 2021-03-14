import pymysql

db = pymysql.connect(host='192.168.123.100',port=3306,user='sun',passwd= '550312171',database='hook')
cursor = db.cursor()

def QueryMobole(mobile):
    # 使用 execute()  方法执行 SQL 查询
    sql = "SELECT username,mobile FROM 8eqq WHERE mobile='{}'".format(str(mobile).strip())
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    except Exception:
        print(Exception)
        return None
    db.close()

def QueryQQ(QQ):
    # 使用 execute()  方法执行 SQL 查询
    sql = "SELECT username,mobile FROM 8eqq WHERE username='{}'".format(str(QQ).strip())
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    except Exception:
        print(Exception)
        return None
    db.close()

def QueryWeibo(mobile):
    # 使用 execute()  方法执行 SQL 查询
    sql = "SELECT uid ,mobile FROM weibo WHERE mobile='{}'".format(str(mobile).strip())
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    except Exception:
        print(Exception)
        return None
    db.close()

def QueryWeiboAll(item):
    uidArr = ()
    for it in item:
        itms = QueryWeibo(it[1])
        if len(itms) > 0:
            uidArr = uidArr + (itms)

    return uidArr
