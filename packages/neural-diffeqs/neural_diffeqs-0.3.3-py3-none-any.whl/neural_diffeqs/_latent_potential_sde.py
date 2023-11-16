
# -- import packages: ----------------------------------------------------------
import torch


# -- import local dependencies: ------------------------------------------------
from . import core


# -- import standard libraries and define types: -------------------------------
from typing import Union, List


# -- Main operational class: ---------------------------------------------------
class LatentPotentialSDE(core.BaseLatentSDE):
    DIFFEQ_TYPE = "SDE"

    def __init__(
        self,
        state_size: int,
        mu_hidden: Union[List[int], int] = [2000, 2000],
        sigma_hidden: Union[List[int], int] = [400, 400],
        mu_activation: Union[str, List[str]] = "LeakyReLU",
        sigma_activation: Union[str, List[str]] = "LeakyReLU",
        mu_dropout: Union[float, List[float]] = 0.2,
        sigma_dropout: Union[float, List[float]] = 0.2,
        mu_bias: Union[bool, List[bool]] = True,
        sigma_bias: Union[bool, List[bool]] = True,
        mu_output_bias: bool = False,
        sigma_output_bias: bool = True,
        mu_n_augment: int = 0,
        sigma_n_augment: int = 0,
        sde_type: str = "ito",
        noise_type: str = "general",
        brownian_dim: int = 1,
        coef_drift: float = 1.,
        coef_diffusion: float = 1.,
        coef_prior_drift: float = 1.,
    ):
        super().__init__()

        # explicitly state that we are not learning a potential function by default
        mu_potential = False
        self.__config__(locals())
        self.potential = core.Potential(state_size=self._state_size)

    def drift(self, y) -> torch.Tensor:
        """ """
        return self.mu(y) * self._coef_drift

    def prior_drift(self, y) -> torch.Tensor:
        """ """
        return self.potential.potential_gradient(y) * self._coef_prior_drift

    def diffusion(self, y) -> torch.Tensor:
        """ """
        return self.sigma(y).view(y.shape[0], y.shape[1], self._brownian_dim) * self._coef_diffusion
