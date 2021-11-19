from PIL import Image
import numpy as np

img1 = Image.open(r"test\image\1.png")
img2 = Image.open(r"test\image\2.png")

img11 = img1.convert('I')
# img11.show()

print(img11.getbands())
data = np.asarray(img11)
print(data[0][0], data.shape)
