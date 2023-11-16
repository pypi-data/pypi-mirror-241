import numpy as np
from game_generators.functions.interpolate import interpolate_table
from game_generators.utils.transforms import scale_array


def increasing_table(dim, batch_size=1, min_y=0, max_y=10, num_points=10, rng=None, seed=None):
    """Create a table of increasing values.

    Args:
        dim (int): The dimension of the table.
        batch_size (int, optional): The batch size. Defaults to 1.
        min_y (int, optional): The minimum value. Defaults to 0.
        max_y (int, optional): The maximum value. Defaults to 10.
        num_points (int, optional): The number of points. Defaults to 10.
        rng (np.random.Generator, optional): The random number generator. Defaults to None.
        seed (int, optional): The random seed. Defaults to None.

    Returns:
        np.ndarray: The table of increasing values.
    """
    rng = rng if rng is not None else np.random.default_rng(seed)

    values = rng.uniform(low=0, high=1, size=(batch_size, *([num_points] * dim)))

    for d in range(dim):
        values = values.cumsum(axis=d + 1)

    # Extract the minimum and maximum values for each batch.
    min_values = values[(slice(None),) + ((0,) * dim)].reshape(batch_size, *([1] * dim))
    max_values = values[(slice(None),) + ((-1,) * dim)].reshape(batch_size, *([1] * dim))

    # Scale the table to the desired range
    return scale_array(values, min_values, max_values, min_y, max_y)


def decreasing_table(dim, batch_size=1, min_y=0, max_y=10, num_points=10, rng=None, seed=None):
    """Create a table of decreasing values.

    Args:
        dim (int): The dimension of the table.
        batch_size (int, optional): The batch size. Defaults to 1.
        min_y (int, optional): The minimum value. Defaults to 0.
        max_y (int, optional): The maximum value. Defaults to 10.
        num_points (int, optional): The number of points. Defaults to 10.
        rng (np.random.Generator, optional): The random number generator. Defaults to None.
        seed (int, optional): The random seed. Defaults to None.

    Returns:
        np.ndarray: The table of decreasing values.
    """
    values = -increasing_table(
        dim, batch_size=batch_size, min_y=min_y, max_y=max_y, num_points=num_points, rng=rng, seed=seed
    )
    return values + (max_y - min_y)


def increasing(dim, batch_size=1, batched=True, min_y=0, max_y=10, num_points=10, rng=None, seed=None):
    """Create an increasing function.

    Args:
        dim (int): The dimension of the function.
        batch_size (int, optional): The batch size. Defaults to 1.
        batched (bool, optional): Whether the function is batched or not. Defaults to True.
        min_y (int, optional): The minimum value. Defaults to 0.
        max_y (int, optional): The maximum value. Defaults to 10.
        num_points (int, optional): The number of points. Defaults to 10.
        rng (np.random.Generator, optional): The random number generator. Defaults to None.
        seed (int, optional): The random seed. Defaults to None.

    Returns:
        callable: An increasing function.
    """
    values = increasing_table(
        dim, batch_size=batch_size, min_y=min_y, max_y=max_y, num_points=num_points, rng=rng, seed=seed
    )
    batched = batch_size > 1 or batched
    if not batched:
        values = values[0]
    increasing_f = interpolate_table(values, batched=batched, method="linear")
    return increasing_f


def decreasing(dim, batch_size=1, batched=True, min_y=0, max_y=10, num_points=10, rng=None, seed=None):
    """Create a decreasing function.

    Args:
        dim (int): The dimension of the function.
        batch_size (int, optional): The batch size. Defaults to 1.
        batched (bool, optional): Whether the function is batched or not. Defaults to True.
        min_y (int, optional): The minimum value. Defaults to 0.
        max_y (int, optional): The maximum value. Defaults to 10.
        num_points (int, optional): The number of points. Defaults to 10.
        rng (np.random.Generator, optional): The random number generator. Defaults to None.
        seed (int, optional): The random seed. Defaults to None.

    Returns:
        callable: A decreasing function.
    """
    values = decreasing_table(
        dim, batch_size=batch_size, min_y=min_y, max_y=max_y, num_points=num_points, rng=rng, seed=seed
    )
    batched = batch_size > 1 or batched
    if not batched:
        values = values[0]
    decreasing_f = interpolate_table(values, batched=batched, method="linear")
    return decreasing_f
