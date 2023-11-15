"""
A library providing a few Math related functions for the 2D plane.
"""
from math import cos, pi, sin, sqrt, atan2


def add(
    v1: tuple[int | float, int | float], v2: tuple[int | float, int | float]
) -> tuple[int | float, int | float]:
    """Performs the addition of vectors

    Args:
        v1 (tuple[int | float, int | float]): the first 2D vector to be added
        v2 (tuple[int | float, int | float]): the second 2D vector to be added

    Returns:
        tuple[int | float, int | float]: the vector sum
    """
    return (v1[0] + v2[0], v1[1] + v2[1])


def add_mult(*v: tuple[int | float, int | float]) -> tuple[int | float]:
    """Variadic version of the add function for 2D vectors

    Args:
        *v (tuple[int | float, int | float]): a variable number of 2D vectors

    Returns:
        tuple[int | float, int | float]: the vector sum
    """
    if len(v) < 2:
        raise ValueError("at least two vectors were expected")
    return (sum([x for x, _ in v]), sum([y for _, y in v]))


def length(v: tuple[int | float, int | float]) -> float:
    """Calculates the length of a vector

    Args:
        v (tuple[int | float, int | float]): the 2D vector

    Returns:
        float: the length of the vector
    """
    return sqrt(v[0] ** 2 + v[1] ** 2)


def scalar_product(
    v: tuple[int | float, int | float], s: int | float
) -> tuple[int | float, int | float]:
    """Calculates the scalar multiplication

    Args:
        v (tuple[int | float, int | float]): the 2D vector
        s (int | float): the scalar

    Returns:
        tuple[int | float, int | float]: the result of the scalar multiplication
    """
    return (v[0] * s, v[1] * s)


def scale(
    s: int | float,
    v: tuple[int | float, int | float],
) -> tuple[int | float, int | float]:
    """Scales the given vector v by the scalar s. This function is an alias of
    scalar_product.

    Args:
        s (int | float): the scalar
        v (tuple[int | float, int | float]): the 2D vector to scale


    Returns:
        tuple[int | float, int | float]: the result of scaling v by the scalar s
    """
    return scalar_product(v, s)


def opposite(
    v: tuple[int | float, int | float]
) -> tuple[int | float, int | float]:
    """Calculates the opposite of a given vector
    Args:
        v (tuple[int | float, int | float]): the 2D vector

    Returns:
        tuple[int | float, int | float]: the result of calculating the opposite
            of the given vector
    """
    return (-v[0], -v[1])


def subtract(
    v: tuple[int | float, int | float], w: tuple[int | float, int | float]
) -> tuple[int | float, int | float]:
    """Calculates the vector that results from subtracting w from v, that is
    the *displacement vector*.

    Args:
        v (tuple[int | float, int | float]): the first 2D vector
        w (tuple[int | float, int | float]): the second 2D vector

    Returns:
        tuple[int | float, int | float]: the vector that results from
            subtracting w from v, in other words, the displacement vector.
    """
    return (v[0] - w[0], v[1] - w[1])


def displacement(
    tip: tuple[int | float, int | float], tail: tuple[int | float, int | float]
) -> tuple[int | float, int | float]:
    """Calculates the displacement vector that goes from tail to tip, in other
    words, it computes tip - tail vector.

    Args:
        tip (tuple[int | float, int | float]): the tip of the displacement
            vector
        tail (tuple[int | float, int | float]): the tail of the displacement
            vector

    Returns:
        tuple[int | float, int | float]: the vector that results from
            subtracting w from v, in other words, the displacement vector.
    """
    return subtract(tip, tail)


def distance(
    tip: tuple[int | float, int | float], tail: tuple[int | float, int | float]
) -> int | float:
    """Calculates the distance that goes from tail to tip, in other
    words, it computes the length of the displacement vector from tail to tip.

    Args:
        tip (tuple[int | float, int | float]): the tip of the displacement
            vector
        tail (tuple[int | float, int | float]): the tail of the displacement
            vector

    Returns:
        int | float: the distance between the given vectors
    """
    return length(displacement(tip, tail))


