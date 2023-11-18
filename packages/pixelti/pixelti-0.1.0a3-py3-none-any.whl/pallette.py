import os

from pixelti.display import ShellPixel
from pixelti.lib import hexToRGB

WARM_RAIN =[(102, 67, 58), (142, 92, 76), (168, 116, 82), (197, 134, 88), (212, 140, 88), (222, 165, 91), (251, 182, 81), (251, 200, 81), (222, 183, 75), (210, 172, 82), (191, 169, 80), (168, 157, 75), (148, 150, 71), (110, 135, 67), (86, 121, 65), (63, 96, 55), (41, 67, 41), (49, 80, 62), (60, 98, 81), (79, 135, 127), (92, 161, 162), (100, 162, 177), (106, 156, 208), (111, 162, 245), (106, 134, 222), (87, 108, 173), (82, 94, 152), (66, 75, 119), (48, 54, 82), (35, 39, 55), (17, 18, 24)]
BOF = [(58, 34, 79), (78, 37, 87), (115, 50, 106), (163, 68, 116), (199, 80, 107), (227, 117, 95), (237, 158, 112), (252, 200, 141), (255, 215, 163), (255, 239, 201), (240, 235, 168), (207, 242, 145), (160, 222, 133), (105, 201, 118), (80, 171, 118), (54, 119, 122), (46, 92, 107), (34, 61, 84), (31, 46, 82)]

class Pallette:
  colors: list

  def __init__(self, colors: list):
    if len(colors) == 0:
      raise Exception('Pallette must not be empty')
    self.colors = colors

  def translateColor(self, color: list) -> list:
    minDistance = 10000000000000000000 # a very large number
    selectedColor = color
    for colorItem in self.colors:
      distance = self.__calculateEuclidean(color, colorItem)
      if minDistance > distance:
        minDistance = distance
        selectedColor = colorItem

    return selectedColor

  def __calculateEuclidean(self, vector1: tuple, vector2: tuple):
    if len(vector1) != len(vector2):
      raise Exception('Vectors must have the same length')
    sumResult = 0
    for i in range(len(vector1)):
      sumResult += (vector1[i] - vector2[i])**2
    return sumResult**(1/2)

  def getColors(self):
    return self.colors

class PalletteManager:
  pallettes: dict

  def __init__(self):
    self.pallettes = {
      'warm_rain': Pallette(WARM_RAIN),
      'bof': Pallette(BOF)
    }

    palletteDir = 'pixelti/assets/pallettes'
    fileName = os.listdir(palletteDir)
    for name in fileName:
      if name.split('.')[1] != 'hex':
        continue
      file = open(palletteDir+'/'+name)
      hexValue = file.read().strip().split('\n')
      self.pallettes[name.split('.')[0]] = Pallette([hexToRGB(hex) for hex in hexValue])

  def printToConsole(self):
    pix = ShellPixel()
    print("\nAvailable Palletes:\n")
    for key, item in self.pallettes.items():
      print(key, end=": ")
      for color in item.getColors():
        pix.put(color)
        print(" ", end="")
      print("\n ")

  def getPallette(self, name: str) -> Pallette:
    if name not in self.pallettes:
      raise Exception('Pallette not found')
    return self.pallettes[name]