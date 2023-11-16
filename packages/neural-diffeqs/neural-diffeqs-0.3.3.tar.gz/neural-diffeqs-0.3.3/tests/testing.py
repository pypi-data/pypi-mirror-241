import os
import torch


def load_install_torchsde():
    """Try importing torchsde. If not installed, it will be installed and imported."""
    try:
        import torchsde
    except:
        os.system("pip install torchsde")
        import torchsde

    return torchsde


def load_install_torchdiffeq():
    """Try importing torchdiffeq. If not installed, it will be installed and imported."""
    try:
        import torchdiffeq
    except:
        os.system("pip install torchdiffeq")
        import torchdiffeq

    return torchdiffeq


def test_odeint(
    ODE, y0=torch.randn([200, 50]), t=torch.Tensor([0, 0.001, 0.002]), **kwargs
):
    torchdiffeq = load_install_torchdiffeq()

    """Generate some random data and test the ODE as it's passed through torchdiffeq.odeint."""
    return torchdiffeq.odeint(ODE, y0, t, **kwargs)


def test_sdeint(
    SDE, y0=torch.randn([200, 50]), t=torch.Tensor([0, 0.5, 1.0]), **kwargs
):
    torchsde = load_install_torchsde()
    """Generate some random data and test the ODE as it's passed through torchsde.sdeint."""
    return torchsde.sdeint(SDE, y0, t, dt=0.1, **kwargs)