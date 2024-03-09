import pickle
from sklearn.neighbors import KNeighborsClassifier

# Assuming your model is stored in 'model.pkl'
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

# Save the model with the updated scikit-learn version
with open('knn_model.pkl', 'wb') as file:
    pickle.dump(knn_model, file)
