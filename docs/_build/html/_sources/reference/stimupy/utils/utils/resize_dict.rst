
resize_dict
===========



.. py:function:: stimupy.utils.utils.resize_dict(dct, factor, keys=('img', '*mask'))


   Return a copy of an array, resized by the given factor. Every value is
   repeated factor[d] times along dimension d.

   :param dct: dict containing arrays to be resized
   :type dct: dict
   :param factor: the resize factor in the y and x dimensions
   :type factor: tuple of 2 ints
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with larger key-arrays according to
             "(arr.shape[0] * factor[0], arr.shape[1] * factor[1])"
             and updated keys for "visual_size" and "shape"
   :rtype: dict[str, Any]




 