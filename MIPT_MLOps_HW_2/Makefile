CXX=g++
CXXFLAGS=-std=c++11 -O3 -march=native -Wall -I$(SRC_DIR) $(shell python3 -m pybind11 --includes)
PY_LDFLAGS=$(shell python3-config --ldflags) -shared -fPIC
SRC_DIR=hadamard/src
PYTHON_DIR=hadamard/python

all: hadamard_core

hadamard_core: $(PYTHON_DIR)/bindings.o $(SRC_DIR)/HadamardProduct.o
	$(CXX) $^ -o $(PYTHON_DIR)/hadamard_core`python3-config --extension-suffix` $(PY_LDFLAGS)

$(PYTHON_DIR)/bindings.o: $(PYTHON_DIR)/bindings.cpp $(SRC_DIR)/HadamardProduct.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

$(SRC_DIR)/HadamardProduct.o: $(SRC_DIR)/HadamardProduct.cpp $(SRC_DIR)/HadamardProduct.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

clean:
	rm -f $(PYTHON_DIR)/*.o $(SRC_DIR)/*.o $(PYTHON_DIR)/hadamard_core`python3-config --extension-suffix`
