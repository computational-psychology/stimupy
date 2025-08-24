
rotate_dict
===========



.. py:function:: stimupy.utils.rotate_dict(dct, nrots=1, keys=('img', '*mask'))


   Return a dict with key-arrays rotated by nrots*90 degrees.

   :param dct: dict containing arrays to be stacked
   :type dct: dict
   :param nrot: number of rotations by 90 degrees
   :type nrot: int
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with rotated key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]




 