
# -- import packages: ---------------------------------------------------------
import torch


# -- import local dependencies: ----------------------------------------------
from . import core


# -- import standard libraries and define types: -----------------------------
from typing import Union, List


# -- Main operational class: -------------------------------------------------
class LatentPotentialODE(core.BaseLatentODE):
    DIFFEQ_TYPE = "ODE"

    def __init__(
        self,
        state_size: int,
        coef_diff: float = 0,
        dt: float = 0.1,
        mu_hidden: Union[List[int], int] = [512, 512],
        mu_activation: Union[str, List[str]] = "LeakyReLU",
        mu_dropout: Union[float, List[float]] = 0.,
        mu_bias: Union[bool, List[bool]] = True,
        mu_output_bias: bool = True,
        mu_n_augment: int = 0,
        sde_type: str = "ito",
        noise_type: str = "general",
        brownian_dim: int = 1,
    ):
        """Instantiate a LatentPotentialODE
        
        Args:
            state_size (int): Description.
            
            coef_diff (float): Description. ``**Default**: 0``
            
            dt (float): Description. ``**Default**: 0.1``
            
            mu_hidden: Union[List[int], int] = [512, 512].
            
            mu_activation: Union[str, List[str]] = "LeakyReLU".
            
            mu_dropout: Union[float, List[float]] = 0..
            
            mu_bias: Union[bool, List[bool]] = True.
            
            mu_output_bias: bool = True.
            
            mu_n_augment: int = 0.
            
            sde_type: str = "ito".
            
            noise_type: str = "general".
            
            brownian_dim: int = 1.
            
        Returns:
            None
            
        Notes:
            By declaring ``mu_potential = False``, we explicitly state that
            we are not are not learning a potential function by default.
        """
        
        super().__init__()

        mu_potential = False
        self.__config__(locals())
        self.potential = core.Potential(state_size = self._state_size)

    def drift(self, y: torch.Tensor) -> torch.Tensor:
        """
        Args:
            y (torch.Tensor): input state.
            
        Returns:
            y_hat_f (torch.Tensor): drift(input).
        """
        return self.mu(y)

    def prior_drift(self, y: torch.Tensor) -> torch.Tensor:
        """
        Args:
            y (torch.Tensor): input state.
            
        Returns:
            y_hat_h (torch.Tensor): prior_drift(input).
        """
        return self.potential.potential_gradient(y)
