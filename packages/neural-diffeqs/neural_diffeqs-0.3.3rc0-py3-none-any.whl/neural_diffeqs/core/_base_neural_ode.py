
import torch
import ABCParse
from abc import abstractmethod

from typing import List

from ._base_neural_diffeq import BaseDiffEq
from ._diffeq_config import DiffEqConfig

class BaseODE(BaseDiffEq):
    DIFFEQ_TYPE = "ODE"

    def __init__(self, *args, **kwargs):
        super().__init__()

        """
        In inherited class, must pass:
            "dt"
            "coef_diff"
        
        Must call self.__config__(locals()) in the __init__
        of the inheriting class.        
        """

    def __config__(self, kwargs, private: List[str] = ["coef_diff", "dt"]):
        """Sets up mu and sigma given params"""

        self.__parse__(kwargs=kwargs, private=private, public = ['noise_type', 'sde_type'])

        self._config_kwargs = ABCParse.function_kwargs(func=DiffEqConfig, kwargs=kwargs)
        configs = DiffEqConfig(**self._config_kwargs)
        self.mu = configs.mu
        
    @property
    def _sqrt_dt(self):
        """Must pass `dt`"""
        return torch.sqrt(torch.Tensor([self._dt]).to(self.device))

    def _sigma(self, y):
        return torch.randn([y.shape[0], y.shape[1], self._brownian_dim], device=self.device)
    
    @property
    def device(self):
        return list(self.parameters())[0].device

    # -- required methods in child classes: ------------------------------------
    @abstractmethod
    def drift(self):
        """Called by self.f and/or self.forward"""
        ...
        
    def forward(self, t: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return self.drift(y)

    def diffusion(
        self, y: torch.Tensor, coef_diff: float = 0., dt: float = 0.1
    ) -> torch.Tensor:
        # keep for compatibility with torchsde.sdeint
        """Called by self.g"""
        return  self._sigma(y) * self._coef_diff * self._sqrt_dt
