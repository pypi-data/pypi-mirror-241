import torch
import pandas as pd
import numpy as np
from typing import Union, Iterable, Optional
from ._conversions import tensor_to_floats
from ._conversions import named_to_tensor, tensor_to_dataframe
from ._neural_network import NeuralNetwork
from ._loss_functions import MSE
from .layers import Normalizer, Dense


class DenseRegressor(NeuralNetwork):
    """
    DenseRegressor is an implementation of a fully connected NeuralNetwork
    for tabular regression.

    The data type of input 'x' and target 'y' are both a pd.DataFrame, 
    or a dictionary, or a np.ndarray of shape (n_observations, n_classes)

    The prediction output is a np.ndarray of shape (n_observations,)
    if there is a single target, and a pd.DataFrame if there are several
    """

    def __init__(self, inputs: Iterable[str],
                 target: Union[str, Iterable[str]],
                 hidden_layers: Iterable[int],
                 activation: str = "relu",
                 normalize: bool = True,
                 dropout: Optional[float] = None):
        """
        Parameters
        ----------
        inputs : Iterable of str
            the column names of the input variables in a dataframe
        target : str or Iterable of str
            the column name(s) of the variable(s) to predict
        hidden_layers : iterable of int
            number of features of each hidden layer of the multi layers perceptron
        activation : str or Callable
            the activation function
        normalize : bool
            whether or not to normalize inputs, hidden layers and target
        dropout : float or None
            the dropout after each hidden layer if provided
        """
        super().__init__()
        self.inputs = tuple(inputs)
        self.target = target if isinstance(target, str) else tuple(target)
        self.layers = torch.nn.ModuleList()
        in_features = len(inputs)
        self.input_normalizer = Normalizer(1, in_features)
        for out_features in hidden_layers:
            self.layers.append(Dense(in_features, out_features, normalize=normalize,
                                     activation=activation, dropout=dropout))
            in_features = out_features
        out_features = 1 if isinstance(target, str) else len(self.target)
        self.output = torch.nn.Linear(in_features, out_features)
        self.target_normalizer = Normalizer(1, out_features)

    def forward(self, X: torch.Tensor):
        X = X.to(self.device)
        X = self.input_normalizer(X)
        for layer in self.layers:
            X = layer(X)
        return self.output(X)

    def loss(self, x: torch.Tensor, y_target: torch.Tensor,
             weights: Optional[torch.Tensor] = None):
        y_pred = self(x)
        y_target = self.target_normalizer(y_target)
        return MSE(y_pred, y_target, weights)

    @property
    def device(self) -> torch.device:
        return self.output.weight.device

    def _x_to_tensor(self, x: Union[pd.DataFrame, dict, Iterable],
                     device: Optional[torch.device] = None):
        return named_to_tensor(x, list(self.inputs), device=device)

    def _y_to_tensor(self, y: Union[pd.DataFrame, dict, Iterable],
                     device: Optional[torch.device] = None) -> torch.Tensor:
        target = [self.target] if isinstance(self.target, str) else list(self.target)
        return named_to_tensor(y, target, device=device)

    def _tensor_to_y(self, tensor: torch.Tensor) -> np.ndarray:
        if self.target_normalizer is not None:
            tensor = self.target_normalizer.unscale(tensor)
        if isinstance(self.target, str):
            return tensor_to_floats(tensor).reshape(-1)
        else:
            return tensor_to_dataframe(tensor, self.target)
