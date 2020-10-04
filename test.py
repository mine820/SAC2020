from depth import DepthImage

# 宮城県伊具郡丸森町役場
x = 140.7654307
y = 37.9114559

if __name__ == '__main__':
  di = DepthImage()
  d = di.GetDepth(y, x)
  print(d)
