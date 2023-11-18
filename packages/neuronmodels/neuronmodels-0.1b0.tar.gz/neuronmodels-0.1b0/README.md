# neuronmodels Package

A Python package containing implementations of various neural network components.

## Installation

```bash
pip install neuronmodels


```
# Usage
# Activation Functions
```bash
python
Copy code
import numpy as np
from neuronmodels import sigmoid, tanh, relu, leaky_relu, softmax, der_sigmoid

# Example usage
x = np.array([0.5, -0.2, 0.1])
result_sigmoid = sigmoid(x)
result_tanh = tanh(x)
result_relu = relu(x)
result_leaky_relu = leaky_relu(x)
result_softmax = softmax(x)
result_der_sigmoid = der_sigmoid(x)
```


# MP Neuron Model
```bash
from neuronmodels import MPNeuron

# Example usage
weights = [0.2, -0.5, 1.0]
threshold = 0.5
mp_neuron = MPNeuron(weights, threshold)

inputs = [0.1, -0.3, 0.5]
output = mp_neuron.activate(inputs)
print("MPNeuron Output:", output)
```
# backpropogation network

```bash
from neuronmodels import backpropogation

# Example usage
input_size = 3
hidden_size = 4
output_size = 2
nn = backpropogation(input_size, hidden_size, output_size)

inputs = np.array([[0.1, -0.2, 0.3]])
targets = np.array([[0.4, 0.7]])
learning_rate = 0.01

nn.train(inputs, targets, learning_rate)

```
# Perceptron model
```bash
from neuronmodels import Perceptron

# Example usage
input_size = 3
learning_rate = 0.1
epochs = 100
perceptron = Perceptron(input_size, learning_rate, epochs)

training_inputs = np.array([[0.1, -0.2, 0.3], [0.4, 0.5, -0.6]])
labels = np.array([1, 0])

perceptron.train(training_inputs, labels)
```
