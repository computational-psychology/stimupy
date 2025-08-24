
array_to_image
==============



.. py:function:: stimupy.utils.export.array_to_image(arr, filename, format=None, norm=True)


   Save a 2D numpy array as a grayscale image file.

   :param arr: array to be exported. Values will be cropped to [0,255].
   :type arr: numpy.ndarray
   :param filename: (full) path to the file to be created.
   :type filename: Path or str
   :param norm: multiply array by 255, by default True
   :type norm: bool




 