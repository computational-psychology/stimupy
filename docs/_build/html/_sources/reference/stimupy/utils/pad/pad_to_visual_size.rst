
pad_to_visual_size
==================



.. py:function:: stimupy.utils.pad.pad_to_visual_size(img, visual_size, ppd, pad_value=0)


   Pad image to specified visual size in degrees visual angle

   :param img: image-array to be padded
   :type img: numpy.ndarray
   :param visual_size: desired visual size (in degrees visual angle) of img after padding
   :type visual_size: Sequence[int, int, ...]
   :param ppd: pixels per degree
   :type ppd: Sequence[Number] or Sequence[Number, Number]
   :param pad_value: value to pad with, by default 0.0
   :type pad_value: Numeric, optional

   :returns: img padded by the specified amount(s)
   :rtype: numpy.ndarray

   .. seealso:: :obj:`stimupy.utils.resolution`




 