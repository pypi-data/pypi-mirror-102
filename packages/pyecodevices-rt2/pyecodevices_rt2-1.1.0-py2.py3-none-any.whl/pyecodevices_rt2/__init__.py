"""Get information from GCE Ecodevices RT2."""

from .ecodevices_rt2 import EcoDevicesRT2
from .abstractswitch import AbstractSwitch
from .abstractsensor import AbstractSensor
from .enocean import EnOceanSwitch, EnOceanSensor
from .toroid import Toroid
from .relay import Relay
from .virtualoutput import VirtualOutput
from .digitalinput import DigitalInput
from .xthl import XTHL
from .x4fp import X4FP
from .counter import Counter
from .supplierindex import SupplierIndex
from .post import Post

__author__ = """Pierre COURBIN"""
__email__ = 'pierre.courbin@gmail.com'
__version__ = '1.1.0'

__all__ = [
    "EcoDevicesRT2",
    "AbstractSwitch",
    "AbstractSensor",
    "EnOceanSwitch",
    "EnOceanSensor",
    "Toroid",
    "Relay",
    "VirtualOutput",
    "DigitalInput",
    "XTHL",
    "X4FP",
    "Counter",
    "SupplierIndex",
    "Post"
]
