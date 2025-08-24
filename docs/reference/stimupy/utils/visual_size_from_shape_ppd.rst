
visual_size_from_shape_ppd
==========================



.. py:function:: stimupy.utils.visual_size_from_shape_ppd(shape, ppd)


   Calculate visual size (degrees) from given shape (pixels) and pixels-per-degree

   :param shape: each element has to be of type that can be cast to int, or None.
                 See validate_shape
   :type shape: Sequence[int, int]; or int, or None
   :param ppd: each element has to be of type that can be cast to int, or None.
               See validate_ppd
   :type ppd: Sequence[int, int]; or int, or None

   :returns: .height: float, height in degrees visual angle
             .width: float, width in degrees visual angle
             See validate_visual_size
   :rtype: Visual_size NamedTuple, with two attributes




 