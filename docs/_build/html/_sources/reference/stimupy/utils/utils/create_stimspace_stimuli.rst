
create_stimspace_stimuli
========================



.. py:function:: stimupy.utils.utils.create_stimspace_stimuli(stimulus_function, permutations_dicts, title_params=None)


   Generate stimuli for all parameter combinations in a stimspace.

   Given a callable `stimulus_function` and a list of parameter combinations
   (as produced by [`utils.permutate_params`](utils.permutate_params)),
   this function generates and returns all corresponding stimulus images.
   Optionally, specific parameters can be included in the stimulus names
   for easier identification in plots or debugging.

   :param stimulus_function: A stimulus-generating function that accepts keyword arguments matching
                             the keys in `permutations_dicts`.
   :type stimulus_function: callable
   :param permutations_dicts: A list of parameter dictionaries, each representing one combination of
                              stimulus parameters to be passed to `stimulus_function`.
                              Typically obtained from [`utils.permutate_params`](utils.permutate_params).
   :type permutations_dicts: list of dict
   :param title_params: Name(s) of parameters to display in the dictionary keys for the output.
                        - If a string, it is interpreted as a single parameter name.
                        - If a list, multiple parameter values will be included in the name.
                        - If `None` (default), keys will be simple integer indices.
   :type title_params: str or list of str, optional

   :returns: Dictionary mapping descriptive keys to the generated stimulus outputs.
             Keys are either:
             - String representations of selected `title_params` and their values.
             - Sequential integer strings if `title_params` is `None`.
   :rtype: dict

   :raises ValueError: If `stimulus_function` is not callable.

   .. rubric:: Examples

   >>> from stimupy.stimuli.gabors import gabor
   >>> from stimupy.utils import permutate_params, create_stimspace_stimuli
   >>> params = {
   ...     "visual_size": [1.],
   ...     "ppd": [50],
   ...     "sigma": [0.1, 0.2],
   ...     "frequency": [2, 4]
   ... }
   >>> permuted = permutate_params(params)
   >>> stimspace = create_stimspace_stimuli(
   ...     stimulus_function=gabor,
   ...     permutations_dicts=permuted,
   ...     title_params=["sigma", "frequency"]
   ... )
   >>> list(stimspace.keys())
   ['sigma=0.1 frequency=2 ', 'sigma=0.1 frequency=4 ',
    'sigma=0.2 frequency=2 ', 'sigma=0.2 frequency=4 ']




 