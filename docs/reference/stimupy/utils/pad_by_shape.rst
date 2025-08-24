
pad_by_shape
============



.. py:function:: stimupy.utils.pad_by_shape(img, padding, pad_value=0)


   Pad image by specified amount(s) of pixels

   Can specify different amount (before, after) each axis.

   :param img: image-array to be padded
   :type img: numpy.ndarray
   :param padding: amount of padding, in pixels, in each direction:
                   ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
                   (int,) or int is a shortcut for before = after = pad width for all axes.
   :type padding: int, or Sequence[int, int], or Sequence[Sequence[int, int], ...]
   :param pad_val: value to pad with, by default 0.0
   :type pad_val: float, optional

   :returns: img padded by the specified amount(s)
   :rtype: numpy.ndarray




 