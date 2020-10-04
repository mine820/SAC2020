from depth import DepthImage

# 画像ファイル名
#   0x000000 浸水地域外
#   0xFFFFFF 0.3m未満
#   0x0000FF 0.3m～3.0m未満
#   0x00FF00 3.0m～5.0m未満
#   0xFF0000 5.0m～10.0m未満
filename = 'image/image_final.png'

# 宮城県伊具郡丸森町役場
x = 140.7654307
y = 37.9114559

if __name__ == '__main__':
  di = DepthImage(filename)
  d = di.GetDepth(y, x)
  print(d)
