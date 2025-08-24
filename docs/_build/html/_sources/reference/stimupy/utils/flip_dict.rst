
flip_dict
=========



.. py:function:: stimupy.utils.flip_dict(dct, direction='lr', keys=('img', '*mask'))


   Return a dict with key-arrays rotated by nrots*90 degrees.

   :param dct: dict containing arrays to be stacked
   :type dct: dict
   :param direction: "lr" for left-right, "ud" for up-down flipping
   :type direction: str
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with flipped key-arrays
   :rtype: dict[str, Any]




 