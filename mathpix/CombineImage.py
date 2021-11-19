import os
from PIL import Image
import numpy as np


def readImageFromDir(path: str) -> list:
    return [np.asarray(Image.open(path+filename).convert('I'))
            for filename in os.listdir(path) if filename.endswith(".png")]


def readImageFromFiles(files: list) -> list:
    return [np.asarray(Image.open(file).convert('I'))
            for file in files]


def expend(data, w, h=0, value=255):
    dataH, dataW = data.shape
    h = dataH if h == 0 else h
    l = (w-dataW)//2
    r = w-dataW-l
    u = (h-dataH)//2
    d = h-dataH-u
    #print(u, d, l, r)
    return np.pad(data, ((u, d), (l, r)), 'constant', constant_values=(value))


def concatenate(images: list):
    w = max([img.shape[1] for img in images])
    h = sum([img.shape[0] for img in images])
    result = Image.new("RGBA", (w, h))
    pasteHigh = 0
    for img in images:
        result.paste(Image.fromarray(expend(img, w)), (0, pasteHigh))
        pasteHigh += img.shape[0]
    # result.show()
    return result


def combineImage(path):
    if isinstance(path, str) and os.path.isdir(path):
        return concatenate(readImageFromDir(path))
    elif isinstance(path, list) and os.path.isfile(path[0]):
        return concatenate(readImageFromFiles(path))
    else:
        print("combineImage:", path)
        return


if __name__ == "__main__":
    combineImage("./test/").show()
    # combineImage("./test/image/").show()
    '''
    images = []
    for i in range(1, 5):
        img = Image.open(rf"test\image\{i}.png").convert('I')
        images.append(np.asarray(img))
    concatenate(images)

    '''
