from sklearn.linear_model import LinearRegression
import joblib
from init import safe_path_to

def main():
    # Train model
    X = [[1], [2], [3], [4]]
    y = [2, 4, 6, 8]
    model = LinearRegression()
    model.fit(X, y)

    # Save the trained classifier to a file
    joblib.dump(model, safe_path_to('build/models/trained_classifier.pkl'))
