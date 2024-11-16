FROM python:3.10-slim
LABEL authors="max-z"
RUN apt-get update && apt-get install -y \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pybind11 build pytest

WORKDIR /app

COPY . .

RUN make all

RUN python3 -m build
RUN pip install dist/hadamard-0.1-py3-none-any.whl

RUN python3 -c "import hadamard; print('Hadamard module loaded successfully')"

CMD ["pytest", "tests/"]