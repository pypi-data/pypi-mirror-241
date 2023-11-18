import numpy as np
from numba import njit

@njit('(int64[:,:], int64[:,:], float64)')
def find_midpoints(bp_1: np.ndarray, bp_2: np.ndarray, percentile: float = 0.5) -> np.ndarray:
    """
    Compute the midpoints between two sets of 2D points based on a given percentile.

    :parameter np.ndarray bp_1: An array of 2D points representing the first set of points. Rows represent frames. First column represent x coordinates. Second column represent y coordinates.
    :parameter np.ndarray bp_2: An array of 2D points representing the second set of points. Rows represent frames. First column represent x coordinates. Second column represent y coordinates.
    :parameter float percentile: The percentile value to determine the distance between the points for calculating midpoints. When set to 0.5 it calculates midpoints at the midpoint of the two points.
    :returns: np.ndarray: An array of 2D points representing the midpoints between the points in bp_1 and bp_2 based on the specified percentile.

    :example:
    >>> bp_1 = np.array([[1, 3], [30, 10]]).astype(np.int64)
    >>> bp_2 = np.array([[10, 4], [20, 1]]).astype(np.int64)
    >>> find_midpoints(bp_1=bp_1, bp_2=bp_2, percentile=0.5)
    >>> [[ 5,  3], [25,  6]]
    """

    result = np.full(bp_1.shape, np.nan)
    for i in range(bp_1.shape[0]):
        frm_bp1, frm_bp2 = bp_1[i], bp_2[i]
        x_dist = max(frm_bp1[0], frm_bp2[0]) - min(frm_bp1[0], frm_bp2[0])
        y_dist = max(frm_bp1[1], frm_bp2[1]) - min(frm_bp1[1], frm_bp2[1])
        x_dist_percentile, y_dist_percentile = int(x_dist * percentile), int(y_dist * percentile)
        if frm_bp2[0] > frm_bp1[0]:
            new_x = frm_bp1[0] + x_dist_percentile
        else:
            new_x = frm_bp1[0] - x_dist_percentile
        if frm_bp2[1] > frm_bp1[1]:
            new_y = frm_bp1[1] + y_dist_percentile
        else:
            new_y = frm_bp1[1] - y_dist_percentile

        result[i] = np.array([new_x, new_y])

    return result.astype(np.int64)











bp_1 = np.array([[1, 3], [30, 10]]).astype(np.int64)
bp_2 = np.array([[10, 4], [20, 1]]).astype(np.int64)

find_midpoints(bp_1=bp_1, bp_2=bp_2, percentile=0.5)