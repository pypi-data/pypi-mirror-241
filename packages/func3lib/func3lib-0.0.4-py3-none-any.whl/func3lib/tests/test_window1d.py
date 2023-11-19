import numpy as np
from func3_lib.func3_lt import window1d


def test_window1d() -> None:
    # Define a 1D numpy array
    input_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Define the window size, shift, and stride
    size = 3
    shift = 2
    stride = 1

    # Call the window1d function
    test_result_windows = window1d(input_array, size, shift, stride)

    # Define the expected result
    result_windows = [
        np.array([1, 2, 3]),
        np.array([3, 4, 5]),
        np.array([5, 6, 7]),
        np.array([7, 8, 9]),
    ]

    assert all(
        np.array_equal(a, b) for a, b in zip(test_result_windows, result_windows)
    )
