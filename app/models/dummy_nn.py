# torch_model.py
import torch
import torch.nn as nn
from init import safe_path_to

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # Simple linear layer

    def forward(self, x):
        return self.linear(x)

def main():
    # Save a pre-trained model
    model = SimpleModel()
    # Fake training
    with torch.no_grad():
        model.linear.weight.fill_(2.0)  # y = 2x
        model.linear.bias.fill_(0.0)

    # Save the model
    torch.save(model.state_dict(), safe_path_to("build/models/simple_model.pth"))
