# -*- coding: utf-8 -*-
'''
tensorflow的程序分为两个阶段，第一是定义输入，也就是在计算图中定义量，
第二是在计算图中读取输入并处理后，输出; 

在这个程序中，首先定义了两个计算图，然后分别在计算图中定义两个变量v,
最后分别在不同的会话中读取变量，并输出。

由此可以概括，tensorflow的程序开发

首先是，定义计算图，
然后是，在指定计算图的会话中计算
'''
import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a + b
print result
# 通过a.graph可以查看张量所属的计算图。因为没有特意指定，所以计算图应该等于
# 当前默认的计算图。所以下面这个操作输出值为True
print a.graph is tf.get_default_graph()

g1 = tf.Graph()
with g1.as_default():
    # v = tf.get_variable('v', initializer=tf.zeros_initializer(shape=[1]))
    # https://stackoverflow.com/questions/44946189/typeerror-init-got-an-unexpected-keyword-argument-shape
    # 在计算图g1中定义变量'v', 并设置初始值为0
    v = tf.get_variable('v', shape=[1], initializer=tf.zeros_initializer)

g2 = tf.Graph()
with g2.as_default():
    # v = tf.get_variable('v', initializer=tf.ones_initializer(shape=[1]))
    # 在计算图g2中定义变量'v', 并设置初始值为0
    v = tf.get_variable('v', shape=[1], initializer=tf.ones_initializer)

# 在计算图g1中读取变量'v'的值
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('', reuse=True):
        print sess.run(tf.get_variable('v'))

# 在计算图g2中读取变量'v'的值
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('', reuse=True):
        print sess.run(tf.get_variable('v'))


g = tf.Graph()
# 指定计算运行的设备
with g.device('/gpu:0'):
    result = a + b
    print result
