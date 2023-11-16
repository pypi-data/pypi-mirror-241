
# -- import packages: ----------------------------------------------------------
import torch


# -- import local dependencies: ------------------------------------------------
from . import core


# -- import standard libraries and define types: -------------------------------
from typing import Union, List


# -- Main operational class: ---------------------------------------------------
class PotentialSDE(core.BaseSDE):
    """PotentialSDE, subclass of core.BaseSDE"""
    DIFFEQ_TYPE = "SDE"
    def __init__(
        self,
        state_size: int,
        mu_hidden: Union[List[int], int] = [512, 512],
        sigma_hidden: Union[List[int], int] = [32, 32],
        mu_activation: Union[str, List[str]] = "LeakyReLU",
        sigma_activation: Union[str, List[str]] = "LeakyReLU",
        mu_dropout: Union[float, List[float]] = 0.,
        sigma_dropout: Union[float, List[float]] = 0.,
        mu_bias: Union[bool, List[bool]] = True,
        sigma_bias: Union[bool, List[bool]] = True,
        sigma_output_bias: bool = True,
        mu_n_augment: int = 0,
        sigma_n_augment: int = 0,
        sde_type: str = "ito",
        noise_type: str = "general",
        brownian_dim: int = 1,
        coef_drift: float = 1.,
        coef_diffusion: float = 1.,
    ):
        
        """PotentialSDE instantiation from parameters are parsed and passed to the base class config function.
        
        Args:
            state_size (int): Input and output state size of the differential equation.
        
            mu_hidden (Union[List[int], int]): Architecture of the hidden layers of the drift neural network. **Default**: ``[512, 512]``.
        
            sigma_hidden (Union[List[int], int]): Architecture of the hidden layers of the diffusion neural network. **Default**: ``[32, 32]``.
            
            mu_activation (Union[str, List[str]]): Activation function(s) used in each layer of the drift neural network. If ``len(mu_hidden) > len(mu_activation)``, the remaining activation functions are autofilled using the last value passed. **Default**: ``"LeakyReLU"``.
            
            sigma_activation (Union[str, List[str]]): Activation function(s) used in each layer of the diffusion neural network. If ``len(sigma_hidden) > len(sigma_activation)``, the remaining activation functions are autofilled using the last value passed. **Default**: ``"LeakyReLU"``.
            
            mu_dropout (Union[float, List[float]]): Description. **Default**: ``0.``.
            
            sigma_dropout (Union[float, List[float]]): Description. **Default**: ``0.``.
            
            mu_bias (Union[bool, List[bool]]): Description. **Default**: ``True``.
            
            sigma_bias (Union[bool, List[bool]]): Description. **Default**: ``True``.
            
            mu_output_bias (bool): Description. **Default**: ``False``.
            
            sigma_output_bias (bool): Description. **Default**: ``True``.
            
            mu_n_augment (int): Description. **Default**: ``0``.
            
            sigma_n_augment (int): Description. **Default**: ``0``.
            
            sde_type (str): Description. **Default**: ``"ito"``.
            
            noise_type (str): Description. **Default**: ``"general"``.
            
            brownian_dim (int): Number of diffusion dimensions. **Default**: ``1``.
            
            coef_drift (float): Multiplier of drift network output. **Default**: ``1.``.
            
            coef_diffusion (float): Multiplier of diffusion network output. **Default**: ``1.``.
        
        Returns:
            None
        
        Notes:
            NeuralSDE: torch.nn.Module
            
        Example:
        
            .. code-block:: python

                import neural_diffeqs
                SDE = neural_diffeqs.PotentialSDE(state_size = 50)
        """
        
        super().__init__()

        mu_potential = True
        self.__config__(locals())
        
    def _potential(self, y: torch.Tensor) -> torch.Tensor:
        
        """ """
        
        y = y.requires_grad_()
        return self.mu(y)

    def _gradient(self, ψ: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        
        """use-case: output is directly psi (from a potential network)"""
        
        return torch.autograd.grad(ψ, y, torch.ones_like(ψ), create_graph=True)[0]

    def drift(self, y: torch.Tensor) -> torch.Tensor:
        
        """ """
        
        y = y.requires_grad_()
        ψ = self._potential(y)
        return self._gradient(ψ, y) * self._coef_drift

    def diffusion(self, y: torch.Tensor) -> torch.Tensor:
        
        """ """
        
        return self.sigma(y).view(y.shape[0], y.shape[1], self._brownian_dim) * self._coef_diffusion
