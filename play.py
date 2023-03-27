import numpy as np
import sklearn.datasets
import sklearn.preprocessing

# Load the MNIST dataset
digits = sklearn.datasets.load_digits()
X_raw = digits.data.astype(float)
y_raw = digits.target.reshape(-1, 1)

# Scale and split the data
scaler = sklearn.preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X_raw)
y_one_hot = sklearn.preprocessing.OneHotEncoder(categories='auto').fit_transform(y_raw).toarray()
train_size = int(0.8 * len(X_scaled))
X_train, X_test = X_scaled[:train_size], X_scaled[train_size:]
y_train, y_test = y_one_hot[:train_size], y_one_hot[train_size:]

# Define the neural network model
class NeuralNetwork():
    def __init__(self):
        self.input_size = 64
        self.hidden_size = 32
        self.output_size = 10
        self.lr = 0.01
        self.W1 = np.random.randn(self.input_size, self.hidden_size) / np.sqrt(self.input_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size) / np.sqrt(self.hidden_size)
        self.b2 = np.zeros((1, self.output_size))

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = np.tanh(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.probabilities = np.exp(self.z2) / np.sum(np.exp(self.z2), axis=1, keepdims=True)
        return self.probabilities

    def backward(self, X, y):
        delta3 = self.probabilities - y
        self.dW2 = np.dot(self.a1.T, delta3)
        self.db2 = np.sum(delta3, axis=0)
        delta2 = np.dot(delta3, self.W2.T) * (1 - np.power(self.a1, 2))
        self.dW1 = np.dot(X.T, delta2)
        self.db1 = np.sum(delta2, axis=0)

    def update(self):
        self.W1 -= self.lr * self.dW1
        self.b1 -= self.lr * self.db1
        self.W2 -= self.lr * self.dW2
        self.b2 -= self.lr * self.db2

    def fit(self, X, y, epochs=30000):
        for i in range(epochs):
            probabilities = self.forward(X)
            self.backward(X, y)
            self.update()

            if i % 1000 == 0:
                cost = -np.sum(y * np.log(probabilities)) / len(X)
                print("Epoch {}: loss = {}".format(i, cost))

    def predict(self, X):
        return np.argmax(self.forward(X), axis=1)

# Train the neural network and evaluate it on the test set
np.random.seed(0)
nn = NeuralNetwork()
nn.fit(X_train, y_train)
predictions = nn.predict(X_test)
accuracy = np.mean(predictions == np.argmax(y_test, axis=1))
print("Test accuracy: {}".format(accuracy))
