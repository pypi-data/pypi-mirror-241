
# -- import packages: ---------------------------------------------------------
import torch


# -- import local dependencies: -----------------------------------------------
from .core import BaseODE


# -- import standard libraries and define types: ------------------------------
from typing import Union, List


# -- Main operational class: --------------------------------------------------
class PotentialODE(BaseODE):
    DIFFEQ_TYPE = "ODE"
    
    """PotentialODE"""
    
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
        brownian_dim: int = 1,
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
            noise_type: str = "general"
            brownian_dim: int = 1
            
        Returns:
            None
        """
        
        super().__init__()
        
        mu_potential = True

        self.__config__(locals())

    def _potential(self, y: torch.Tensor) -> torch.Tensor:
        """ """
        return self.mu(y)

    def _gradient(self, ψ: torch.Tensor, y:  torch.Tensor) -> torch.Tensor:
        """use-case: output is directly psi (from a potential network)"""
        return torch.autograd.grad(ψ, y, torch.ones_like(ψ), create_graph=True)[0]

    def drift(self, y: torch.Tensor) -> torch.Tensor:
        """ """
        y = y.requires_grad_()
        ψ = self._potential(y)
        return self._gradient(ψ, y)
