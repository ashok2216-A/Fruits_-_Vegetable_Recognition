# Data Info

## Fruits_-_Vegetable_Recognition

Fruits 360 dataset: A dataset of images containing fruits and vegetables
Version: 2020.05.18.0
Content
The following fruits and are included:
Apples (different varieties: Crimson Snow, Golden, Golden-Red, Granny Smith, Pink Lady, Red, Red Delicious), Apricot, Avocado, Avocado ripe, Banana (Yellow, Red, Lady Finger), Beetroot Red, Blueberry, Cactus fruit, Cantaloupe (2 varieties), Carambula, Cauliflower, Cherry (different varieties, Rainier), Cherry Wax (Yellow, Red, Black), Chestnut, Clementine, Cocos, Corn (with husk), Cucumber (ripened), Dates, Eggplant, Fig, Ginger Root, Granadilla, Grape (Blue, Pink, White (different varieties)), Grapefruit (Pink, White), Guava, Hazelnut, Huckleberry, Kiwi, Kaki, Kohlrabi, Kumsquats, Lemon (normal, Meyer), Lime, Lychee, Mandarine, Mango (Green, Red), Mangostan, Maracuja, Melon Piel de Sapo, Mulberry, Nectarine (Regular, Flat), Nut (Forest, Pecan), Onion (Red, White), Orange, Papaya, Passion fruit, Peach (different varieties), Pepino, Pear (different varieties, Abate, Forelle, Kaiser, Monster, Red, Stone, Williams), Pepper (Red, Green, Orange, Yellow), Physalis (normal, with Husk), Pineapple (normal, Mini), Pitahaya Red, Plum (different varieties), Pomegranate, Pomelo Sweetie, Potato (Red, Sweet, White), Quince, Rambutan, Raspberry, Redcurrant, Salak, Strawberry (normal, Wedge), Tamarillo, Tangelo, Tomato (different varieties, Maroon, Cherry Red, Yellow, not ripened, Heart), Walnut, Watermelon.

**Dataset properties**

The total number of images: 90483.

Training set size: 67692 images (one fruit or vegetable per image).

Test set size: 22688 images (one fruit or vegetable per image).

The number of classes: 131 (fruits and vegetables).

Image size: 100x100 pixels.

Filename format: imageindex100.jpg (e.g. 32100.jpg) or rimageindex100.jpg (e.g. r32100.jpg) or r2imageindex100.jpg or r3imageindex100.jpg. "r" stands for rotated fruit. "r2" means that the fruit was rotated around the 3rd axis. "100" comes from image size (100x100 pixels).

# WARNING

There is a new -major version- of the dataset under release. A test archive (named fruits-360-original-size.zip) was already loaded to Kaggle. The new version contains images at their original (captured) size.
The name of the image files in the new version does not contain the "_100" suffix anymore. This will help you to make distinction between this version and the old 100x100 version.
So, if you use the 100x100 version, please make sure that the file names have the "_100" suffix. All others MUST be ignored.

# END OF WARNING

Different varieties of the same fruit (apple for instance) are stored as belonging to different classes.

How fruits were filmed
Fruits and vegetables were planted in the shaft of a low-speed motor (3 rpm) and a short movie of 20 seconds was recorded.

A Logitech C920 camera was used for filming the fruits. This is one of the best webcams available.

Behind the fruits, we placed a white sheet of paper as a background.

Here is a movie showing how the fruits and vegetables are filmed: https://youtu.be/_HFKJ144JuU

How fruits were extracted from background
However, due to the variations in the lighting conditions, the background was not uniform and we wrote a dedicated algorithm that extracts the fruit from the background. This algorithm is of flood fill type: we start from each edge of the image and we mark all pixels there, then we mark all pixels found in the neighborhood of the already marked pixels for which the distance between colors is less than a prescribed value. We repeat the previous step until no more pixels can be marked.

All marked pixels are considered as being background (which is then filled with white) and the rest of the pixels are considered as belonging to the object.

The maximum value for the distance between 2 neighbor pixels is a parameter of the algorithm and is set (by trial and error) for each movie.

