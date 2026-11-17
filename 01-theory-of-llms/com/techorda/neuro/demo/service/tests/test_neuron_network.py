import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from neuron_network import NeuronNetwork


def test_predict_returns_finite_output():
    network = NeuronNetwork()
    output = network.predict([0.1, -0.5, 0.8])
    assert len(output) == 1
    assert math.isfinite(output[0])


def test_finds_maximum_value():
    network = NeuronNetwork()
    network.train(epochs=1000, learning_rate=0.05)
    
    # max([0.2, 0.5, -0.3]) should be close to 0.5
    pred = network.predict([0.2, 0.5, -0.3])[0]
    assert abs(pred - 0.5) < 0.2


def test_evaluate_mae():
    network = NeuronNetwork()
    network.train(epochs=1000, learning_rate=0.05)
    mae = network.evaluate(network.test_inputs, network.test_outputs)
    assert mae < 0.2
