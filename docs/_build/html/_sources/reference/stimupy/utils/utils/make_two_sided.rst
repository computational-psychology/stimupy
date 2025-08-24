
make_two_sided
==============



.. py:function:: stimupy.utils.utils.make_two_sided(func, two_sided_params)


   Create two-sided version of a stimulus function

   Where (some) parameters can be specified separately for each side.
   These parameters should then be specified as a 2-Sequence (2-ple, list of len=2),
   where entry [0] is the parameter value for left side, and [1] for right side.
   This means that if the kwarg takes a Sequence itself, e.g., `intensities`,
   then the two-sided specification must be, e.g.,
   ((int_left_0, int_left_1), (int_right_0, int_right_1))

   Will be left- and right-sided.


   :param func: stimulus function to double
   :type func: function
   :param two_sided_params: names of parameters (kwargs) of func
                            that can be specified separately for each side of the display.
   :type two_sided_params: Sequence[str]

   :returns: two-sided version of stimulus function
   :rtype: function




 