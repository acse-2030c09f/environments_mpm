from envtest import rand_array
from scipy import misc
import matplotlib.pyplot as plt

image = misc.ascent()
sigma = 5

smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1,2,1)
plt.imshow(image)
f.add_subplot(1,2,2)
plt.imshow(smoothed_image)
plt.show(blocked=True)

shape = (3, 3)

print(rand_array(shape))
