import wavely as wv
import matplotlib.pyplot as plt

def plot(title, *paths):
  fig, ax = plt.subplots(figsize=(12, 8))
  colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']

  for i, (label, path) in enumerate(paths):
    color = colors[i % len(colors)]
    ax.plot(path.x, path.y, color=color, linewidth=2, label=label, marker='o', markersize=3)

    ax.set_title(title)
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True, alpha=0.3)
    ax.legend()
  plt.show()

plot("Linear Paths",
  ("y = 1.5x - 1", wv.Linear((-5, 5), slope=1.5, y_intercept=-1)),
  ("y =   3x + 7", wv.Linear((-5, 5), slope=3.0, y_intercept=+7)))

plot("Sigmoid Paths",
  ("Basic Sigmoid",   wv.Sigmoid(( -5,  5), density=5.0, steepness=1.0)),
  ("Steep Sigmoid",   wv.Sigmoid(( -3,  3), density=3.0, steepness=3.0).scale(4)),
  ("Custom Midpoint", wv.Sigmoid((-10, 10), steepness=0.5, midpoint=0.1)))

plot("Unit Paths",
  ("Unit Sigmoid", wv.Sigmoid((-5, 5), density=10.0, steepness=1.0, midpoint=0.5)),
  ("Unit Sigmoid", wv.Sigmoid((-5, 5), density=10.0, steepness=-1.0, midpoint=0.5)),
  ("Bell", wv.Sigmoid((-5, 0), density=10.0, steepness=2.0, midpoint=0.5) \
             .append(wv.Sigmoid((0, 5), density=10.0, steepness=-2.0, midpoint=0.5))),
  ("Bell", wv.Sigmoid((-5, 0), density=10.0, steepness=-2.0, midpoint=0.5) \
             .append(wv.Sigmoid((0, 5), density=10.0, steepness=2.0, midpoint=0.5))),
  ("Unit Line", wv.Linear((-5, 5), density=10.0, slope=0.1, y_intercept=0.5)),
  ("Unit Line", wv.Linear((-5, 5), density=10.0, slope=-0.1, y_intercept=0.5)),
  ("Unit Line", wv.Linear((-5, 5), density=10.0, slope=0, y_intercept=0.5)))

upper = wv.combine(
  wv.Sigmoid((0, 10), density=4.0, steepness=1.0),
  wv.Sigmoid((0, 6), density=4.0, steepness=3.0).scale(5),
  wv.Sigmoid((0, 20),density=4.0, steepness=0.5, midpoint=0.1))
lower = wv.combine(
  wv.Sigmoid((0, 12), density=4.0, steepness=1.0).translateY(-2),
  wv.Sigmoid((0, 10), density=4.0, steepness=2.0).scale(4.9),
  wv.Sigmoid((0, 14), density=4.0, steepness=0.7, midpoint=0.4))

plot("Bounded Composite Paths",
  ("Upper Bounds", upper),
  ("Lower Bounds", lower),
  ("Bounded Random", wv.Bounded(lower, upper)))

plot("Seasonal Paths",
  ("Seasonal", wv.seasonal(a=(90, 10), b=(180, -5), c=(270, 15), t=360)),
  ("Seasonal", wv.seasonal(a=(60, 11), b=(180, 25), c=(310, -1), t=360)))
