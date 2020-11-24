import tensorflow as tf
import numpy as np
import os
import cv2
from numpy import genfromtxt
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
import h5py
import matplotlib.pyplot as plt
import Database as db
import mysql.connector
import datetime

_FLOATX = 'float32'


def variable(value, dtype=_FLOATX, name=None):
    v = tf.Variable(np.asarray(value, dtype=dtype), name=name)
    _get_session().run(v.initializer)
    return v


def shape(x):
    return x.get_shape()


def square(x):
    return tf.square(x)


def zeros(shape, dtype=_FLOATX, name=None):
    return variable(np.zeros(shape), dtype, name)


def concatenate(tensors, axis=-1):
    if axis < 0:
        axis = axis % len(tensors[0].get_shape())
    return tf.concat(axis, tensors)


def LRN2D(x):
    return tf.nn.lrn(x, alpha=1e-4, beta=0.75)


def conv2d_bn(x,
              layer=None,
              cv1_out=None,
              cv1_filter=(1, 1),
              cv1_strides=(1, 1),
              cv2_out=None,
              cv2_filter=(3, 3),
              cv2_strides=(1, 1),
              padding=None):
    num = '' if cv2_out == None else '1'
    tensor = Conv2D(cv1_out, cv1_filter, strides=cv1_strides, data_format='channels_first', name=layer + '_conv' + num)(
        x)
    tensor = BatchNormalization(axis=1, epsilon=0.00001, name=layer + '_bn' + num)(tensor)
    tensor = Activation('relu')(tensor)
    if padding == None:
        return tensor
    tensor = ZeroPadding2D(padding=padding, data_format='channels_first')(tensor)
    if cv2_out == None:
        return tensor
    tensor = Conv2D(cv2_out, cv2_filter, strides=cv2_strides, data_format='channels_first', name=layer + '_conv' + '2')(
        tensor)
    tensor = BatchNormalization(axis=1, epsilon=0.00001, name=layer + '_bn' + '2')(tensor)
    tensor = Activation('relu')(tensor)
    return tensor


WEIGHTS = [
    'conv1', 'bn1', 'conv2', 'bn2', 'conv3', 'bn3',
    'inception_3a_1x1_conv', 'inception_3a_1x1_bn',
    'inception_3a_pool_conv', 'inception_3a_pool_bn',
    'inception_3a_5x5_conv1', 'inception_3a_5x5_conv2', 'inception_3a_5x5_bn1', 'inception_3a_5x5_bn2',
    'inception_3a_3x3_conv1', 'inception_3a_3x3_conv2', 'inception_3a_3x3_bn1', 'inception_3a_3x3_bn2',
    'inception_3b_3x3_conv1', 'inception_3b_3x3_conv2', 'inception_3b_3x3_bn1', 'inception_3b_3x3_bn2',
    'inception_3b_5x5_conv1', 'inception_3b_5x5_conv2', 'inception_3b_5x5_bn1', 'inception_3b_5x5_bn2',
    'inception_3b_pool_conv', 'inception_3b_pool_bn',
    'inception_3b_1x1_conv', 'inception_3b_1x1_bn',
    'inception_3c_3x3_conv1', 'inception_3c_3x3_conv2', 'inception_3c_3x3_bn1', 'inception_3c_3x3_bn2',
    'inception_3c_5x5_conv1', 'inception_3c_5x5_conv2', 'inception_3c_5x5_bn1', 'inception_3c_5x5_bn2',
    'inception_4a_3x3_conv1', 'inception_4a_3x3_conv2', 'inception_4a_3x3_bn1', 'inception_4a_3x3_bn2',
    'inception_4a_5x5_conv1', 'inception_4a_5x5_conv2', 'inception_4a_5x5_bn1', 'inception_4a_5x5_bn2',
    'inception_4a_pool_conv', 'inception_4a_pool_bn',
    'inception_4a_1x1_conv', 'inception_4a_1x1_bn',
    'inception_4e_3x3_conv1', 'inception_4e_3x3_conv2', 'inception_4e_3x3_bn1', 'inception_4e_3x3_bn2',
    'inception_4e_5x5_conv1', 'inception_4e_5x5_conv2', 'inception_4e_5x5_bn1', 'inception_4e_5x5_bn2',
    'inception_5a_3x3_conv1', 'inception_5a_3x3_conv2', 'inception_5a_3x3_bn1', 'inception_5a_3x3_bn2',
    'inception_5a_pool_conv', 'inception_5a_pool_bn',
    'inception_5a_1x1_conv', 'inception_5a_1x1_bn',
    'inception_5b_3x3_conv1', 'inception_5b_3x3_conv2', 'inception_5b_3x3_bn1', 'inception_5b_3x3_bn2',
    'inception_5b_pool_conv', 'inception_5b_pool_bn',
    'inception_5b_1x1_conv', 'inception_5b_1x1_bn',
    'dense_layer'
]

