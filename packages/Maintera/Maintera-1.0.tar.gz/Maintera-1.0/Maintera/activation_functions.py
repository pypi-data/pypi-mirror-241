# Mentera/activation_function.py

def activation_functions():
    code = """
    import numpy as np

    def sigmoid(z):
        s = 1 / (1 + np.exp(-z))
        return s

    def dsig(s):
        das = (s)*(1-s)
        return das


    def tanh(z):
        s = (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))
        return s

    def dthan(s):
        dat = (1-s**2)
        return dat


    def relu(z):
        s = np.maximum(0, z)
        return s

    def drelu(s):
        dar=(np.int64(s>0))
        return dar


    def lrelu(z, alpha=0.01):
        s = np.maximum(alpha * z, z)
        return s

    def dlrelu(s,alpha=0.01):
        dal=np.where(s >0, 1, alpha)
        return dal

    def softmax(vector):
        e = np.exp(vector)
        s = e / e.sum()
        return s
    """
    print(code)