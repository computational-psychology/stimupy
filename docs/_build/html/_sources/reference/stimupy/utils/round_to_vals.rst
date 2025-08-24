
round_to_vals
=============



.. py:function:: stimupy.utils.round_to_vals(arr, vals, mode='nearest')


   Round each element of array to closest match in provided values

   For each element in the input `arr`, find the closest value from the provided `vals`
   and replace the element with this closest value.
   If the element is equidistant to two values, the smaller
   value is chosen.

   :param arr: array to be rounded
   :type arr: np.ndarray
   :param vals: values to which array will be rounded
   :type vals: Sequence(float, ...)
   :param mode: rounding mode. Default is "nearest".
   :type mode: ["nearest", "floor", "ceil"], optional

   :returns: **out_arr** -- Rounded output array
   :rtype: np.ndarray

   :raises ValueError: If `mode` is not one of ["nearest", "floor", "ceil"].
       If `arr` contains values outside the bounds of
       `vals` when `mode` is "floor" or "ceil".

   .. rubric:: Examples

   >>> arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
   >>> vals = [1, 3, 5]
   >>> round_to_vals(arr, vals)
   array([1., 3., 3., 5., 5.])




 