conv_shape = {
    'conv1': [64, 3, 7, 7],
    'conv2': [64, 64, 1, 1],
    'conv3': [192, 64, 3, 3],
    'inception_3a_1x1_conv': [64, 192, 1, 1],
    'inception_3a_pool_conv': [32, 192, 1, 1],
    'inception_3a_5x5_conv1': [16, 192, 1, 1],
    'inception_3a_5x5_conv2': [32, 16, 5, 5],
    'inception_3a_3x3_conv1': [96, 192, 1, 1],
    'inception_3a_3x3_conv2': [128, 96, 3, 3],
    'inception_3b_3x3_conv1': [96, 256, 1, 1],
    'inception_3b_3x3_conv2': [128, 96, 3, 3],
    'inception_3b_5x5_conv1': [32, 256, 1, 1],
    'inception_3b_5x5_conv2': [64, 32, 5, 5],
    'inception_3b_pool_conv': [64, 256, 1, 1],
    'inception_3b_1x1_conv': [64, 256, 1, 1],
    'inception_3c_3x3_conv1': [128, 320, 1, 1],
    'inception_3c_3x3_conv2': [256, 128, 3, 3],
    'inception_3c_5x5_conv1': [32, 320, 1, 1],
    'inception_3c_5x5_conv2': [64, 32, 5, 5],
    'inception_4a_3x3_conv1': [96, 640, 1, 1],
    'inception_4a_3x3_conv2': [192, 96, 3, 3],
    'inception_4a_5x5_conv1': [32, 640, 1, 1, ],
    'inception_4a_5x5_conv2': [64, 32, 5, 5],
    'inception_4a_pool_conv': [128, 640, 1, 1],
    'inception_4a_1x1_conv': [256, 640, 1, 1],
    'inception_4e_3x3_conv1': [160, 640, 1, 1],
    'inception_4e_3x3_conv2': [256, 160, 3, 3],
    'inception_4e_5x5_conv1': [64, 640, 1, 1],
    'inception_4e_5x5_conv2': [128, 64, 5, 5],
    'inception_5a_3x3_conv1': [96, 1024, 1, 1],
    'inception_5a_3x3_conv2': [384, 96, 3, 3],
    'inception_5a_pool_conv': [96, 1024, 1, 1],
    'inception_5a_1x1_conv': [256, 1024, 1, 1],
    'inception_5b_3x3_conv1': [96, 736, 1, 1],
    'inception_5b_3x3_conv2': [384, 96, 3, 3],
    'inception_5b_pool_conv': [96, 736, 1, 1],
    'inception_5b_1x1_conv': [256, 736, 1, 1],
}


def load_weights_from_FaceNet(FRmodel):
    # Load weights from csv files (which was exported from Openface torch model)
    weights = WEIGHTS
    weights_dict = load_weights()

    # Set layer weights of the model
    for name in weights:
        if FRmodel.get_layer(name) != None:
            FRmodel.get_layer(name).set_weights(weights_dict[name])
        elif model.get_layer(name) != None:
            model.get_layer(name).set_weights(weights_dict[name])


def load_weights():
    # Set weights path
    dirPath = './weights'
    fileNames = filter(lambda f: not f.startswith('.'), os.listdir(dirPath))
    paths = {}
    weights_dict = {}

    for n in fileNames:
        paths[n.replace('.csv', '')] = dirPath + '/' + n

    for name in WEIGHTS:
        if 'conv' in name:
            conv_w = genfromtxt(paths[name + '_w' + "-Copy1"], delimiter=',', dtype=None)
            conv_w = np.reshape(conv_w, conv_shape[name])
            conv_w = np.transpose(conv_w, (2, 3, 1, 0))
            conv_b = genfromtxt(paths[name + '_b' + "-Copy1"], delimiter=',', dtype=None)
            weights_dict[name] = [conv_w, conv_b]
        elif 'bn' in name:
            bn_w = genfromtxt(paths[name + '_w' + "-Copy1"], delimiter=',', dtype=None)
            bn_b = genfromtxt(paths[name + '_b' + "-Copy1"], delimiter=',', dtype=None)
            bn_m = genfromtxt(paths[name + '_m' + "-Copy1"], delimiter=',', dtype=None)
            bn_v = genfromtxt(paths[name + '_v' + "-Copy1"], delimiter=',', dtype=None)
            weights_dict[name] = [bn_w, bn_b, bn_m, bn_v]
        elif 'dense' in name:
            dense_w = genfromtxt(dirPath + '/dense_w-Copy1.csv', delimiter=',', dtype=None)
            dense_w = np.reshape(dense_w, (128, 736))
            dense_w = np.transpose(dense_w, (1, 0))
            dense_b = genfromtxt(dirPath + '/dense_b-Copy1.csv', delimiter=',', dtype=None)
            weights_dict[name] = [dense_w, dense_b]

    return weights_dict


