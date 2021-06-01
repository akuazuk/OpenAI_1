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
    print ("Input Argv {}".format(i))
    sys.exit()
print(triange(int(sys.argv[1]), int(sys.argv[2])))
print(rectange(str(sys.argv[3]), str(sys.argv[4])))

