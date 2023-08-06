import os
import sys
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
from functools import reduce
import operator
from . import tinyCrypt
import tempfile
import requests
import random
from zlib import crc32

DEBUG = False

__all__ = ["imageTool"]

class imageTool():
    shape = []
    transp = []
    flat = []

    def imageTool(self):
        self.datas = []

    def reloadAsPng(self, datas):
        """image datas as converted to RBGA (png) format

        Args:
            datas (ndarray): image datas from Pillow.image.Open

        Returns:
            ndarray: image datas (png format. i.e. RGBA)
        """
        temp = tempfile.NamedTemporaryFile(prefix="Stegy_",
                                           suffix=".png")

        mpimg.imsave(temp, datas)
        temp.seek(0)
        # read datas as png
        datas = mpimg.imread(temp)
        temp.close()

        return datas

    def randomImageAsPng(self, topics = None):
        """get a random image from flikr using topic to filter search

        Args:
            topics (str, optional): comma-separated list of topics for image search. Defaults to None.
        """
        if topics is None:
            topics = ('cat', 'dog', 'mountain', 'forest', 'beach')

        # get image data from url and save it as a temp png file
        url = 'https://loremflickr.com/320/240/' + random.choice(topics)
        response = requests.get(url, stream=True)
        # use a temp jpeg file support
        jpg = tempfile.NamedTemporaryFile(prefix="flk_", suffix=".jpg")
        for chunk in response.iter_content(chunk_size=1024):
            jpg.write(chunk)
        jpg.seek(0)
        # read datas as ndarray
        datas = mpimg.imread(jpg, "jpeg")
        jpg.close()  # temp file is deleted

        datas = self.reloadAsPng(datas)
        # return flatten datas whitout transparency
        self.transp = datas[:, :, 3]
        self.shape = datas.shape
        self.flat = datas[:, :, 0:3].flatten()

    def fileReadAsPNG(self, fname, downscale=False):
        """open image file and convert it to png format

        Args:
            fname (str): path to image file
            downscale (bool, optional): if True, downscale image below 1000px on its larger dimension. Defaults to False.
        """

        if downscale is True:
            img = Image.open(fname)    # Open image as PIL image object

            siz = np.array(img.size)
            m = siz.max()
            while m > 1000:
                siz = siz / 2
                m = siz.max()

            rsize = img.resize(siz.astype(int))  # Use PIL to resize
            datas = np.asarray(rsize)  # Get array back

            datas = self.reloadAsPng(datas)
        else:
            datas = mpimg.imread(fname)

        # return flatten datas whitout transparency
        self.transp = datas[:, :, 3]
        self.shape = datas.shape
        self.flat = datas[:, :, 0:3].flatten()

    def fileWritePNG(self, rac,  filepath):
        """save image datas to PNG file

        Args:
            rac (str): filename prefix
            filepath (str): filepath

        Returns:
            str: path of created file
        """
        fp = list(os.path.split(filepath))
        fp[-1] = rac + fp[-1]

        ffolder = fp[:-1]
        foldname = os.path.join(*ffolder)
        if not(os.path.exists(foldname)):
            os.mkdir(foldname)
        fname = os.path.join(*fp)

        ts = list(self.shape)
        ts[2] = 3
        tmp = self.flat.reshape(ts)
        dataLoc = np.zeros(self.shape, dtype=np.float32)
        dataLoc[:, :, 0:3] = tmp[:, :, 0:3]
        dataLoc[:, :, 3] = self.transp

        mpimg.imsave(fname, dataLoc)

        return fname

    def getIdxsLength(self, siz, key : str):
        if DEBUG == True:
            return [x for x in range(12)]
        
        offset = 0
        if not(key is None):
            offset = (crc32(bytes(key, 'utf-8')) % 16) - 8

        step = int(siz / 24)
        return [(i*2*step) + step + offset for i in range(12)]

    def getIdxsMessage(self, tab, lenM, posL):
        # if DEBUG == True:
        #     return [x+12 for x in range(lenM)]
        lenD = len(tab)

        # second code message itself
        step = (int)(lenD/(2*lenM))
        posM = [(i*2*step) + step for i in range(lenM)]
        # avoid idx collision between size and msg
        for i in range(len(posM)):
            while posM[i] in posL:
                posM[i] = posM[i] + 1

        return posM

    def fuzz(self, tab):
        # add background noise to avoid analysis
        fuzz = np.random.randint(-3, 4, size=tab.shape) / 255
        temp = tab + fuzz
        temp = np.where(temp > 1, 1, temp)
        temp = np.where(temp < 0, 0, temp)

        return np.array(temp, dtype=np.float32)

    def mark(self, mess, key=None):
        """encode message into image datas ( previously loaded with fileReadAsPNG()

        Args:
            mess (str): message to encode
            key (str, optional): message encryption key. Defaults to None.
        """ 
        coder = tinyCrypt(key)

        tab = self.fuzz(self.flat)
        lenD = len(tab)

        bmess, lon = coder.crypt(mess)
        lenB = len(bmess)

        # first code length
        posL = self.getIdxsLength(lenD, key)
        for i in range(len(posL)):
            self.pxSet(tab, posL[i], lon[i])

        # second code message itself
        posM = self.getIdxsMessage(tab, lenB, posL)

        for i in range(len(bmess)):
            self.pxSet(tab, posM[i], bmess[i])

        self.flat = tab

    def read(self, key=None):
        """decode message from image datas ( previously loaded with fileReadAsPNG()


        Args:
            key (str, optional): message encryption key. Defaults to None.

        Returns:
            str: message
        """
        coder = tinyCrypt(key)
        tab = self.flat

        # first decode length
        posL = self.getIdxsLength(len(tab), key)
        tabL = []
        for i in range(len(posL)):
            tabL.append(self.pxGet(tab, posL[i]))

        lenB = coder.decryptLength(tabL)

        # second decode message itself
        posM = self.getIdxsMessage(tab, lenB, posL)
        tabM = []
        for i in range(len(posM)):
            tabM.append(self.pxGet(tab, posM[i]))

        return coder.decrypt(tabM)

    def pxSet(self, tab, idx, val):
        ov = int(tab[idx] * 255)
        nv = ov - (ov % 5) + val
        while (nv >= 255):
            nv = nv - 5
            # print("[", idx, "] ", ov, " -> ", nv)
        tab[idx] = nv / 255

    def pxGet(self, tab, idx):
        ov = int(tab[idx] * 255)
        val = ov % 5

        return val

    def len(self):
        return len(self.flat)


def main():

    tool = imageTool()
    datas = tool.randomImageAsPng()


    img = Image.open('./data/papillon.jpg')    # Open image as PIL image object

    siz = np.array(img.size)
    m = siz.max()
    while m > 1000:
        siz = siz / 2
        m = siz.max()

    rsize = img.resize(siz.astype(int))  # Use PIL to resize
    rsizeArr = np.asarray(rsize)  # Get array back

    print(rsizeArr.shape)

    # im = imageTool()

    # im.fileReadAsPNG('.','data','papillon.jpg')

    # im.fileWritePNG(''""'', '.','data','papillon.png')

    # l = im.len()


if __name__ == "__main__":
    # execute only if run as a script
    main()
