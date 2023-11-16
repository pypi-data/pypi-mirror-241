
# -- import packages: ---------------------------------------------------------
import torch


# -- import local dependencies: -----------------------------------------------
from .core._base_neural_ode import BaseODE


# -- import standard libraries and define types: ------------------------------
from typing import Union, List


# -- Main operational class: --------------------------------------------------
class NeuralODE(BaseODE):
    DIFFEQ_TYPE = "ODE"
    
    """NeuralODE"""
    
    def __init__(
        self,
        state_size: int,
        dt: float = 0.1,
        coef_diff: float = 0,
        mu_hidden: Union[List[int], int] = [512, 512],
        mu_activation: Union[str, List[str]] = "LeakyReLU",
        mu_dropout: Union[float, List[float]] = 0.,
        mu_bias: bool = True,
        mu_output_bias: bool = True,
        mu_n_augment: int = 0,
        sde_type: str = "ito",
        noise_type: str = "general",
    ) -> None:
        """
        Args:
            state_size: int
            
            dt: float = 0.1
            
            coef_diff: float = 0
            
            mu_hidden: Union[List[int], int] = [512, 512]
            
            mu_activation: Union[str, List[str]] = "LeakyReLU"
            
            mu_dropout: Union[float, List[float]] = 0.
            
            mu_bias: bool = True
            
            mu_output_bias: bool = True
            
            mu_n_augment: int = 0
            
            sde_type: str = "ito"
            
            noise_type (str): Description. **Default**: ``"general"``.
            
        Returns:
            None
        """

        # -- auto: we are not using the diffusion: ----------------------------

        sigma_hidden = []
        sigma_output_bias = False
        brownian_dim = 1

        super().__init__()

        self.__config__(locals())

    def drift(self, y: torch.Tensor) -> torch.Tensor:
        """ """
        return self.mu(y)

    def forward(self, t, y: torch.Tensor) -> torch.Tensor:
        """ """
        return self.mu(y)
