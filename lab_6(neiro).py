import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class SimpleNeuralNetwork:
    def __init__(self, input_size, output_size):
        self.weights = 2 * np.random.random((input_size, output_size)) - 1

    def train(self, training_inputs, training_outputs, iterations):
        for iteration in range(iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * sigmoid_derivative(output))
            self.weights += adjustments

    def think(self, inputs):
        return sigmoid(np.dot(inputs, self.weights))

if __name__ == "__main__":
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    neural_network = SimpleNeuralNetwork(3, 1)

    print("Случайные начальные веса:")
    print(neural_network.weights)

    print(training_inputs)
    print(training_outputs)

    neural_network.train(training_inputs, training_outputs, 10000)

    print("Веса после обучения:")
    print(neural_network.weights)

    print("Результат для нового входа [1, 0, 0]:")
    print(neural_network.think(np.array([1, 0, 0])))
