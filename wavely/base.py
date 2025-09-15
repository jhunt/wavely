from .exceptions import ValueOutOfRangeException

import math

class Path():
  def __init__(self, x, density = 1.0):
    if x is None:
      return

    if density <= 0.0:
      raise ValueRangeException(f'path density must range from (0,∞); given value {density} is out of range.')

    if not isinstance(x, tuple):
      self.x = x
      self.y = [0 for _ in x]

    else:
      span    = x[1] - x[0]
      samples = math.ceil(span * density)
      delta   = span / float(samples)

      self.x = [x[0] + delta * i for i in range(samples)]
      self.y = [0 for i in range(samples)]

  def copy(self):
    p = Path(None)
    p.x = [x for x in self.x]
    p.y = [y for y in self.y]
    return p

  def min(self):
    """Find the smallest Y component."""
    return min(self.y)

  def max(self):
    """Find the largest Y component."""
    return max(self.y)

  def shape(self):
    return (min(self.x), max(self.x)+1)

  def scale(self, ydelta):
    """Scale the Y components, uniformly."""
    self.y = [y * (1. + ydelta) for y in self.y]
    return self

  def translateX(self, xdelta):
    """Translate the X components by xdelta units along the X axis."""
    self.x = [x + xdelta for x in self.x]
    return self

  def translateY(self, ydelta):
    """Translate the Y components by xdelta units along the Y axis."""
    self.y = [y + ydelta for y in self.y]
    return self

  def translate(self, xdelta, ydelta):
    """Translate in both X and Y directions."""
    return self.translateX(xdelta).translateY(ydelta)

  def zero(self):
    """Anchor the current Path to the (0,0) origin point."""
    return self.translate(-1.0 * self.x[0], -1.0 * self.y[0])

  def baseline(self):
    """Drop the current Path such that min(Y) = 0."""
    return self.translateY(-1.0 * self.min())

  def append(self, succ):
    """Append the (x,y) pairs from the successor Path (succ) to this Path."""
    succ.zero().translate(self.x[-1], self.y[-1])
    self.x += succ.x[1:]
    self.y += succ.y[1:]
    return self

  def repeat(self, n=1):
    """Repeat the current Path n times."""
    _x = [x for x in self.x]
    _y = [y for y in self.y]

    dx = _x[-1] - _x[0]
    dy = _y[-1] - _y[0]

    for i in range(n):
      self.x += [x + (i+1)*dx for x in _x]
      self.y += [y + (i+1)*dy for y in _y]
    return self

  def sample(self, m):
    """Sample every 1/m (x,y) pair from the current Path."""
    x = [self.x[i*m] for i in range(math.floor(len(self.x) / float(m)))]
    y = [self.y[i*m] for i in range(math.floor(len(self.x) / float(m)))]
    return Literal(x, y)

  def mix(self, other):
    if not self.is_congruent(other):
      raise Exception('cong fail')
    self.y = [(self.y[i] + other.y[i]) / 2.0 for i in range(len(self.y))]
    return self

  def is_congruent(self, other):
    """Predicate for congruency along the X axis for self and other Paths."""
    if len(other.x) != len(self.x):
      return False
    for (i, x) in enumerate(other.x):
      if self.x[i] != x:
        return False
    return True

class Literal(Path):
  def __init__(self, x, y):
    self.x = x
    self.y = y

