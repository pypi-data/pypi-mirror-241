import numpy as np
def sigmoid(x): return 1 / (1 + np. exp(-x))
def tanh(x): return np. tanh(x)
def relu(x): return np. maximum(0, x)
def leaky_relu(x, alpha=0.01): return np. maximum(alpha * x, x)
def softmax(x): exp_x = np. exp(x)
def der_sigmoid(x): return sigmoid(x) * (1- sigmoid(x))



class MPNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        # Ensure the number of weights matches the number of inputs
        if len(self.weights) != len(inputs):
            raise ValueError("Number of weights must match number of inputs")

        # Calculate the weighted sum
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))

        # Activate the neuron (output 1) if the weighted sum exceeds the threshold, else output 0
        output = 1 if weighted_sum >= self.threshold else 0

        return output

class backpropogation:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize the weights with random values
        self.weights_input_hidden = np.random.uniform(-1, 1, size=(input_size, hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, size=(hidden_size, output_size))

    def train(self, inputs, targets, learning_rate):
        # Forward propagation
        hidden_inputs = np.dot(inputs, self.weights_input_hidden)
        hidden_outputs = sigmoid(hidden_inputs)

        output_inputs = np.dot(hidden_outputs, self.weights_hidden_output)
        output_outputs = sigmoid(output_inputs)

        # Backpropagation
        output_error = targets - output_outputs
        output_delta = output_error * der_sigmoid(output_outputs)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * der_sigmoid(hidden_outputs)

               # Update the weights
        self.weights_hidden_output += np.outer(hidden_outputs, output_delta) * learning_rate
        self.weights_input_hidden += np.outer(inputs, hidden_delta) * learning_rate


    def predict(self, inputs):
        hidden_inputs = np.dot(inputs, self.weights_input_hidden)
        hidden_outputs = sigmoid(hidden_inputs)

        output_inputs = np.dot(hidden_outputs, self.weights_hidden_output)
        output_outputs = sigmoid(output_inputs)
        #print(output_outputs)
        return np.argmax(output_outputs)


#perceptron model

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activate(self, inputs):
        # Calculate the weighted sum
        weighted_sum = np.dot(self.weights, inputs) + self.bias

        # Apply the step function as the activation function
        return 1 if weighted_sum >= 0 else 0

    def train(self, training_inputs, labels):
        for epoch in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.activate(inputs)
                error = label - prediction

                # Update weights and bias
                self.weights += self.learning_rate * error * inputs
                self.bias += self.learning_rate * error

