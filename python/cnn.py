from __future__ import absolute_import 
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

tf.logging.set_verbosity(tf.logging.INFO)

def cnn_model_fn():
    input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])
    conv1 = tf.layers.conv2d(inputs=input_layer,
        filters=32,
        kernel_size=[5,5],
        padding='same',
        activation=tf.nn.relu)
    pool1 = tf.nn.max_pooling2d(inputs=conv1,
        pool_size=[2,2], strides=2)
    conv2 = tf.layers.conv2d(inputs=pool1,
        filters=64,
        kernel_size=[5,5],
        padding='same',
        activation=tf.nn.relu)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)])
    pool2_flat = tf.reshape(pool2, [-1, 7*7*64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(
          inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)


if __name__ == '__main__':
    tf.app.run()
