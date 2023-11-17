
__module_name__ = "_available_devices.py"
__author__ = "Michael E. Vinyard"
__email__ = "mvinyard.ai@gmail.com"


# -- Import packages: ---------------------------------------------------------
import torch


# -- set typing: --------------------------------------------------------------
from typing import Dict, List


# -- operational class: -------------------------------------------------------
class AvailableDevices(object):
    def __init__(self, *args, **kwargs):
        """Container for available devices"""

    @property
    def cuda(self) -> bool:
        """ """
        return torch.cuda.is_available()

    @property
    def mps(self) -> bool:
        """ """
        return torch.backends.mps.is_available()

    @property
    def cpu(self) -> bool:
        """ """
        return True

    @property
    def _DEVICE_ATTRIBUTES(self) -> List:
        """ """
        return [attr for attr in self.__dir__() if not attr.startswith("_")]

    def _forward(self) -> Dict:
        """ """
        return {attr: getattr(self, attr) for attr in self._DEVICE_ATTRIBUTES}
    
    def __call__(self) -> Dict:
        """
        Returns:
            available_devices (Dict): Description.
        """
        return self._forward()

    @property
    def _REPR_STRING(self) -> str:
        """ """
        repr_str = "Available devices:"
        for k, v in self._forward().items():
            repr_str += "\n  {:<4} : {}".format(k, bool(v))
        return repr_str

    def __repr__(self) -> str:
        """
        Returns:
            repr (str): Description.
        """
        return self._REPR_STRING
