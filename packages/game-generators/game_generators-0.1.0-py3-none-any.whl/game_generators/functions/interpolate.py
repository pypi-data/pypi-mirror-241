import numpy as np
from scipy.interpolate import RegularGridInterpolator


def interpolate_table(table_function, batched=False, method="linear"):
    """Interpolate a table function.

    Note:
        This function is a wrapper for scipy.interpolate.RegularGridInterpolator.

    Args:
        table_function (np.array): A table function.
        batched (bool, optional): Whether to return a batched interpolation function. Defaults to False.
        method (str, optional): The interpolation method. Defaults to 'linear'.

    Returns:

    """
    table_shape = table_function.shape if not batched else table_function.shape[1:]
    table_points = [np.arange(n) for n in table_shape]

    if not batched:
        return RegularGridInterpolator(table_points, table_function, method=method)
    else:
        return [RegularGridInterpolator(table_points, table, method=method) for table in table_function]
