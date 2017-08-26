# -*- encoding: utf-8 -*-
'''
张量是tensorflow的数据模型
会话是tensorflow的运行模型

简言之：
tensorflow编程模型共有３种：
计算模型，数据模型，运行模型。

张量的定义，顾名思义，张量就是保存计算的结果的引用。
会话是用来组织数据和运算的。
计算图是在会话中被计算的。
变量是在计算图中存在的。
当然tensorflow中还有一个常量的定义。

还有，张量也可以脱离会话。
'''

import tensorflow as tf
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = tf.add(a, b, name='add')
print(type(a))
print(result)

# method 1
sess = tf.Session()
with sess.as_default():
    print(result.eval())

# method 2
sess = tf.Session()
sess.run(result)
print(result.eval(session=sess))

# method 3 
meses = tf.InteractiveSession()
print(result.eval())
ses.close()
