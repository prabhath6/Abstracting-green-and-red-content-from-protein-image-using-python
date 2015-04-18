""" Extrating data from images. """
import numpy as np

# Load all the .jpg files as a list
import os
# Path where the images are located
path = 'filePath'
files = []
for image in os.listdir(path):
    if image.endswith('.jpg'):
        files.append(image)

reder_image = []
grener_image = []

# Reading images
import pylab
for image in files:
    img = pylab.imread(image)
    reds = img[:,:,0]
    reder_image.append(np.sum(reds))
    green = img[:,:,1]
    grener_image.append(np.sum(green))

#converting into numpy array
reder_image = np.array(reder_image, dtype=float)
grener_image = np.array(grener_image, dtype=float)
ratio = reder_image / grener_image

pylab.figure(1)
pylab.plot(111)
pylab.plot(range(0, len(reder_image)), reder_image, 'ro')
pylab.plot(range(0, len(grener_image)), grener_image, 'go')
pylab.xlabel("images")
pylab.ylabel("Range of values")
pylab.title("Green vs Red Protien")

# Ratio of both the read and green protiens


pylab.figure(2)
pylab.subplot(111)
pylab.xlabel("images")
pylab.ylabel("Range of values")
pylab.title("Ratio of red to green")
pylab.plot(range(0, len(ratio)), ratio, 'b*')
pylab.show()
