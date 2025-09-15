from . import Path

import math
import random

class Sigmoid(Path):
  def __init__(self, x, density = 1.0, steepness = 1.0, midpoint = 0.5):
    if midpoint <= 0.0 or midpoint >= 1.0:
      raise ValueRangeException(f'sigmoid midpoint must range from [0,1]; given value {midpoint} is out of range.')
    midpoint = x[0] + (midpoint * (x[1] - x[0]))

    super().__init__(x, density)
    for (i, x) in enumerate(self.x):
      self.y[i] = 1 / (1 + math.exp(-steepness * (x - midpoint)))

class Linear(Path):
  def __init__(self, x, density = 1.0, slope = 1.0, y_intercept = 0.0):
    super().__init__(x, density)
    for (i, x) in enumerate(self.x):
      self.y[i] = slope * x + y_intercept

class Bounded(Path):
  def __init__(self, lower, upper, fn=random.uniform):
    if not lower.is_congruent(upper):
      raise Exception('cong fail')

    self.x = [x for x in lower.x]
    self.y = [fn(lower.y[i], upper.y[i]) for i in range(len(lower.y))]

  def by(p, ydelta, fn=random.uniform):
    """Return a new random path bounded by +/- ydelta."""
    return Bounded(
      lower=p.copy().translateY(-ydelta),
      upper=p.copy().translateY(+ydelta),
      fn=fn,
    )
