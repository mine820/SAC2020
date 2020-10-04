from dem import DEM

filename = 'dem/FG-GML-5640-55-00-DEM5A-20161001.xml'

if __name__ == '__main__':
  d = DEM(filename)

  ulat, ulong, llat, llong = d.GetArea()
  print(ulat, ulong, llat, llong)

  x, y = d.GetSize()
  print(x, y)

  depthArray = d.GetDepth()
  for yy in range(y):
    for xx in range(x):
      print(depthArray[xx,yy])
