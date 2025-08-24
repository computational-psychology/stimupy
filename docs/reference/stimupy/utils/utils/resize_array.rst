
resize_array
============



.. py:function:: stimupy.utils.utils.resize_array(arr, factor)


   Return a copy of an array, resized by the given factor. Every value is
   repeated factor[d] times along dimension d.

   :param arr: the array to be resized
   :type arr: 2D array
   :param factor: the resize factor in the y and x dimensions
   :type factor: tuple of 2 ints

   :rtype: An array of shape (arr.shape[0] * factor[0], arr.shape[1] * factor[1])




 