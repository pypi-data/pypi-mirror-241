"""
Protocol classes from types outside the optimization submodule
"""
#                                                                       Modules
# =============================================================================

from __future__ import annotations

# Standard
from typing import Any, Dict, Optional, Tuple, Type

try:
    from typing import Protocol
except ImportError:  # Python 3.7
    from typing_extensions import Protocol

# Third-party core
import numpy as np

#                                                          Authorship & Credits
# =============================================================================
__author__ = 'Martin van der Schelling (M.P.vanderSchelling@tudelft.nl)'
__credits__ = ['Martin van der Schelling']
__status__ = 'Stable'
# =============================================================================
#
# =============================================================================


class _Data(Protocol):
    ...


class Domain(Protocol):
    """Protocol class for the domain"""

    def get_continuous_parameters(self):
        ...


class ExperimentSample:
    def __init__(self, dict_input: Dict[str, Any],
                 dict_output: Dict[str, Any], jobnumber: int):
        """Single realization of a design of experiments.

        Parameters
        ----------
        dict_input : Dict[str, Any]
            Input parameters of one experiment
        dict_output : Dict[str, Any]
            Output parameters of one experiment
        jobnumber : int
            Index of the experiment
        """
        self._dict_input = dict_input
        self._dict_output = dict_output
        self._jobnumber = jobnumber

    @classmethod
    def from_numpy(cls: Type[ExperimentSample], input_array: np.ndarray,
                   output_value: Optional[float] = None,
                   jobnumber: int = 0) -> ExperimentSample:
        """Create a ExperimentSample object from a numpy array.

        Parameters
        ----------
        input_array : np.ndarray
            input 1D numpy array
            output_value : Optional[float], optional
            objective value, by default None

        jobnumber : int
            jobnumber of the design

        Returns
        -------
        ExperimentSample
            ExperimentSample object
        """
        dict_input = {f"x{i}": val for i, val in enumerate(input_array)}
        if output_value is None:
            dict_output = {}
        else:
            dict_output = {"y": output_value}

        return cls(dict_input=dict_input,
                   dict_output=dict_output, jobnumber=jobnumber)

    def to_numpy(self) -> Tuple[np.ndarray, np.ndarray]:
        """Converts the design to a tuple of numpy arrays.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            A tuple of numpy arrays containing the input and output data.
        """
        return (np.array(list(self._dict_input.values())),
                np.array(list(self._dict_output.values())))

    def __setitem__(self, key: str, value: Any):
        self._dict_output[key] = value

    @property
    def input_data(self) -> Dict[str, Any]:
        """Retrieve the input data of the design as a dictionary.

        Returns
        -------
        Dict[str, Any]
            The input data of the design as a dictionary.
        """
        return self._dict_input

    @property
    def output_data(self) -> Dict[str, Any]:
        """Retrieve the output data of the design as a dictionary.

        Returns
        -------
        Dict[str, Any]
            The output data of the design as a dictionary.
        """
        # Load all the data from the experiment data
        # return {key: self.get(key) for key in self._dict_output.keys()}
        return self._dict_output

    @property
    def jobs(self) -> int:
        return self._jobnumber

    _output_data = output_data
    _input_data = input_data
    _jobs = jobs


class DataGenerator(Protocol):
    def _run(self, experiment_sample: ExperimentSample) -> ExperimentSample:
        ...
