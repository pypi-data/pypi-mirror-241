# Vector2D library
> Helper library with Math and graphing related functions for vectors in the 2D plane.

## Usage

Install the library by typing:

```bash
python -m pip install vec2d
```

Once installed, you'll have access to the Math and graphing packages:

```python
from vec2d.math import add
from vec2d.graph import draw, Arrow, Colors

u = (2, 0)
v = (1, 3)

draw(
    Arrow(u, color=Colors.ORANGE),
    Arrow(v, color=Colors.PINK),
    Arrow(add(u, v), color=Colors.BLUE)
)
```

The functions in the `vec2d.math` library are self-explanatory. Vectors are represented and tuples with `int` or `float` components.

The `vec2d.graph` is a helper library for graphing related capabilities for 2D objects. With it you can draw simple figures such as points, segments, polygons, and arrows on the 2D plane using Matplotlib as the backend in a very simple way and without any hassle.

The library exposes classes for the figures, an enumeration for the common colors, and a function `draw` to render the figures as Matplotlib plots.

| Class | Constructor example | Description |
| :---- | :------------------ | :---------- |
| `Polygon` | `Polygon(*vectors)` | Draws a polygon whose vertices are represented by the given list of vectors. |
| `Points` | `Points(*vectors)` | Represents a list of points (i.e., dots), one at each of the input vectors. |
| `Arrow` | `Arrow(tip)`<br>`Arrow(tip, tail)` | Draws an arrow from the origin to the `tip` vector, or from the `tail` vector to the `tip` vector if `tail` if given. |
| `Segment` | `Segment(start, end)` | Draws a line segment from the start to the vector end. |

## See Also

See also [vec3d](https://pypi.org/project/vec3d/) for a similar library for vectors in the 3D space.

## Acknowledgements

This library is a small refactoring of https://github.com/orlandpm/Math-for-Programmers library.
