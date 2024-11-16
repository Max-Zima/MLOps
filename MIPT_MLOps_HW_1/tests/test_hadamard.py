import hadamard

def test_hadamard_product():
    mat1 = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
    ]
    mat2 = [
        [9.0, 8.0, 7.0],
        [6.0, 5.0, 4.0],
        [3.0, 2.0, 1.0],
    ]
    expected = [
        [9.0, 16.0, 21.0],
        [24.0, 25.0, 24.0],
        [21.0, 16.0, 9.0],
    ]
    result = hadamard.product(mat1, mat2)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_hadamard_product()
    print("All tests passed!")
