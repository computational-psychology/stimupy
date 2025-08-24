
pad_to_shape
============



.. py:function:: stimupy.utils.pad_to_shape(img, shape, pad_value=0)


   Pad image to a resulting specified shape in pixels

   :param img: image-array to be padded
   :type img: numpy.ndarray
   :param shape: desired shape of img after padding
   :type shape: Sequence[int, int, ...]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: float, optional

   :returns: img padded to specified shape
   :rtype: numpy.ndarray

   :raises ValueError: if img.shape already exceeds shape




 