from pymysql import Connect


class db(object):
    def __init__(self):
        self.conn = Connect(host='mysql', user='root', password='root', database='visual_db_2017', port=3306)

    def get_cur(self, sql):
        """
        向数据库查询sql语句
        :param sql: 需要查询的sql语法   ：string
        :return: 返回结果游标
        """
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.close()
        return cur


if __name__ == '__main__':
    # 新增查询测试
    sql = 'select sum(confirmed_add), update_time from covid_data_2017 group by update_time'
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()

    for confirmed, date in data:
        import datetime
        if date == datetime.date(2020, 2, 13):
            continue
        else:
            print(confirmed, date)
    # 连接测试
    # mydb = db()
    # sql = 'select * from area_china limit 10'
    # cur = mydb.get_cur(sql)
    #
    # data = cur.f()
    # print(data)