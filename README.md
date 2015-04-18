# Abstracting-green-and-red-content-from-protein-image-using-python
This project mainly extracts the red and green content from protein images. Then plots the graph using the data obtained from the images. The other image plot the ratio between the red to green image. All this done using python.

Modules used

1. Numpy

2. Os

3. Pylab


First you need to load all the '.jpg' files into list for manipulation. This is done by looping through the image directory and checking if the file is '.jpg' or not. This verification can be done using ```image.endswith('.jpg')```. If this returns true then the image is appended into files ```files.append(image)```.

Once we are done with loading images in to files. Then read the images using ```img = pylab.imread(image)```. This will read the image, the image has three components RGB each can be accessed using indexing the img ```red = img[:,:,0]``` since red is the first one it is accessed using 0 as index. This returns the values in the image, the mean of the values is calculated using numpy ```np.mean(red)```. In the similar way green content from the image is abstracted.

Now convert the normal arrays into numpy arrays for beter manipulation. ```np.array(reder_image)```

Plot the values in the numpy arrays corresponding to the images using the pylab module.


