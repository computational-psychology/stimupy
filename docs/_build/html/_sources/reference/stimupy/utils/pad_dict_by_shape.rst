
pad_dict_by_shape
=================



.. py:function:: stimupy.utils.pad_dict_by_shape(dct, padding, pad_value=0, keys=('img', '*mask'))


   Pad images in dictionary by specified amount(s) of pixels
   Can specify different amount (before, after) each axis.

   :param dct: dict containing image-arrays to be padded
   :type dct: dict
   :param padding: amount of padding, in pixels, in each direction:
                   ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
                   (int,) or int is a shortcut for before = after = pad width for all axes.
   :type padding: int, or Sequence[int, int], or Sequence[Sequence[int, int], ...]
   :param pad_val: value to pad with, by default 0.0
   :type pad_val: float, optional
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with larger key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]




 