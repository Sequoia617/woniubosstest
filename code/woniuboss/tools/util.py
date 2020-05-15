# 创建工具类
class Utility:

    # 从文本中读取内容
    @classmethod
    def get_txt(cls, path):
        with open(path, encoding='utf8') as file:
            contents = file.readlines()
        return contents

    # 将原始[str1,str2]进行转化
    @classmethod
    def trans_str(cls, path):
        contents = cls.get_txt(path)
        li = []
        for content in contents:
            if not content.startswith("#"):
                s = content.strip()
                li.append(s)
        return li

    # 读取json内容,返回原始的数据类型
    @classmethod
    def get_json(cls, path):
        import json
        with open(path, encoding='utf8') as file:
            contents = json.load(file)
        return contents

    # 从测试数据配置文件中读取测试数据内容,返回json格式数据
    @classmethod
    def get_testinfo(cls, conf):
        import xlrd
        workbook = xlrd.open_workbook(conf['TESTINFO_PATH'])
        contents = workbook.sheet_by_name(conf['SHEETNAME'])
        testinfo = []
        for i in range(conf['START_ROW'], conf['END_ROW']):
            testdata = contents.cell(i, conf['TESTDATA_COL']).value
            expect = contents.cell(i, conf['EXPECT_COL']).value
            temp = testdata.split('\n')
            dict = {}
            for t in temp:
                dict[t.split('=')[0]] = t.split('=')[1]
                dict['expect'] = expect
            testinfo.append(dict)

        return testinfo

    # 将json格式数据转化为列表+元组，用于unittest框架参数化
    @classmethod
    def trans_tuple(cls, conf):
        json_info = cls.get_testinfo(conf)
        li = []
        for info in json_info:
            # 通过tuple(dict.values())将字典的值转化为元组的值
            tup = tuple(info.values())
            li.append(tup)
        return li

    # 生成随机数
    @classmethod
    def get_random_num(cls, start, end):
        import random
        return random.randint(start, end)

    # 获取当前系统时间
    @classmethod
    def get_ctime(cls):
        import time
        return time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

    # 创建数据库连接
    @classmethod
    def getConn(cls):
        import pymysql
        return pymysql.connect('172.16.5.33', 'root', '123456', 'agileone', charset='utf8')

    # 查询一条记录
    @classmethod
    def query_one(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchone()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result

    # 查询多条记录
    @classmethod
    def query_all(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result

    # 增删改操作
    @classmethod
    def update_data(cls, sql):
        flag = False
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            flag = True
        finally:
            cur.close()
            conn.close()
            return flag


if __name__ == '__main__':
    print(Utility.get_ctime())
