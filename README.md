# Fruits_-_Vegetable_Recognition

## Data Info

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

## WARNING

There is a new -major version- of the dataset under release. A test archive (named fruits-360-original-size.zip) was already loaded to Kaggle. The new version contains images at their original (captured) size.
The name of the image files in the new version does not contain the "_100" suffix anymore. This will help you to make distinction between this version and the old 100x100 version.
So, if you use the 100x100 version, please make sure that the file names have the "_100" suffix. All others MUST be ignored.

## END OF WARNING

Different varieties of the same fruit (apple for instance) are stored as belonging to different classes.

How fruits were filmed
Fruits and vegetables were planted in the shaft of a low-speed motor (3 rpm) and a short movie of 20 seconds was recorded.

A Logitech C920 camera was used for filming the fruits. This is one of the best webcams available.

Behind the fruits, we placed a white sheet of paper as a background.

Here is a movie showing how the fruits and vegetables are filmed: https:/

https://user-images.githubusercontent.com/74713336/150738182-d9d4c66f-0e73-4a20-87dc-bc6435ba2e1c.mp4

/youtu.be/_HFKJ144JuU

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

Copyright (c) 2021-2022 Ashok_kumar

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

# Convolutional Neural Network Architectures :

we will see what are convolutional neural network architectures right from basic and we will take a basic architecture as a case study to apply our learnings, The only pre-requisite is you just need to know how convolution works But don’t worry it is very simple !!

Let us take a simple Convolutional neural network,

