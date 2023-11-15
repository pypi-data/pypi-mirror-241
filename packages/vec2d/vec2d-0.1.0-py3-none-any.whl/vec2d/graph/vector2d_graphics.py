"""
A library to draw simple figures such as points, segments, polygons, and arrows
in the 2D plane using Matplotlib as the backend.
The library exposes classes for the figures, an enumeration for the common
colors, and a function draw() to render the figures.
"""
import logging
from abc import ABC, abstractmethod
from enum import Enum
from math import ceil, floor, sqrt
from typing import Optional, Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlim, ylim
from matplotlib.patches import Polygon as pyplot_poly
from matplotlib.collections import PatchCollection

logging.basicConfig(
    format="%(asctime)s [%(levelname)8s] (%(name)s) | %(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("Using vec2d.graph v0.2.0")


class Colors(Enum):
    """A few Matplotlib colors using the CN scheme in which
    'C' precedes a number acting as an index into the default
    property cycle
    (see https://matplotlib.org/stable/users/explain/colors/colors.html).
    """

    BLUE = "C0"
    BLACK = "k"
    RED = "C3"
    GREEN = "C2"
    PURPLE = "C4"
    BROWN = "C5"
    PINK = "C6"
    ORANGE = "C11"
    GRAY = "gray"


class Figure2D(ABC):
    """Abstract base class for all the figures that can be represented
    in the 2D plane.
    """

    @abstractmethod
    def extract_vectors(self) -> tuple[int | float, int | float]:
        """Generator function that returns the vectors (points) that define the
        figure.

        Returns:
            tuple[int | float, int | float]: a tuple with the corresponding
                vector coordinates in the 2D plane.
        """

    @abstractmethod
    def render(self) -> None:
        """Performs the necessary actions on Matplotlib to render the
        corresponding figure on screen.
        """

    def normalize_color(self, color):
        """Normalize the color with which a Figure2D has been initialized so
        that it matches Matplotlib's native handling of colors. That way, either
        a color from Colors enumeration, a Matplotlib color, or a value from a
        colormap can be used."""
        return color.value if hasattr(color, "value") else color


class Points(Figure2D):
    """Represents a collection of points on the 2D plane, given their
    (x,y) coordinates. The points will be displayed as dots in the
    given color. By default, the points will be drawn in black color.
    """

    def __init__(
        self, *vectors: tuple[int | float, int | float], color=Colors.BLACK
    ) -> None:
        self.vectors = list(vectors)
        self.color = self.normalize_color(color)

    def extract_vectors(self) -> tuple[int | float, int | float]:
        for v in self.vectors:
            yield v

    def render(self) -> None:
        xs = [v[0] for v in self.vectors]
        ys = [v[1] for v in self.vectors]
        plt.scatter(xs, ys, color=self.color)


class Segment(Figure2D):
    """Represents a segment on the 2D plane, with a start point and
    an end point using their (x, y) coordinates. The segment will be drawn
    using the given color. By default, the segment will be drawn in blue.
    """

    def __init__(
        self,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float],
        *,
        color: Colors = Colors.BLUE,
    ) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.color = self.normalize_color(color)

    def extract_vectors(self) -> tuple[int | float, int | float]:
        yield self.start_point
        yield self.end_point

    def render(self) -> None:
        x1, y1 = self.start_point  # pylint: disable=invalid-name
        x2, y2 = self.end_point  # pylint: disable=invalid-name
        plt.plot([x1, x2], [y1, y2], color=self.color)


class Polygon(Figure2D):
    """Represents a polygon on the 2D plane, defined by its vertices using their
    (x,y) coordinates. You can specify the color of the lines delimiting the
    polygon using color. By default, the lines will be drawn in blue. If a color
    is specified for the fill parameter, the polygon will be filled. By default,
    the polygon will not be filled. The alpha parameter can be used to
    established the alpha blending parameter. By default, the alpha blending is
    set to a 0.4 value.
    """
    def __init__(
        self,
        *vertices: tuple[int | float, int | float],
        color=Colors.BLUE,
        fill: Optional[Colors] = None,
        alpha=0.4,
    ) -> None:
        self.vertices = vertices
        self.color = self.normalize_color(color)
        self.fill = self.normalize_color(fill)
        self.alpha = alpha

    def extract_vectors(self) -> tuple[int | float, int | float]:
        for v in self.vertices:  # pylint: disable=invalid-name
            yield v

    def render(self) -> None:
        if self.color:
            for i in range(0, len(self.vertices)):
                x1, y1 = self.vertices[i]
                x2, y2 = self.vertices[(i + 1) % len(self.vertices)]
                plt.plot([x1, x2], [y1, y2], color=self.color)

        if self.fill:
            patches = []
            poly = pyplot_poly(self.vertices, closed=True)
            patches.append(poly)
            patch_collection = PatchCollection(patches, color=self.fill)
            plt.gca().add_collection(patch_collection)


