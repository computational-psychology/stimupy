
roll_dict
=========



.. py:function:: stimupy.utils.roll_dict(dct, shift, axes, keys=('img', '*mask'))


   Return a dict with key-arrays rolled by shift in axes.

   :param dct: dict containing arrays to be stacked
   :type dct: dict
   :param shift: number of pixels by which to shift
   :type shift: int
   :param axes: axes in which to shift
   :type axes: Number or Sequence[Number, ...]
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with rolled key-arrays
   :rtype: dict[str, Any]




 