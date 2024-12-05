# inference_cython.pyx
# cython: language_level=3
from libc.stdlib cimport malloc, free
import sys

def predict_cython(double x) -> double:
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
    model = sys.argv[1]
    
    if model == "torch":
        from inference import predict_torch as predict
    elif model == "sklearn":
        from inference import predict_sklearn as predict
    else:
        raise ValueError(f"Model {model} not supported")

    return predict(x)