def load_dataset():
    train_dataset = h5py.File('datasets/train_happy.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('datasets/test_happy.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def img_to_encoding(image_path, model):
    img = cv2.imread(image_path, 1)
    img = img[...,::-1]  #BGR to RGB
    img = np.around(np.transpose(img, (2,0,1))/255.0, decimals=12)
    x_train = np.array([img])
    embedding = model.predict_on_batch(x_train)
    return embedding


def triplet_loss(y_pred, alpha=0.2):
    """
    Arguments:
    y_pred -- python list containing three objects:
            anchor -- the encodings for the anchor images, of shape (None, 128)
            positive -- the encodings for the positive images, of shape (None, 128)
            negative -- the encodings for the negative images, of shape (None, 128)

    Returns:
    loss -- real number, value of the loss
    """

    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]

    # Step 1: Compute the (encoding) distance between the anchor and the positive
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    # Step 2: Compute the (encoding) distance between the anchor and the negative
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    # Step 3: subtract the two previous distances and add alpha.
    basic_loss = pos_dist - neg_dist + alpha
    # Step 4: Take the maximum of basic_loss and 0.0. Sum over the training examples.
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0))

    return loss

def verify(image_path, identity, model):
    """
    Function that verifies if the person on the "image_path" image is "identity".

    Arguments:
    image_path -- path to an image
    identity -- string, name of the person you'd like to verify the identity. Has to be an employee who works in the office.
    database -- python dictionary mapping names of allowed people's names (strings) to their encodings (vectors).
    model -- your Inception model instance in Keras

    Returns:
    dist -- distance between the image_path and the image of "identity" in the database.
    Mark_attendance -- True, if the attendance should be marked . False otherwise.
    """

    # Step 1: Compute the encoding for the image. Use img_to_encoding() see example above. (≈ 1 line)
    encoding = img_to_encoding(image_path, model)
    ImageEncoding = np.frombuffer(identity,dtype=np.float32)
    # Step 2: Compute distance with identity's image (≈ 1 line)
    dist = np.linalg.norm(encoding - ImageEncoding)

    # Step 3: Open the door if dist < 0.7, else don't open (≈ 3 lines)
    if dist < 0.7:
        Mark_attendance = True
    else:
        Mark_attendance = False

    return dist, Mark_attendance

def ValidateInfo(name,roll,course,semester,ret=False):
    if roll.startswith("0"):
        roll = roll[1:]
    mydb = mysql.connector.connect(host="localhost",user="arjun",password="wedding9711",database="AttendanceManager")
    mycur = mydb.cursor()
    sql = "select Name,ID,SubjectID,ImageEncoding from Students where Name='{}' and EnrollmentNumber={} and Course='{}' and Semester={}".format(name,roll,course,semester)
    mycur.execute(sql)
    result = list(mycur)
    if ret==False:
        if result:
            return True
        else:
            return False
    elif ret==True:
        if result:
            return result[0][1],result[0][2],result[0][3]
        else:
            return False
    elif ret=="Check":
        if result:
            return result[0][1],result[0][2]
        else:
            return False


def MarkInDatabase(subject,ID):
    CurrentDate = datetime.datetime.now().strftime("%Y-%m-%d")
    mydb = mysql.connector.connect(host="localhost", user="arjun", password="wedding9711", database="AttendanceManager")
    mycur = mydb.cursor()
    sql = "select * from {} where Date=(%s)".format(subject)
    val = (CurrentDate,)
    mycur.execute(sql, val)
    if list(mycur):
        sql = "select * from {} where Date='{}' and PresentID like '%{}%'".format(subject,CurrentDate,ID)
        mycur.execute(sql)
        if list(mycur):
            return "You have already marked your attendance for the subject {}.".format(subject)
        else:
            sql = "select PresentID from {} where Date='{}'".format(subject,CurrentDate)
            mycur.execute(sql)
            mycurl = str(list(mycur)[0][0])
            mycurl = mycurl + "," + str(ID)

            sql = "Update {} SET PresentID = {} where Date = '{}' ".format(subject,mycurl,CurrentDate)
            mycur.execute(sql)
            mydb.commit()
            return "Your attendance has been marked for the subject {}!".format(subject)
    else:
        sql = "Insert into {} (Date,PresentID) VALUES (%s,%s)".format(subject)
        val = (CurrentDate,ID)
        mycur.execute(sql,val)
        mydb.commit()
        return "Your attendance has been marked for the subject {}!".format(subject)
