
shape_from_visual_size_ppd
==========================



.. py:function:: stimupy.utils.shape_from_visual_size_ppd(visual_size, ppd)


   Calculate shape (pixels) from given visual size (degrees) and pixels-per-degree

   :param visual_size: each element has to be of type that can be cast to float, or None.
   :type visual_size: Sequence[Number, Number]; or Number; or None
   :param ppd: each element has to be of type that can be cast to int, or None.
               See validate_ppd
   :type ppd: Sequence[int, int]; or int, or None

   :returns: .height: int, height in pixels
             .width: int, width in pixels
             See validate_shape
   :rtype: Shape NamedTuple, with two attributes




 