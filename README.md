wavely
======

A small library for building curve coordinates from simple
components.

With `wavely`, you can describe a complex curve piecemeal, using
scaled and transalted sigmoid and linear components, mix complex
curves together, and generate noisy, semi-random curves within
constraints.

This is perfect for synthesizing data with observable
characteristics without losing verisimilitude.

I use it for demos.

## Examples

The `examples.py` script will flip through a series of plots,
showing different ways of dealing with the `Linear` and `Sigmoid`
primitives and the `Bounded` aggregate.

![Example: Unit Curves][1]

![Example: Linear Curves][2]

![Example: Sigmoid Curves][3]

![Example: Bounded Random Curves][4]

![Example: Seasonal Curves][5]

[1]: https://raw.githubusercontent.com/jhunt/wavely/refs/heads/main/docs/unit.png
[2]: https://raw.githubusercontent.com/jhunt/wavely/refs/heads/main/docs/example-linear.png
[3]: https://raw.githubusercontent.com/jhunt/wavely/refs/heads/main/docs/example-sigmoid.png
[4]: https://raw.githubusercontent.com/jhunt/wavely/refs/heads/main/docs/example-bounded-random.png
[5]: https://raw.githubusercontent.com/jhunt/wavely/refs/heads/main/docs/example-seasonal.png
