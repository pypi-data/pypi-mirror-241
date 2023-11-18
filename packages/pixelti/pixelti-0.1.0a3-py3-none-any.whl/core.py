import asyncio
from statistics import mean, median, mode

import numpy as np
from PIL import Image

from pixelti.lib.utils import createChunks
from pixelti.pallette import Pallette


class Pixelti:
  colorPallette: Pallette = None
  img: np.ndarray
  imgW: int
  imgH: int
  # compressed dimention is the dimention of the copressed image
  # after we combained pixelSize x pixelSize of the original image into one pixel in the new image
  compressedW: int
  compressedH: int
  pixelSize: int = 7

  __samplingMethod = 'median'

  __outputArray: any

  def __init__(self, colorPallette: Pallette = None):
    self.colorPallette = colorPallette

  def setImage(self, img: Image.Image):
    self.img = np.array(img)
    (self.imgH, self.imgW, _) = self.img.shape
    self.__outputArray  = np.zeros(shape=(self.imgH, self.imgW, 3), dtype=np.uint8)
    self.compressedH = self.imgH // self.pixelSize
    self.compressedW = self.imgW // self.pixelSize

  def setPixelSize(self, pixelSize: int):
    self.pixelSize = pixelSize

  def setColorPallette(self, colorPallette: Pallette):
    self.colorPallette = colorPallette

  def getSample(self, v: list):
    if(self.__samplingMethod == 'mean'):
      return mean(v)

    if(self.__samplingMethod == 'median'):
      return median(v)

    if(self.__samplingMethod == 'mode'):
      return mode(v)

  def setSamplingMethod(self, method: str):
    if method not in ['mean', 'median', 'mode']:
      raise Exception('Sampling method not found, vailable methods: %s' % ['mean', 'median', 'mode'])

  def __compressPixel(self, i: int, j: int) -> list:
    offset1 = i * self.pixelSize
    offset2 = j * self.pixelSize
    r = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,0]
    g = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,1]
    b = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,2]
    return [self.getSample(r.flatten()), self.getSample(g.flatten()), self.getSample(b.flatten())]

  def __fillOriginalPixel(self, i: int, j: int, color: list) -> np.ndarray:
    offset1 = i * self.pixelSize
    offset2 = j * self.pixelSize
    for m in range(offset1, offset1 + self.pixelSize):
      for n in range(offset2, offset2 + self.pixelSize):
        self.__outputArray[m][n] = color

  async def __generatePerChunk(self, index:list):
    for i in index:
      for j in range(self.compressedW):
        newColor = self.__compressPixel(i, j)
        if self.colorPallette is not None:
          newColor = self.colorPallette.translateColor(newColor)
        self.__fillOriginalPixel(i, j, newColor)

  async def __asyncTask(self) -> None:
    chunk = createChunks([x for x in range(self.compressedH)], 3)
    self.__outputArray = np.zeros(shape=(self.imgH, self.imgW, 3), dtype=np.uint8)
    asyncio.gather(*[self.__generatePerChunk(task) for task in chunk])

  def generate(self) -> Image.Image:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(self.__asyncTask())
    loop.close()
    return Image.fromarray(self.__outputArray)
