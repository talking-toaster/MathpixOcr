from PIL import Image
import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([[2, 3, 6, 2], [4, 2, 7, 8]])

c = 4
c = 5 if c == 3 else c
# print(a.shape)
#c = np.pad(b, ((0, 0), (2, 3)), 'constant', constant_values=(255))
#print(a.append([4, 5, 6, 7]))


def expend(data, w, h=0, value=255):
    dataH, dataW = data.shape
    h = dataH if h == 0 else h
    l = (w-dataW)//2
    r = w-dataW-l
    u = (h-dataH)//2
    d = h-dataH-u
    print(u, d, l, r)
    return np.pad(data, ((u, d), (l, r)), 'constant', constant_values=(value))


def concatenate(images):
    w = max([img.shape[1] for img in images])
    h = sum([img.shape[0] for img in images])
    result = Image.new("RGBA", (w, h))
    pasteHigh = 0
    for img in images:
        result.paste(Image.fromarray(expend(img, w)), (0, pasteHigh))
        pasteHigh += img.shape[0]
    result.show()


if __name__ == "__main__":
    images = []
    for i in range(1, 5):
        img = Image.open(rf"test\image\{i}.png").convert('I')
        images.append(np.asarray(img))
    concatenate(images)
#concatenate(img1, img2)
