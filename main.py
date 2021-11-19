import time
import os
import threading
import latex2mathml.converter as converter
from mathpix.MathpixOcr import MathpixOcr
from mathpix.CombineImage import combineImage
from mathpix import PaperClip


def startOcr(imagePath):
    ocr = MathpixOcr("", "")
    # ocr.login()
    ocr.login()
    return ocr.ocr(imagePath).json()


def run():
    dataPath = f"./data/{int(time.time())}/"
    snipPath = dataPath+"snip/"
    os.mkdir(dataPath)
    os.mkdir(snipPath)
    paperClipThread = threading.Thread(
        target=PaperClip.listen, args=(snipPath,))
    paperClipThread.daemon = True
    paperClipThread.start()
    try:
        while True:
            i = input("正在监听剪贴板中(输入y识别，q退出):")
            if i == 'y' or i == 'Y':
                letex = startOcr(snipPath+"combine.png")["latex"]
                print(converter.convert(letex))
            if i == 'q' or i == 'Q':
                exit(0)
    except KeyboardInterrupt as e:
        exit(0)


if __name__ == "__main__":
    run()
