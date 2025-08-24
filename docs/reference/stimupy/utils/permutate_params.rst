
permutate_params
================



.. py:function:: stimupy.utils.permutate_params(params)


   Generate all possible parameter combinations for a stimulus function.

   Takes a dictionary of stimulus parameters, where each parameter value is
   provided as a sequence (e.g., list, tuple). Returns a list of dictionaries,
   each representing one unique combination of parameter values. This is
   useful for systematically exploring a stimulus parameter space
   (e.g., in 1D, 2D, or higher dimensions).

   :param params: Dictionary mapping parameter names (str) to sequences of possible values.
                  Each sequence will be iterated over to form combinations.
                  Example::
                      {
                          "frequency": [1, 2, 4],
                          "sigma": [0.05, 0.1]
                      }
   :type params: dict

   :returns: A list where each element is a dictionary mapping parameter names to
             specific values, corresponding to one combination from the Cartesian
             product of all provided sequences.
             Example output::
                 [
                     {"frequency": 1, "sigma": 0.05},
                     {"frequency": 1, "sigma": 0.1},
                     {"frequency": 2, "sigma": 0.05},
                     ...
                 ]
   :rtype: list of dict

   :raises ValueError: If `params` is not a dictionary.




 