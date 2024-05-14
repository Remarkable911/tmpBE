import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,
    blocking=True,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='tmpsql',
    charset='utf8'
)


# 执行sql语句
def execute_query(sql, params=None, fetchone=False):
    # 连接数据库
    conn = POOL.connection()

    # 创建游标对象，使用字典格式返回查询结果
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL查询
    cursor.execute(sql, params)
    # 根据fetchone参数选择返回结果的方式
    if fetchone:
        # 返回一条查询结果
        result = cursor.fetchone()
    else:
        # 返回所有查询结果
        result = cursor.fetchall()
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    # 返回查询结果
    return result
