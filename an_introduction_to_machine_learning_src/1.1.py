# -*- coding: utf-8 -*-
import sqlite3
import random
import time


class Sample(object):
    def __init__(self, shape, crust_size, crust_shade, filling_size,
                 filling_shade, category):
        self.shape = shape
        self.crust_size = crust_size
        self.crust_shade = crust_shade
        self.filling_size = filling_size
        self.filling_shade = filling_shade
        self.category = category


def init_db():
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    tb_name = int(time.time())
    sql = '''
        create table tb_%d(
        id int primary key,
        shape text,
        crust_size text,
        crust_shade text,
        filling_size text,
        filling_shade text,
        category text)
        '''% tb_name
    print(sql)
    c.execute(sql)
    c.close()
    return 'tb_' + str(tb_name)


def insert_ex(tb_name, sample):
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    args = (tb_name, sample.shape, sample.crust_size, sample.crust_shade,
            sample.filling_size, sample.filling_shade, sample.category,)
    sql = ("insert into %s(shape, crust_size, crust_shade, filling_size,"
           "filling_shade, category) "
           "values('%s','%s','%s','%s','%s','%s')")
    sql = sql % args
    print(sql)
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()

def generate_train_data():
    tbs = []
    for j in range(10):
        tb_name = init_db()
        tbs.append(tb_name)
        for i in xrange(random.randint(10, 100)):
            shape = random.sample(['circle', 'triangle', 'square'], 1)[0]
            crust_size = random.sample(['thick', 'thin'], 1)[0]
            crust_shade = random.sample(['gray', 'white', 'dark'], 1)[0]
            filling_size = random.sample(['thick', 'thin'], 1)[0]
            filling_shade = random.sample(['white', 'gray', 'dark'], 1)[0]
            category = random.sample(['pos', 'neg'], 1)[0]

            sample = Sample(shape, crust_size, crust_shade,
                                filling_size, filling_shade, category)
            insert_ex(tb_name, sample)
        time.sleep(1)
    return tbs

def train_model(tbs):
    pass

if __name__ == '__main__':
    tbs = generate_train_data()
    train_model(tbs)
