
pad_by_visual_size
==================



.. py:function:: stimupy.utils.pad_by_visual_size(img, padding, ppd, pad_value=0.0)


   Pad image by specified degrees of visual angle

   Can specify different amount (before, after) each axis.

   :param img: image-array to be padded
   :type img: numpy.ndarray
   :param padding: amount of padding, in degrees visual angle, in each direction:
                   ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
                   (float,) or float is a shortcut for before = after = pad width for all axes.
   :type padding: float, or Sequence[float, float], or Sequence[Sequence[float, float], ...]
   :param ppd: pixels per degree
   :type ppd: Sequence[Number] or Sequence[Number, Number]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: Numeric, optional

   :returns: img padded by the specified amount(s)
   :rtype: numpy.ndarray

   .. seealso:: :obj:`stimupy.utils.resolution`




 