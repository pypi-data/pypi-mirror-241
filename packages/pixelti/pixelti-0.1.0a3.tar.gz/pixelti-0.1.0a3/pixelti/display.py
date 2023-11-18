from colr import Colr as C


class ShellPixel:
  pixel = "\u2588\u2588"

  def put(self, color=(255,255,255)):
    print(C().rgb(color[0],color[1],color[2], self.pixel), end="")

  def endLine(self):
    print()