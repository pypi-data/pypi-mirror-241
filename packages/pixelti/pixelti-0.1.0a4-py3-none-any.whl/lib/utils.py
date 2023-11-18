import math


def createChunks(iterable, n=3):
  chunkSize = math.ceil(len(iterable) / n)
  return [iterable[i:i+chunkSize] for i in range(0, len(iterable), chunkSize)]

def hexToRGB(hexA: str) -> tuple:
  if len(hexA) != 6:
    raise Exception('Hex must have 6 characters')
  return (int(hexA[0:2], 16), int(hexA[2:4], 16), int(hexA[4:6], 16))