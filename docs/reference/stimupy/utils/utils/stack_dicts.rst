
stack_dicts
===========



.. py:function:: stimupy.utils.utils.stack_dicts(dct1, dct2, direction='horizontal', keys=('img', '*mask'), keep_mask_indices=False)


   Return a dict with resized key-arrays by the given factor. Every value is
   repeated factor[d] times along dimension d.

   :param dct1: dict containing arrays to be stacked
   :type dct1: dict
   :param dct2: dict containing arrays to be stacked
   :type dct2: dict
   :param direction: stack horizontal(ly) or vertical(ly) (default: horizontal)
   :type direction: str
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict1 but with stacked key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]




 