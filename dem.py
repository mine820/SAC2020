from bs4 import BeautifulSoup
import numpy as np

class DEM:
  def __init__(self, filename):
    # 国土地理院のDEMデータ（5mメッシュ）を読み込む
    with open(filename, encoding='UTF-8') as f:
      self.soup = BeautifulSoup(f, 'xml')

    # 緯度経度の最小値／最大値の取得
    for e in self.soup.find_all('gml:lowerCorner'):
      self.low_latitude = float(e.contents[0].split()[0])
      self.low_longitude = float(e.contents[0].split()[1])
    for e in self.soup.find_all('gml:upperCorner'):
      self.upper_latitude = float(e.contents[0].split()[0])
      self.upper_longitude = float(e.contents[0].split()[1])

    # データ数（横、縦）の取得
    for e in self.soup.find_all('gml:low'):
       low_x = int(e.contents[0].split()[0])
       low_y = int(e.contents[0].split()[1])
    for e in self.soup.find_all('gml:high'):
       high_x = int(e.contents[0].split()[0])
       high_y = int(e.contents[0].split()[1])
    self.x = high_x - low_x + 1
    self.y = high_y - low_y + 1

    # 標高データの取得
    elevation = []
    for e in self.soup.find_all('gml:tupleList'):
      for d in e.contents[0].split('\n'):
        if (len(d.split(',')) < 2):
          continue
        elevation.append(float(d.split(',')[1]))
    if (len(elevation) < (self.x * self.y)):
        for i in range(self.x*self.y-len(elevation)):
	        elevation.append(-9999.0)
    self.elevationArray = np.array(elevation)
    self.elevationArray = np.reshape(self.elevationArray, (self.x, self.y))

  # 緯度経度の最小値／最大値の取得
  def GetArea(self):
    return self.upper_latitude, self.upper_longitude, self.low_latitude, self.low_longitude

  # データ数（横、縦）の取得
  def GetSize(self):
    return self.x, self.y

  # 標高データの取得
  def GetElevation(self):
    return self.elevationArray
