import numpy as np

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s

def tanh(z):
    s = (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))
    return s

def relu(z):
    s = np.maximum(0, z)
    return s

def lrelu(z, alpha=0.01):
    s = np.maximum(alpha * z, z)
    return s

def softmax(vector):
    e = np.exp(vector)
    s = e / e.sum()
    return s
