from func3_lib.func3_lt import transpose2d


def test_transpose2d() -> None:
    test_result = transpose2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert test_result == result
