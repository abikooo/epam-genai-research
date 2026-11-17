import random
import math
import sys
import os
from typing import List

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from neuron_layer import NeuronLayer
from neuron.neuron import Neuron


class TanhNeuron(Neuron):
    """Neuron using hyperbolic tangent activation."""
    def __init__(self, inputs_count: int):
        super().__init__(inputs_count)

    def activation_function(self, x: float) -> float:
        return math.tanh(x)

    def activate(self, inputs: List[float]) -> float:
        net = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation_function(net)

    def derivative(self, output: float) -> float:
        return 1.0 - (output ** 2)


class LinearNeuron(Neuron):
    """Neuron using linear (identity) activation for regression."""
    def __init__(self, inputs_count: int):
        super().__init__(inputs_count)

    def activation_function(self, x: float) -> float:
        return x

    def activate(self, inputs: List[float]) -> float:
        net = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation_function(net)

    def derivative(self, output: float) -> float:
        return 1.0


class NeuronNetwork:
    """Multi-layer neural network for regression trained with backpropagation and MSE."""

    def __init__(self, hidden_size: int = 8):
        random.seed(1)
        # 3 inputs -> hidden tanh layer -> 1 linear output
        self.layers: List[NeuronLayer] = [
            NeuronLayer([TanhNeuron(3) for _ in range(hidden_size)]),
            NeuronLayer([LinearNeuron(hidden_size)])
        ]

        for layer in self.layers:
            self.initialize_weights(layer)

        self.train_inputs, self.train_outputs = self.generate_data(300, seed=1)
        self.test_inputs, self.test_outputs = self.generate_data(100, seed=2)

    def initialize_weights(self, layer):
        """Initialize layer weights and biases uniformly in [-0.5, 0.5]."""
        for neuron in layer.neurons:
            neuron.weights = [random.uniform(-0.5, 0.5) for _ in neuron.weights]
            neuron.bias = random.uniform(-0.5, 0.5)

    def generate_data(self, count: int, seed: int = 1):
        """Generate random (x1, x2, x3) points labeled with their maximum value."""
        rng = random.Random(seed)
        inputs = []
        outputs = []
        for _ in range(count):
            x1 = rng.uniform(-1.0, 1.0)
            x2 = rng.uniform(-1.0, 1.0)
            x3 = rng.uniform(-1.0, 1.0)
            max_val = max(x1, x2, x3)
            inputs.append([x1, x2, x3])
            outputs.append([max_val])
        return inputs, outputs

    def predict(self, inputs: List[float]) -> List[float]:
        """Run a forward pass on [x1, x2, x3] coordinates."""
        output = inputs
        for layer in self.layers:
            output = layer.activate(output)
        return output

    def evaluate(self, inputs: List[List[float]], outputs: List[List[float]]) -> float:
        """Compute Mean Absolute Error on a dataset."""
        total_error = 0.0
        for x, y in zip(inputs, outputs):
            pred = self.predict(x)[0]
            total_error += abs(pred - y[0])
        return total_error / len(inputs)

    def train(self, training_inputs=None, training_outputs=None, epochs=2000, learning_rate=0.03):
        """Train the network using backpropagation and MSE loss."""
        if training_inputs is None or training_outputs is None:
            training_inputs = self.train_inputs
            training_outputs = self.train_outputs

        for epoch in range(1, epochs + 1):
            total_error = 0.0

            for sample, expected in zip(training_inputs, training_outputs):
                layer_inputs = []
                layer_outputs = []
                current = sample

                for layer in self.layers:
                    layer_inputs.append(current)
                    current = layer.activate(current)
                    layer_outputs.append(current)

                deltas = [[] for _ in self.layers]

                # Output layer error using MSE derivative (expected - predicted)
                output_layer = self.layers[-1]
                predicted = layer_outputs[-1]
                for i, neuron in enumerate(output_layer.neurons):
                    error = expected[i] - predicted[i]
                    total_error += error ** 2
                    deltas[-1].append(error * neuron.derivative(predicted[i]))

                # Backpropagate through hidden layers
                for l in range(len(self.layers) - 2, -1, -1):
                    layer = self.layers[l]
                    next_layer = self.layers[l + 1]
                    outputs = layer_outputs[l]

                    for i, neuron in enumerate(layer.neurons):
                        error = sum(
                            next_layer.neurons[j].weights[i] * deltas[l + 1][j]
                            for j in range(next_layer.size())
                        )
                        deltas[l].append(error * neuron.derivative(outputs[i]))

                # Update weights and biases
                for l, layer in enumerate(self.layers):
                    inputs_to_layer = layer_inputs[l]
                    for i, neuron in enumerate(layer.neurons):
                        delta = deltas[l][i]
                        for w in range(len(neuron.weights)):
                            neuron.weights[w] += learning_rate * delta * inputs_to_layer[w]
                        neuron.bias += learning_rate * delta

            if epoch % 500 == 0:
                mse = total_error / len(training_inputs)
                print(f"Epoch {epoch} - MSE: {mse:.6f}")


if __name__ == "__main__":
    net = NeuronNetwork()
    net.train(net.train_inputs, net.train_outputs, 1500, 0.05)
    mae = net.evaluate(net.test_inputs, net.test_outputs)
    print(f"Final test MAE: {mae:.4f}")
