'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-12-04 00:39:04
@LastEditTime: 2019-12-04 00:45:05
@LastEditors: 
'''

import tensorflow as tf

physical_devices = tf.config.list_physical_devices("GPU")
for i in range(len(physical_devices)):
    tf.config.experimental.set_memory_growth(physical_devices[i], True)
strategy = tf.distributions.OneDeviceStrategy(device="/gpu:0")

with strategy.scope():
    a = tf.ones([1,5,5])
    b = tf.ones([1,5,10])
    c = tf.nn.matmul(a, b)
    print(c.device)
    print(c)