
__module_name__ = "_autodevice.py"
__author__ = "Michael E. Vinyard"
__email__ = "mvinyard.ai@gmail.com"


# -- import packages: ---------------------------------------------------------
import ABCParse
import torch


# -- import local dependencies: -----------------------------------------------
from ._available_devices import AvailableDevices


# -- set typing: --------------------------------------------------------------
from typing import Optional, Union


# -- operational class: -------------------------------------------------------
class _AutoDevice(ABCParse.ABCParse):
    def __init__(
        self,
        use_cpu: Optional[bool] = False,
        idx: Optional[int] = None,
        *args,
        **kwargs,
    ) -> None:
        """Operational class to mediate device-handling.

        Args:
            use_cpu (Optional[bool]): Description. Default = False.

            idx (Optional[Union[int, None]]): Description. Default = None.

        Returns:
            None, class is instantiated.
        """

        self.__parse__(locals())

        self.availability = AvailableDevices()

    @property
    def use_cpu(self):
        """Flag meant to override auto-gpu assignment"""
        # -- if cpu is a kwarg passed as: {"cpu": True}
        if "cpu" in self._kwargs and self._kwargs["cpu"]:
            self._use_cpu = True
        return self._use_cpu

    @property
    def gpu_idx(self):
        """ """
        if self.availability.cuda:
            if self._idx is None:
                self._idx = torch.cuda.current_device()
            return self._idx
        return None

    @property
    def device(self) -> torch.device:
        """determined torch device.
        Returns:
            device (torch.device): assigned device.
        """

        if self.use_cpu:
            return torch.device("cpu")

        if self.availability.mps:
            return torch.device("mps")

        if self.availability.cuda:
            return torch.device(f"cuda:{self.gpu_idx}")

        return torch.device("cpu")


# -- API-facing function: -----------------------------------------------------
def AutoDevice(
    use_cpu: Optional[bool] = False,
    idx: Optional[Union[int, None]] = None,
    *args,
    **kwargs,
) -> torch.device:
    """API-facing function to mediate device-handling.

    Args:
        use_cpu (Optional[bool]): Description. Default = False.

        idx (Optional[Union[int, None]]): Description. Default = None.

    Returns:
        device (torch.device): assigned device.
    """

    auto_device = _AutoDevice(use_cpu=use_cpu, idx=idx, *args, **kwargs)
    return auto_device.device