def translate(
    translation_vector: tuple[int | float, int | float],
    vectors: list[tuple[int | float, int | float]],
) -> list[tuple[int | float, int | float]]:
    """Takes a translation vector and a list of input vectors and returns a list
    of the input vectors all translated by the translated vector.

    Args:
        translation_vector (tuple[int | float, int | float]): the translation
            vector
        vectors (list[tuple[int | float, int | float]]): the list of vectors to
            be translated

    Returns:
        list[tuple[int | float, int | float]]: the list of vectors that results
            from translating all the given vectors.
    """
    if len(vectors) == 0:
        raise ValueError("expected a non-empty list of vectors")

    return [add(translation_vector, v) for v in vectors]


def rotate(
    angle: float,
    vectors: list[tuple[int | float, int | float]],
) -> list[tuple[int | float, int | float]]:
    """Takes an angle in radians and a list of input vectors and returns a list
    of the input vectors all of them rotated by the given angle counterclockwise
    about the origin if the given angle is positive, or clockwise if the given
    angle is negative.

    Args:
        angle (float]): the angle (in radians) that will be used in the rotation
        vectors (list[tuple[int | float, int | float]]): the list of vectors in
        to Cartesian coordinates to be rotated

    Returns:
        list[tuple[int | float, int | float]]: the list of vectors that results
            from rotating all the given vectors by the given angle.
    """
    if len(vectors) == 0:
        raise ValueError("expected a non-empty list of vectors")

    vectors_polar = [to_polar(v) for v in vectors]
    return [to_cartesian((r, theta + angle)) for r, theta in vectors_polar]

def rescale(
    factor: float,
    vectors: list[tuple[int | float, int | float]],
) -> list[tuple[int | float, int | float]]:
    """Takes a scaling factor and a list of input vectors and returns a list
    of the input vectors all of them scaled by the given factor.

    Args:
        factor (float]): the factor to be used when scaling.
        vectors (list[tuple[int | float, int | float]]): the list of vectors in
        to Cartesian coordinates to be rotated

    Returns:
        list[tuple[int | float, int | float]]: the list of vectors that results
            from scaling all the given vectors by the given factor.
    """
    if len(vectors) == 0:
        raise ValueError("expected a non-empty list of vectors")

    return [scale(factor, v) for v in vectors]


def perimeter(vectors: list[tuple[int | float, int | float]]) -> int | float:
    """Computes the perimeter of the shape defined by the given vectors.

    Args:
        vectors (list[tuple[int | float, int | float]]): the list of vectors/
            points that define the 2D shape.

    Returns:
        int | float: the perimeter of the 2D shape
    """
    distances = [
        distance(vectors[i], vectors[(i + 1) % len(vectors)])
        for i in range(0, len(vectors))
    ]
    return sum(distances)


def to_cartesian(polar_vector: tuple[float, float]) -> tuple[float, float]:
    """Returns the Cartesian coordinates (x, y) of a vector given its polar
    coordinates (r, θ), where r is the length of the vector and the angle θ is
    expressed in radians, measured counterclockwise from the positive x axis.

    Args:
        polar_vector (tuple[float, float]): the vector in polar coordinates
            (radius and angle).

    Returns:
        tuple[float, float]: the Cartesian coordinates (x, y) of the vector.
    """
    length, angle = polar_vector
    return (length * cos(angle), length * sin(angle))


def to_polar(cartesian_vector: tuple[float, float], positive_angle=False) -> tuple[float, float]:
    """Returns the polar coordinates (r, θ) of a vector, where r is the length
    of the vector and the angle θ is expressed in radians, measured
    counterclockwise from the positive x axis given its Cartesian coordinates
    (x, y).

    Args:
        cartesian_vector (tuple[float, float]): the vector in Cartesian
        coordinates (x, y).
        positive_angle (bool, Optional): forces the angle to have a positive
            value. Otherwise, angles greater than pi will have negative values.

    Returns:
        tuple[float, float]: the polar coordinates (r, θ) of the vector.
    """
    x, y = cartesian_vector
    angle = atan2(y, x)
    if positive_angle and angle < 0:
        angle += 2 * pi
    return (length(cartesian_vector), angle)


def to_radians(angle_deg: float) -> float:
    """Returns the radians value for an angle expressed in degrees.

    Args:
        angle_deg (float): the value of the angle express in degrees.

    Returns:
        float: the equivalent angle expressed in radians.
    """
    return angle_deg * pi / 180


def to_degrees(angle_rad: float) -> float:
    """Returns the degrees value for an angle expressed in radians.

    Args:
        angle_rad (float): the value of the angle express in radians.

    Returns:
        float: the equivalent angle expressed in degrees.
    """
    return angle_rad * 180 / pi
