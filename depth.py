from PIL import Image
import numpy as np

# 浸水深クラス
class DepthImage:
  # 世界測地系（Degree形式）
  org_x = 140.59050113407473309608540925267
  org_y = 37.982445567039106145251396648045
  delta_w = 1.0672944839857651245551601423488e-4
  delta_h = 8.4511508379888268156424581005587e-5

  # 浸水深
  depth_list = [0.0, 10.0, 5.0, -1.0, 3.0, -1.0, -1.0, 0.3]

  def __init__(self, filename):
    # 事前に画像ファイルを読み込み
    im = Image.open(filename)
    im = im.convert('RGB')
    self.img_w = im.size[0]
    self.img_h = im.size[1]
    self.imArray = np.array(im)

  def GetDepth(self, y, x):
    # 座標をピクセル値に変換
    px = round((x - self.org_x) / self.delta_w)
    py = round((self.org_y - y) / self.delta_h)

    # 画像外なら-1を返す
    if ((px < 0 or px >= self.img_w) or (py < 0 or py >= self.img_h)):
      return -1.0

    # 画素値を取得する
    pixel = self.imArray[py, px]

    # 画素値をインデックス値に変換
    index = 0
    index += 1 if (pixel[0] & 0xFF > 0) else 0
    index += 2 if (pixel[1] & 0xFF > 0) else 0
    index += 4 if (pixel[2] & 0xFF > 0) else 0

    # 浸水深を返す
    return self.depth_list[index]
