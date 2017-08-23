# -*- coding: utf-8 -*-
import sqlite3
import random
import time
import sys

XRANGE = range
if sys.platform.startswith('2.7'):
    XRANGE = xrange


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
    try:
        tb_name = '1_1'
        sql = '''
            create table tb_%s(
            id int primary key,
            shape text,
            crust_size text,
            crust_shade text,
            filling_size text,
            filling_shade text,
            category text)
            ''' % tb_name
        print(sql)
        c.execute(sql)
    except:
        pass
    finally:
        c.close()
        conn.close()


def insert_ex(tb_name, sample):
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    args = (
        tb_name,
        sample.shape,
        sample.crust_size,
        sample.crust_shade,
        sample.filling_size,
        sample.filling_shade,
        sample.category, )
    sql = ("insert into %s(shape, crust_size, crust_shade, filling_size,"
           "filling_shade, category) values('%s','%s','%s','%s','%s','%s')")
    sql = sql % args
    print(sql)
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def select_shape(tb_name, shape_ex):
    # pudb.set_trace()
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    pos_shape = ("select count(*) as pos_shape from %s where shape='%s' and "
                 "category='pos'" % (tb_name, shape_ex))
    c.execute(pos_shape)
    result = c.fetchone()
    pos_shape = float(result[0])

    shape = ("select count(*) as shape from %s where shape='%s'" % (tb_name,
                                                                    shape_ex))
    c.execute(shape)
    result = c.fetchone()
    shape = float(result[0])

    # 1
    pos_shape__shape = pos_shape / shape
    print('input: shape=%s' % shape_ex)
    print('P(pos|shape=%s) / P(shape=%s) = %f' % (pos_shape, shape,
                                                  pos_shape__shape))

    neg_shape = ("select count(*) as neg_shape from %s where shape='%s' and"
                 " category='neg'" % (tb_name, shape_ex))
    c.execute(neg_shape)
    result = c.fetchone()
    neg_shape = float(result[0])

    # 2
    neg_shape__shape = neg_shape / shape
    print('P(neg|shape=%s) / P(shape=%s) = %f' % (neg_shape, shape,
                                                  neg_shape__shape))

    c.close()
    conn.close()
    print('output:')
    if pos_shape__shape > neg_shape__shape:
        return 'pos'
    else:
        return 'neg'


def generate_train_data():
    init_db()
    for j in XRANGE(1):
        for i in XRANGE(random.randint(10, 100)):
            shape = random.sample(['circle', 'triangle', 'square'], 1)[0]
            crust_size = random.sample(['thick', 'thin'], 1)[0]
            crust_shade = random.sample(['gray', 'white', 'dark'], 1)[0]
            filling_size = random.sample(['thick', 'thin'], 1)[0]
            filling_shade = random.sample(['white', 'gray', 'dark'], 1)[0]
            category = random.sample(['pos', 'neg'], 1)[0]

            sample = Sample(shape, crust_size, crust_shade, filling_size,
                            filling_shade, category)
            insert_ex(tb_name, sample)
        time.sleep(1)


if __name__ == '__main__':
    tb_name = 'tb_1_1'
    generate_train_data()
    print(select_shape(tb_name, 'circle'))
