import time
import threading
from PIL import Image, ImageGrab
import numpy as np
from mathpix.CombineImage import combineImage


cacheImgList = []
cacheImgLock = threading.Lock()
combinedImagePath = ""


def _binary_array_to_hex(arr):
    """
    internal function to make a hex string out of a binary array.
    """
    bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    width = int(np.ceil(len(bit_string)/4))
    return '{:0>{width}x}'.format(int(bit_string, 2), width=width)


def ahash(image, hash_size=8, mean=np.mean):
    if hash_size < 2:
        raise ValueError("Hash size must be greater than or equal to 2")
    image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)

    # find average pixel value; 'pixels' is an array of the pixel values, ranging from 0 (black) to 255 (white)
    pixels = np.asarray(image)
    avg = mean(pixels)

    # create string of bits
    diff = pixels > avg
    # make a hash
    return _binary_array_to_hex(diff)


def saveImage(path):
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        imghash = hash(ahash(img, 16))
        with cacheImgLock:
            if imghash not in cacheImgList:
                cacheImgList.append(imghash)
                img.save(path+f"{imghash}.png")
                if len(cacheImgList) == 1:
                    Image.open(path + f"{imghash}.png").save(combinedImagePath)
                elif len(cacheImgList) == 2:
                    combineImage(
                        [path+f"{imgName}.png" for imgName in cacheImgList]).save(combinedImagePath)
                else:
                    combineImage([combinedImagePath, path +
                                  f"{imghash}.png"]).save(combinedImagePath)


def listen(path, interval=1):
    global combinedImagePath
    combinedImagePath = path+"combine.png"
    while True:
        saveImage(path)
        time.sleep(interval)


if __name__ == "__main__":
    listen("./test/temp/")
