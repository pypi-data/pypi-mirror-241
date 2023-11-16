
import ABCParse
import torch_nets


class DiffEqConfig(ABCParse.ABCParse):
    def __init__(
        self,
        state_size,
        mu_hidden=[2000, 2000],
        sigma_hidden=[400, 400],
        brownian_dim=1,
        mu_activation=["LeakyReLU"],
        sigma_activation=["LeakyReLU"],
        mu_dropout=[0.2],
        sigma_dropout=[0.2],
        mu_n_augment=0,
        sigma_n_augment=0,
        mu_bias=[True],
        sigma_bias=[True],
        mu_potential=False,
        sigma_potential=False,
        mu_output_bias=False,
        sigma_output_bias=False,
    ):
        self.__parse__(locals(), public = [None])

    @property
    def mu_in_features(self):
        return self._state_size

    @property
    def sigma_in_features(self):
        return self._state_size

    @property
    def mu_out_features(self):
        if self._mu_potential:
            return 1
        return self._state_size

    @property
    def sigma_out_features(self):
        if self._sigma_potential:
            return 1
        return self._state_size * self._brownian_dim

    @property
    def mu_output_bias(self):
        if self._mu_potential:
            return False
        return self._mu_output_bias

    @property
    def sigma_output_bias(self):
        if self._sigma_potential:
            return False
        return self._sigma_output_bias

    @property
    def mu_net_cls(self):
        if self._mu_n_augment:
            self._mu_kwargs = {"n_augment": self._mu_n_augment}
            return torch_nets.AugmentedTorchNet
        self._mu_kwargs = {}
        return torch_nets.TorchNet

    @property
    def sigma_net_cls(self):
        if self._sigma_n_augment:
            self._sigma_kwargs = {"n_augment": self._sigma_n_augment}
            return torch_nets.AugmentedTorchNet
        self._sigma_kwargs = {}
        return torch_nets.TorchNet

    @property
    def mu(self):
        return self.mu_net_cls(
            in_features=self.mu_in_features,
            out_features=self.mu_out_features,
            hidden=self._mu_hidden,
            activation=self._mu_activation,
            dropout=self._mu_dropout,
            bias=self._mu_bias,
            output_bias=self.mu_output_bias,
            **self._mu_kwargs,
        )

    @property
    def sigma(self):
        return self.sigma_net_cls(
            in_features=self.sigma_in_features,
            out_features=self.sigma_out_features,
            hidden=self._sigma_hidden,
            activation=self._sigma_activation,
            dropout=self._sigma_dropout,
            bias=self._sigma_bias,
            output_bias=self.sigma_output_bias,
            **self._sigma_kwargs
        )
    def __call__(self):
        return self.mu, self.sigma
