import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('files/opencv/cocacola.png')
print(img)

imgarray = np.asarray(img)

# shape of image array
print(np.shape(img))
# or both syntax are true.
print(imgarray.shape)

#plt.imshow(imgarray)

img_coca = imgarray[:,:,0]
#plt.imshow(img_coca,cmap="hot")
plt.imshow(img_coca,cmap ='nipy_spectral')

plt.colorbar()



# Show the plot
plt.show()
# Wait until a key is pressed
plt.waitforbuttonpress()

# Close the plot window
plt.close()

