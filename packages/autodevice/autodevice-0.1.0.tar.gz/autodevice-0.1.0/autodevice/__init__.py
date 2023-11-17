
__module_name__ = "__init__.py"
__doc__ = """Top-level __init__ for the autodevice package."""
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["mvinyard.ai@gmail.com"])


from .__version__ import __version__



# -- import API module(s): ----------------------------------------------------
from ._autodevice import AutoDevice

from ._available_devices import AvailableDevices as _AvailableDevices