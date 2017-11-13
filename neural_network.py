class NeuralNetwork:
    
    def __init__(self, layers_num_nodes, random_weights=True):
        '''
        layers_size: array containing num nodes for each layer. Pos 0 is input, Pos last is outut, hidden layers in middle
        random_weights: boolean, whether weights should be randomized
        '''
        self.input_num_nodes = layers_num_nodes[0]
        self.output_num_nodes = layers_num_nodes[-1]
        self.num_hidden_layers = len(layers_num_nodes)-2
        self.layers_num_nodes = layers_num_nodes
        self.weights = []
        self.bias = []
        self.init_weights(random_weights)
        
    def __str__(self):
        return str({'w':self.weights, 'b':self.bias})
        
    def __repr__(self):
        return str(self.weights)
    
    def init_weights(self, random_weights):
        import numpy as np
        prev_layer_num_nodes = self.input_num_nodes
        
        if not random_weights:
            for i, num_hidden_nodes in enumerate(self.layers_num_nodes[1:]):
                self.weights.append(np.zeros(shape=(num_hidden_nodes, prev_layer_num_nodes)))
                self.bias.append(np.zeros(shape=(num_hidden_nodes, 1)))
                
                prev_layer_num_nodes = num_hidden_nodes
        
        else:
            for i, num_hidden_nodes in enumerate(self.layers_num_nodes[1:]):
                self.weights.append((np.random.rand(num_hidden_nodes, prev_layer_num_nodes)-0.5)*25)
                self.bias.append((np.random.rand(num_hidden_nodes, 1)-0.5)*25)
                
                prev_layer_num_nodes = num_hidden_nodes
 
    def predict(self, inp):
        import numpy as np
        import math
        if inp.shape != (self.input_num_nodes, 1):
            raise ValueError('Input size error. Expected {}, got {}'.format((self.input_num_nodes, 1), inp.shape))
        
        prev_layer = inp
        #No need for activation function for the output layer. We're not doing backprop, just select the node with the highest value.
        for layer, weight in enumerate(self.weights):
            prev_layer = np.dot(weight, prev_layer) + self.bias[layer]
            
            relu = np.vectorize(lambda x: max(x, 0))
            if layer != len(self.weights)-1:
                prev_layer = relu(prev_layer)
        return prev_layer
        
