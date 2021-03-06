# A direct copy from tf examples

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

learning_rate = .01
training_epochs = 1000
display_step = 50

train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

X = tf.placeholder('float')
Y = tf.placeholder('float')

W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# init model
pred = tf.add(tf.multiply(X, W), b)

# cost function
cost = tf.reduce_sum(tf.pow(pred - Y, 2))/(2*n_samples) # why 2 * n?

# gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Fit
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X:x, Y:y}) # Note we can feed any shape because unspecified

        # Logs
        if (epoch + 1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y: train_Y}) # cost of current setting
            print "Epoch: ", '%04d' %(epoch+1), "cost = ", "{:.9f}".format(c), "W=", sess.run(W), "b=", sess.run(b)

    print 'finish training'
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y}) # cost of end setting
    print "Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n'

    #Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

# Questions
# - Tensorboard? (Tabled for a later example)
# - Why does cost function use 2 * n for mean? UNRESOLVED

