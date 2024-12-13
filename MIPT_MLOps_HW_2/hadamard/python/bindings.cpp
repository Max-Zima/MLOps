#include "HadamardProduct.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(hadamard_core, m) {
    m.doc() = R"doc(
        Python bindings for HadamardProduct library
    )doc";

    m.def("product", &hadamard::product, R"doc(
            Perform the Hadamard product of two matrices.

            Parameters:
                a : list of list of float
                    The first matrix.
                b : list of list of float
                    The second matrix.

            Returns:
                list of list of float
                    The result of matrix Hadamard Product.
        )doc");
}
