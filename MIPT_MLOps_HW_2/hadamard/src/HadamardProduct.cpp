#include "HadamardProduct.h"
#include <stdexcept>

std::vector<std::vector<double>> hadamard::product (const std::vector<std::vector<double>> &a,
                                                  const std::vector<std::vector<double>> &b) {

    size_t aRows = a.size();
    size_t aCols = a[0].size();
    size_t bRows = b.size();
    size_t bCols = b[0].size();

    if ((aRows != bRows) || (aCols != bCols)) {
        throw std::invalid_argument("Vectors must be of the same size");
    }

    size_t rows = aRows;
    size_t cols = aCols;

    std::vector<std::vector<double>> result(rows, std::vector<double>(cols));
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            result[i][j] = a[i][j] * b[i][j];
        }
    }

    return result;
}