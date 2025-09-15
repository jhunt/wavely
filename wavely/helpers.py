from .base import Path
from .paths import Sigmoid

import math

def combine(*paths):
  p = paths[0]
  for x in paths[1:]:
    p.append(x)
  return p

def seasonal(a, b, c, t):
  (ax, ay) = a
  (bx, by) = b
  (cx, cy) = c
  s = lambda x, y: 10.0 * (y/math.fabs(y)) / x
  return combine(
    Sigmoid((0,  ax), steepness=s(ax-0,  ay-0 )).scale(math.fabs(ay-0 )),
    Sigmoid((ax, bx), steepness=s(bx-ax, by-ay)).scale(math.fabs(by-ay)),
    Sigmoid((bx, cx), steepness=s(cx-bx, cy-by)).scale(math.fabs(cy-by)),
    Sigmoid((cx,  t), steepness=s(t-cx,  0-cy )).scale(math.fabs(0-cy )),
  )