class Arrow(Figure2D):
    """Represents an arrow on the 2D plane, defined by its tip and tail
    specified by their coordinates (x, y). If tail is not provided the arrow is
    assumed to have its tail in the origin of coordinates (0, 0). The color
    argument sets the color of the segment and head of the arrow. By default,
    arrows are drawn in red.
    """

    def __init__(
        self,
        tip: tuple[int | float, int | float],
        tail=(0, 0),
        color=Colors.RED,
    ) -> None:
        self.tip = tip
        self.tail = tail
        self.color = self.normalize_color(color)

    def extract_vectors(self) -> tuple[int | float, int | float]:
        yield self.tip
        yield self.tail

    def render(self) -> None:
        tip, tail = self.tip, self.tail
        tip_length = (xlim()[1] - xlim()[0]) / 20.0
        length = sqrt((tip[1] - tail[1]) ** 2 + (tip[0] - tail[0]) ** 2)
        new_length = length - tip_length
        new_y = (tip[1] - tail[1]) * (new_length / length)
        new_x = (tip[0] - tail[0]) * (new_length / length)
        plt.gca().arrow(
            tail[0],
            tail[1],
            new_x,
            new_y,
            head_width=tip_length / 1.5,
            head_length=tip_length,
            fc=self.color,
            ec=self.color,
        )


def draw(
    *objects: Sequence[Figure2D],
    origin=True,
    axes=True,
    grid=(1, 1),
    nice_aspect_ratio=True,
    width=6,
    save_as: str = None,
):
    """Draws the given objects as a Matplotlib object with the given
    configuration

    Args:
        objects (Sequence[Figure2D]): the list of figures to be displayed in the
            plot.
        origin (bool, optional): whether to show or hide the origin of
            coordinates. Default is to show the origin (True). You can pass None
            or False if you don't want the origin to be displayed.
        axes (bool, optional): whether to show the x- and y-coordinate axes.
            Default is to show the axes (True). You can pass None or False if
            you don't want the axes to be displayed.
        grid (tuple[int | float, int | float], optional): sets the frequency for
            the ticks in the plot for x- and y- axes. Default is (1, 1) meaning
            that you will find a tick per unit in both x- and y- axes. You can
            pass None or False if you don't want the grid to be displayed.
        nice_aspect_ratio (bool): whether to adjust the aspect ratio, so that a
            square of side one is displayed as a square, instead of as a
            rectangle. Default is True.
        width (int | float): the width of the plot in inches. The larger this
            number, the bigger the plot. Default is 6 which is OK for most
            monitors and 2D drawings.
        save_as (str, optional): path of the file to be created with the plot,
            or None if no file is to be created.
    """
    all_vectors = [vec for obj in objects for vec in obj.extract_vectors()]
    xs, ys = zip(*all_vectors)  # pylint: disable=invalid-name
    max_x, max_y, min_x, min_y = (
        max(0, *xs),
        max(0, *ys),
        min(0, *xs),
        min(0, *ys),
    )

    if grid:
        x_padding = max(ceil(0.05 * (max_x - min_x)), grid[0])
        y_padding = max(ceil(0.05 * (max_y - min_y)), grid[1])

        plt.xlim(
            floor((min_x - x_padding) / grid[0]) * grid[0],
            ceil((max_x + x_padding) / grid[0]) * grid[0],
        )
        plt.ylim(
            floor((min_y - y_padding) / grid[1]) * grid[1],
            ceil((max_y + y_padding) / grid[1]) * grid[1],
        )
    else:
        x_padding = 0.05 * (max_x - min_x)
        y_padding = 0.05 * (max_y - min_y)

        plt.xlim(min_x - x_padding, max_x + x_padding)
        plt.ylim(min_y - y_padding, max_y + y_padding)

    if origin:
        plt.scatter([0], [0], color=Colors.BLACK.value, marker="x")

    if grid:
        plt.gca().set_xticks(np.arange(plt.xlim()[0], plt.xlim()[1], grid[0]))
        plt.gca().set_yticks(np.arange(plt.ylim()[0], plt.ylim()[1], grid[1]))
        plt.grid(True)
        plt.gca().set_axisbelow(True)

    if axes:
        plt.gca().axhline(linewidth=2, color=Colors.BLACK.value)
        plt.gca().axvline(linewidth=2, color=Colors.BLACK.value)

    if nice_aspect_ratio:
        coords_height = ylim()[1] - ylim()[0]
        coords_width = xlim()[1] - xlim()[0]
        plt.gcf().set_size_inches(width, width * coords_height / coords_width)

    for obj in objects:
        obj.render()

    if save_as:
        plt.savefig(save_as)

    plt.show()
