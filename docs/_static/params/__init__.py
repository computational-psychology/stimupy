"""
Parameter classes for stimupy interactive demos.

This module contains parameter classes extracted from the interactive demo files.
Each parameter class inherits from param.Parameterized and provides get_stimulus_params()
method to return the parameters in the format expected by stimupy functions.
"""

from . import components
from . import noises
from . import stimuli

__all__ = ["components", "noises", "stimuli"]
