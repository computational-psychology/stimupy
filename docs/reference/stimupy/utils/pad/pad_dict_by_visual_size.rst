
pad_dict_by_visual_size
=======================



.. py:function:: stimupy.utils.pad.pad_dict_by_visual_size(dct, padding, ppd, pad_value=0.0, keys=('img', '*mask'))


   Pad images in dictionary by specified degrees of visual angle

   Can specify different amount (before, after) each axis.

   :param dct: dict containing image-arrays to be padded
   :type dct: dict
   :param padding: amount of padding, in degrees visual angle, in each direction:
                   ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
                   (float,) or float is a shortcut for before = after = pad width for all axes.
   :type padding: float, or Sequence[float, float], or Sequence[Sequence[float, float], ...]
   :param ppd: pixels per degree
   :type ppd: Sequence[Number] or Sequence[Number, Number]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: Numeric, optional
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with larger key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]




 