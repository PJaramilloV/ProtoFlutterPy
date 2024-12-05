import torch
import joblib
import numpy as np
from init import safe_path_to
from models.dummy_nn import SimpleModel
from models.dummy_lr import LinearRegression
from ctypes import cdll, c_double, POINTER

# Load model weights
model_nn = SimpleModel()
model_nn.load_state_dict(torch.load(safe_path_to("build/models/simple_model.pth")))
model_nn.eval()

# Load the shared library
model_lr:LinearRegression = joblib.load(safe_path_to("build/models/trained_classifier.pkl"))


# Expose a prediction function
def predict_torch(x: float) -> float:
    with torch.no_grad():
        input_tensor = torch.tensor([[x]], dtype=torch.float32)
        output = model_nn(input_tensor)
    return output.item()

def predict_sklearn(x: float) -> float:
    return model_lr.predict([[x]])[0]