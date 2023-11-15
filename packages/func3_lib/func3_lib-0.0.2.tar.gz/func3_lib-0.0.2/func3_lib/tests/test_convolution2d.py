import numpy as np
from func3_lib.func3_lt import convolution2d


def test_convolution2d() -> None:
    input_matrix = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )

    kernel = np.array([[1, 0], [0, 1]])

    test_result = convolution2d(input_matrix, kernel, stride=2)

    result = np.array([[7.0, 11.0], [23.0, 27.0]])

    assert all(np.array_equal(a, b) for a, b in zip(test_result, result))
