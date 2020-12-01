import pymysql

def get_list(query, args):
    '''

    :param query: sql 语句
    :param args: sql语句的参数
    :return: sql查询出来的元组
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           password='', database='testvth', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _tmp = cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_one(query, args):
    '''

    :param query: sql 语句
    :param args: sql语句的参数
    :return: sql查询出来的元组(1条数据)
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           password='', database='testvth', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _tmp = cursor.execute(query, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify(query, args):
    '''

    :param query: sql语句
    :param args: sql语句的参数
    :return: 不返回
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           password='', database='testvth', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _tmp = cursor.execute(query, args)
    conn.commit()
    cursor.close()
    conn.close()