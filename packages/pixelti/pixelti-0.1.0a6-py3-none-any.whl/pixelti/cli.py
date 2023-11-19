import time

import typer
from typing_extensions import Annotated

from pixelti import PalletteManager
from pixelti.app.cli.generate_pixelti import handleGeneratePixelti

app = typer.Typer()
@app.command()
def pallette():
  manager = PalletteManager()
  manager.printToConsole()

@app.command()
def generate(
  image: Annotated[str, typer.Argument()],
  pixelSize:Annotated[int, typer.Option()] = 7,
  save: Annotated[bool, typer.Option()] = False,
  fileName: Annotated[str, typer.Option()] = None,
  pallette: Annotated[str, typer.Option()] = None,
  samplingMethod: Annotated[str, typer.Option()] = 'median'):
  startTime = time.time()
  handleGeneratePixelti(image, pixelSize, save, fileName, pallette, samplingMethod)
  print("\n")
  print("Execution Time: %0.3f seconds"%(time.time() - startTime))

if __name__ == "__main__":
  app()
