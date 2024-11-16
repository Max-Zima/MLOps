#ifndef MIPT_MLOPS_HW_1_HADAMARDPRODUCT_H
#define MIPT_MLOPS_HW_1_HADAMARDPRODUCT_H

#pragma once
#include <vector>

class hadamard {
public:
    static std::vector<std::vector<double>> product (const std::vector<std::vector<double>> &a,
                                                     const std::vector<std::vector<double>> &b);
};

#endif // MIPT_MLOPS_HW_1_HADAMARDPRODUCT_H
