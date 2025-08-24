
pad_dict_to_shape
=================



.. py:function:: stimupy.utils.pad_dict_to_shape(dct, shape, pad_value=0, keys=('img', '*mask'))


   Pad images in dictionary to a resulting specified shape in pixels

   :param dct: dict containing image-arrays to be padded
   :type dct: dict
   :param shape: desired shape of img after padding
   :type shape: Sequence[int, int, ...]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: float, optional
   :param keys: keys in dict for images to be padded
   :type keys: Sequence[String, String] or String

   :returns: same as input dict but with larger key-arrays and updated keys for
             "visual_size" and "shape"
   :rtype: dict[str, Any]

   :raises ValueError: if img.shape already exceeds shape




 