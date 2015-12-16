import matplotlib.pyplot as plt
import os.path
import numpy

directory = os.path.dirname(os.path.abspath(__file__));
filename = os.path.join(directory, 'Screenshot_2015-11-12-17-51-54.png')
img = plt.imread(filename)
img2 = plt.imread(filename)

img_height = len(img)
img_width = len(img[0])

print(img_height, img_width)

for x in range(0, img_height):
	for y in range(0, img_width):
		luminence = img[x][y][0] * .2126 + img[x][y][1] * .7152 + img[x][y][2] * .0722
		img[x][y][0] = luminence
		img[x][y][1] = 0
		img[x][y][2] = 0

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img)
ax[1].imshow(img2)
#Pltw had 'fig.show()' but the window disapeared right away. S.O. said to change it to 'plt.show()'
plt.show()
plt.imsave(os.path.join(directory, 'redshift.png'), img)