Pictures from the test-multiple_fruits folder were taken with a Nexus 5X phone.

Research papers
Horea Muresan, Mihai Oltean, Fruit recognition from images using deep learning, Acta Univ. Sapientiae, Informatica Vol. 10, Issue 1, pp. 26-42, 2018.

The paper introduces the dataset and implementation of a Neural Network trained to recognize the fruits in the dataset.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# LICENSE


![This is an image](https://tse4.mm.bing.net/th/id/OIP.Eb5UsQ_5mF3xe3DEppv3cwAAAA?w=126&h=150&c=7&r=0&o=5&pid=1.7)

License
MIT License

Copyright (c) 2017-2021 Mihai Oltean

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# About this Project

**This Image Recognition project is build in Convolutional Neural Network (CNN)**

# Convolutional Neural Network(CNN) Explained:

A Convolutional Neural Network, also known as CNN or ConvNet, is a class of neural networks that specializes in processing data that has a grid-like topology, such as an image. A digital image is a binary representation of visual data. It contains a series of pixels arranged in a grid-like fashion that contains pixel values to denote how bright and what color each pixel should be.

# Convolutional Neural Network(CNN) :

- A convolutional neural network, or CNN, is a deep learning neural network sketched for processing structured arrays of data such as portrayals.
- CNN are very satisfactory at picking up on design in the input image, such as lines, gradients, circles, or even eyes and faces.
- This characteristic that makes convolutional neural network so robust for computer vision.
- CNN can run directly on a underdone image and do not need any preprocessing.
- A convolutional neural network is a feed forward neural network, seldom with up to 20.
- The strength of a convolutional neural network comes from a particular kind of layer called the convolutional layer.
- CNN contains many convolutional layers assembled on top of each other, each one competent of recognizing more sophisticated shapes.
- With three or four convolutional layers it is viable to recognize handwritten digits and with 25 layers it is possible to differentiate human faces.
- The agenda for this sphere is to activate machines to view the world as humans do, perceive it in a alike fashion and even use the knowledge for a multitude of duty such as image and video recognition, image inspection and classification, media recreation, recommendation systems, natural language processing, etc.

# Convolutional Neural Network Design :

- The construction of a convolutional neural network is a multi-layered feed-forward neural network, made by assembling many unseen layers on top of each other in a particular order.
- It is the sequential design that give permission to CNN to learn hierarchical attributes.
- In CNN, some of them followed by grouping layers and hidden layers are typically convolutional layers followed by activation layers.
- The pre-processing needed in a ConvNet is kindred to that of the related pattern of neurons in the human brain and was motivated by the organization of the Visual Cortex.

# Case Study of CNN for Diabetic retinopathy :

- Diabetic retinopathy also known as diabetic eye disease, is a medical state in which destruction occurs to the retina due to diabetes mellitus, It is a major cause of blindness in advance countries.
- Diabetic retinopathy influence up to 80 percent of those who have had diabetes for 20 years or more.
- The overlong a person has diabetes, the higher his or her chances of growing diabetic retinopathy.
- It is also the main cause of blindness in people of age group 20-64.
Diabetic retinopathy is the outcome of destruction to the small blood vessels and neurons of the retina.


![This is an image](https://th.bing.com/th/id/R.b8078035020e40fa966679ee1fe544cb?rik=3%2fCoOK1Sz%2bfJRQ&riu=http%3a%2f%2frpmarchildon.com%2fwp-content%2fuploads%2f2018%2f06%2fRM-CNN-Schematic-1.jpg&ehk=5HvEQOLFRNxWH6oVbMj9z8Zb%2fBZWK2eHigBBAbezCm8%3d&risl=&pid=ImgRaw&r=0)








![GitHub Dark](https://editor.analyticsvidhya.com/uploads/99433dnn4.gif)



![This is an image](https://editor.analyticsvidhya.com/uploads/92373dnn5.gif)



![This is an image](https://editor.analyticsvidhya.com/uploads/54575dnn6.png)































