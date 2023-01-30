#!/usr/bin/env python
import sys

def triange (base, hight):
  return base*hight/2
def rectange (name, hello):
  return name+hello
for i in range (1, 5):
  try:
    sys.argv[i]
  except:
    print ("You must input Argv {}".format(i))
    if i == 4:
      sys.exit()
print(triange(int(sys.argv[1]), int(sys.argv[2])))
print(rectange(str(sys.argv[3]), str(sys.argv[4])))

