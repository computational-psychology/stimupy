
convolve
========



.. py:function:: stimupy.utils.filters.convolve(arr1, arr2, mode='same', axes=None, padding=False)


   Convolve two N-dimensional arrays using FFT

   :param arr1: Input array 1
   :type arr1: numpy.ndarray
   :param arr2: Input array 2
   :type arr2: numpy.ndarray
   :param mode: String which indicates the size of the output. The default is "same".
   :type mode: str {"full", "valid", "same"}, optional
   :param axes: Axes over which to convolve. The default is over all axes
   :type axes: int or None (default), optional
   :param padding: if True, pad array before convolving
   :type padding: Bool

   :returns: **out** -- Output array
   :rtype: numpy.ndarray




 