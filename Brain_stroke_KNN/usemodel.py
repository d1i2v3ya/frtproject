import pickle
from sklearn.neighbors import KNeighborsClassifier

# Function to load the pre-trained model
def load_model(file_path='Knn_model.pkl'):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model
    with open('model.pkl', 'rb') as file:
        knn_model = pickle.load(file)
    with open('model.pkl', 'wb') as file:pickle.dump(knn_model, file)

# Example of using the loaded model
if __name__ == "__main__":
    # Load the pre-trained KNeighborsClassifier
    knn_model = load_model()

    # Now you can use 'knn_model' for predictions or other tasks
    # For example, you might use it to predict on new data
    # new_data = ...  # Your new data
    # predictions = knn_model.predict(new_data)

    # You can also integrate this with your Streamlit app or other applications
    # ...

# If you run this script directly, it will load the model and perform some example tasks
# If you import this script as a module in another script, the code inside 'if __name__ == "__main__":' won't run
