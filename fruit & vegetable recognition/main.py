# -*- coding: utf-8 -*-
"""Fruits & Vegetables Image Recognition

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ngf7Ae9mExUc847c8ZHu-waubU0lJqIv
"""

!nvidia-smi

# Commented out IPython magic to ensure Python compatibility.
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.express as px
plt.style.use('seaborn-darkgrid')
plt.style.use('dark_background')
plt.rc('figure', figsize=(10,10))
plt.rc('font', size=14)
plt.rc('lines', markersize=16)
import warnings 
warnings.filterwarnings('ignore')
import cv2
from google.colab.patches import cv2_imshow
import sklearn
from sklearn.model_selection import train_test_split
import tensorflow as tf
import datetime
!rm -rf ./logs/
# %load_ext tensorboard
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras import Sequential, layers, models
from tensorflow.keras import activations, losses, optimizers, metrics
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.activations import relu, sigmoid, softmax
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

from google.colab import files
uploaded = files.upload()

os.environ['KAGGLE_USERNAME'] = "ashokkumarbibbab"
os.environ['KAGGLE_KEY'] = "5eb29961f66e7dbd74e811a8f3cac56b"

!kaggle datasets download -d moltean/fruits

from zipfile import ZipFile

file_path = '/content/fruits.zip'
with ZipFile(file_path, 'r') as zip:
  print('Extracting...')
  zip.extractall()
  print('Done')

img = cv2.imread('/content/fruits-360_dataset/fruits-360/Training/Apple Red 3/100_100.jpg')
cv2_imshow(img)

os.chdir('/content/fruits-360_dataset/fruits-360')
os.getcwd()

plt.rc('figure', figsize=(5,5))
CATEGORIES = list(os.listdir('/content/fruits-360_dataset/fruits-360/Training'))
DATADIR = '/content/fruits-360_dataset/fruits-360/Training'

for category in CATEGORIES:
  path = os.path.join(DATADIR, category)
  img_path = os.listdir(path)
  for img in img_path[0:1]:
    print('File Name:', img,'Name:',category)
    #gray_img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
    rgb_img_array = cv2.imread(os.path.join(path, img))
    rgb_img_array = cv2.resize(rgb_img_array, (256,256))
    cv2_imshow(rgb_img_array)
    print('')
    plt.show()
    break

imgs_count = []

for category in CATEGORIES:
  path = os.path.join(DATADIR, category)
  img_count = len(os.listdir(path))
  print('Count:',img_count,'--','Name:',category)
  val = (category, img_count)
  imgs_count.append(val)

img_counts = pd.DataFrame(imgs_count, columns=['Fruits','Counts'])
img_counts

fig = px.scatter(data_frame=img_counts, x='Fruits', y='Counts', color='Fruits', template='plotly_dark')
fig.show()

fig = px.bar(data_frame=img_counts, x='Fruits', y='Counts', color='Fruits', template='plotly_dark')
fig.show()

image_size = (200,200)
batch_size = 32
 
train_data = tf.keras.preprocessing.image_dataset_from_directory(
                                        "/content/fruits-360_dataset/fruits-360/Training",
                                        validation_split=0.050,
                                        subset="training",
                                        seed=1337,
                                        image_size=image_size,
                                        batch_size=batch_size,
                                                         )
 
 
validation_data = tf.keras.preprocessing.image_dataset_from_directory(
                                        "/content/fruits-360_dataset/fruits-360/Validation",
                                        validation_split=0.9,
                                        subset="validation", 
                                        seed=1337,
                                        image_size=image_size,
                                        batch_size=batch_size,
                                                              )

label_dict = train_data.class_names

plt.figure(figsize=(20, 20))
for images, labels in train_data.take(1):
    for i in range(12):
        ax = plt.subplot(3, 4, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")

model = tf.keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(200, 200, 3)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(131, activation='softmax')
    
])
keras.utils.plot_model(model, show_shapes=True)

model.summary()

img_path='/content/OIP (8).jpg'
img = image.load_img(img_path, target_size = (200, 200))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis = 0)
img_tensor = img_tensor / 255.

# Print image tensor shape
print(img_tensor.shape)

# Print image
plt.rc('figure', figsize=(5,5))
plt.imshow(img_tensor[0])
plt.show()

plt.rc('figure', figsize=(20,20))

select_layer = model.layers[3:] #select the layers here
layer_outputs = [layer.output for layer in select_layer]
activation_model = models.Model(inputs = model.input, outputs = layer_outputs)
activations = activation_model.predict(img_tensor)
first_layer_activation = activations[0]
#print(first_layer_activation.shape)
for i in range(32):
  ax = plt.subplot(4,8, i + 1)
  plt.imshow(first_layer_activation[0, :, :, i], cmap='rainbow')
  #plt.title(lay_name)
  plt.axis("off")
  #plt.colorbar()
lay_name = []
for lay in select_layer:
  lay_name.append(lay.name)
print('outputs>>>','layer_name:',lay_name[0],'\t','layer_shape:',first_layer_activation.shape)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

checkpoint_filepath = 'model-{epoch:03d}.h5'
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath)

model.fit(train_data, validation_data=validation_data, epochs=5, callbacks=[model_checkpoint_callback])

img_path='/content/OIP (8).jpg'
img = image.load_img(img_path, target_size = (200,200))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis = 0)
img_tensor = img_tensor / 255.

# Print image tensor shape
print(img_tensor.shape)

# Print image
plt.rc('figure', figsize=(5,5))
plt.imshow(img_tensor[0])
plt.show()

plt.rc('figure', figsize=(20,20))

select_layer = model.layers[4:] #select the layers here
layer_outputs = [layer.output for layer in select_layer]
activation_model = models.Model(inputs = model.input, outputs = layer_outputs)
activations = activation_model.predict(img_tensor)
first_layer_activation = activations[0]
#print(first_layer_activation.shape)
for i in range(32):
  ax = plt.subplot(4,8, i + 1)
  plt.imshow(first_layer_activation[0, :, :, i], cmap='rainbow')
  #plt.title(lay_name)
  plt.axis("off")
  #plt.colorbar()
lay_name = []
for lay in select_layer:
  lay_name.append(lay.name)
print('layer_name:',lay_name[0],'\t','layer_shape:',first_layer_activation.shape)

layer_names = []
for layer in model.layers[:8]:
  layer_names.append(layer.name)
  print(layer_names)

layer_outputs = [layer.output for layer in model.layers]
layer_outputs

model.evaluate(train_data)

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(train_data, 
          epochs=2, 
          validation_data=validation_data, 
          callbacks=[tensorboard_callback])

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs/fit

model = load_model('/content/fruits-360_dataset/fruits-360/model-005.h5')

plt.rc('figure', figsize=(10,10))
file_path = '/content/OIP (6).jpg'

img = keras.preprocessing.image.load_img(
    file_path, target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis
 
predictions = model.predict(img_array)
score = predictions[0]
classes = []
for labels in label_dict:
    classes.append(labels)
classes = np.array(pd.DataFrame(classes))
print('Predicted:',predictions.argmax())
print('Score:',score.argmax())
imgs = plt.imread(file_path)
plt.imshow(imgs)
print('Class Name Predicted:', classes[predictions.argmax()])