![This is an image](https://th.bing.com/th/id/R.b8078035020e40fa966679ee1fe544cb?rik=3%2fCoOK1Sz%2bfJRQ&riu=http%3a%2f%2frpmarchildon.com%2fwp-content%2fuploads%2f2018%2f06%2fRM-CNN-Schematic-1.jpg&ehk=5HvEQOLFRNxWH6oVbMj9z8Zb%2fBZWK2eHigBBAbezCm8%3d&risl=&pid=ImgRaw&r=0)

# Padding

While applying convolutions we will not obtain the output dimensions the same as input we will lose data over borders so we append a border of zeros and recalculate the convolution covering all the input values.

![This is an image](https://editor.analyticsvidhya.com/uploads/99433dnn4.gif)

# Striding
Some times we do not want to capture all the data or information available so we skip some neighboring cells let us visualize it,

![This is an image](https://editor.analyticsvidhya.com/uploads/92373dnn5.gif)
The stride is the number of pixels that the analysis window moves on each iteration. A stride of 2 means that each kernel is offset by 2 pixels from its predecessor.

# Pooling
In general terms pooling refers to a small portion, so here we take a small portion of the input and try to take the average value referred to as average pooling or take a maximum value termed as max pooling, so by doing pooling on an image we are not taking out all the values we are taking a summarized value over all the values present !!!

![This is an image](https://editor.analyticsvidhya.com/uploads/54575dnn6.png)

here this is an example of max pooling so here taking a stride of two we are taking the maximum value present in the matrix

# Caution
![This is an image](https://tse2.mm.bing.net/th/id/OIP.NBRhdDu3xPQP6dqq0kauPgHaHa?w=186&h=186&c=7&r=0&o=5&pid=1.7)

## **Don't Run Without Graphics card**

## If you don’t have a graphic card, then all the programs you run will cause your processor to overheat, potentially damaging it. Moreover, you can’t expect to run multiple tasks without a graphics card. Not, having a graphics card can also cause adverse effects on other hardware components like motherboard etc.

## Causes

## 1. Stuttering

Usually, a graphics card on the path of failure will stutter or lag to fulfill your requirements. There are also other reasons that the computer is behaving in a similar way.

Malware can cause a similar effect.
The game was not optimized.
Your graphics card is of low quality. In other words, the Game needs a recent version.
You need to update the drivers on the computer.
These are some signs of graphics card failure in your computer/laptop.

## 2. Glitches in Screen
Let us assume, you are playing games or watching a movie. All of a sudden, you see weird colors appearing on the screen. Then the graphics card is on the path of failure. For a temporary solution, you can restart the computer. But note, the problem will recur. It is the time to seek a computer repair expert, and fix the problem. He can give the best suggestion on replacement or updating the graphics card. Plus, you will also get the complete maintenance of the computer.

To check if the graphics card has entirely gone wrong, check it with other images or games. If the same problem happens, then you can know it is sure signs of graphics card failure.

 
## 3. Blue Screens
Yes, we have dealt with the Blue screen on previous articles. There are many reasons, you may get this problem such as hard drives, RAM, graphics card and even other components. But if you notice frequent crashes during image or video viewing or working on graphic images, then it is one of the signs of graphics card failure.

# Minimum to Average GPU Specs

![This is an image](https://tse2.mm.bing.net/th/id/OIP.qh322Yoh8F1cbYT92n0_2QHaDt?w=326&h=175&c=7&r=0&o=5&pid=1.7)

- Graphics card --		Nvidia Tesla T4		
- Market (main)	--	Desktop		
- Architecture	--	Turing		
- GPU base clock		585 MHz		
- GPU boost clock		1.59 GHz		
- Memory frequency		1,250 MHz		
- Effective memory speed		10 GB/s		
- Memory size		16 GB		
- Memory type		GDDR6		
- Memory bus		256 bit		
- Performance FP16 (half)		65.1 TFLOPS		
- Performance FP32 (float)		8.1 TFLOPS		
- Performance FP64 (double)		254.4 GFLOPS

Finaly Model Deployment :

your saved model have been deploy into cloud or edge devices

Suggested Products : 

# OpenCV AI Kit

![This is an image](https://blog.roboflow.com/content/images/2021/05/image-10.png)

- Open CV AI Kit comes with two variations of spatial AI cameras OAK-1 and OAK-D.
- Both OAK-1 and OAK-D supports Windows, Linux, and Mac-OS platform.
- OAK-1 has a single-camera 4k @ 60fps hardware module which includes a Myriad X and is a tiny 45 mm x 30 mm.
- OAK-D has a 4k @ 60fps camera and stereo depth cameras that provide spatial 3D tracking capability. It is about the size of a Raspberry Pi.
- The hardware includes a 12-megapixel auto-focus camera with a wide horizontal field of view and 4056 x 3040 resolutions. 
- The raw video output is at up to 4K/60fps with hardware 4K H.265 video encoding. 
- OAK-1 is a single camera solution that can do neural inference like image classification, object detection, segmentation and much more on the device.
- OAK-D is a Spatial AI solution that comes with a stereo camera in addition to the standard RGB camera. This can be considered as a higher version of OAK-1.
- They have a software library for advanced on-device real-time neural network processing for the OAK boards.

# Nvidia Jetson Toolkits

![This is an image](https://hackster.imgix.net/uploads/attachments/1134547/jetson_nx_briefing_16_vmxipsyqVB.png?auto=compress%2Cformat&w=740&h=555&fit=max)

## Nvidia jetson better for CNN models :

![image](https://user-images.githubusercontent.com/74713336/150744245-9d880610-4292-4cee-bf73-0f991c8c303b.png)

They excel at running CNN inference in INT8 precision, doing that task faster and more energy efficient than GPUs – the downside being that they are not as the general purpose when it comes to different network architecture support. NVIDIA realized that GPUs alone cannot beat highly specialized hardware and decided to take the best of both worlds by having both advanced 384-core NVIDIA Volta™ GPU with 48 Tensor Cores and dedicated CNN accelerators in the new module.

![image](https://tse4.mm.bing.net/th/id/OIP.2fNVbXa9QiLzVBW3RQHyaAHaEK?w=292&h=180&c=7&r=0&o=5&pid=1.7)

# **Thank you!**



