
pad_dict_to_visual_size
=======================



.. py:function:: stimupy.utils.pad.pad_dict_to_visual_size(dct, visual_size, ppd, pad_value=0, keys=('img', '*mask'))


   Pad images in dictionary to specified visual size in degrees visual angle

   :param dct: dict containing image-arrays to be padded
   :type dct: dict
   :param visual_size: desired visual size (in degrees visual angle) of img after padding
   :type visual_size: Sequence[int, int, ...]
   :param ppd: pixels per degree
   :type ppd: Sequence[Number] or Sequence[Number, Number]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: Numeric, optional
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with larger key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]




 