
ppd_from_shape_visual_size
==========================



.. py:function:: stimupy.utils.ppd_from_shape_visual_size(shape, visual_size)


   Calculate resolution (ppd) from given shape (pixels) and visual size (degrees)

   :param shape: each element has to be of type that can be cast to int, or None.
                 See validate_shape
   :type shape: Sequence[int, int]; or int, or None
   :param visual_size: each element has to be of type that can be cast to float, or None.
                       See validate_visual_size
   :type visual_size: Sequence[Number, Number]; or Number; or None

   :returns: .vertical: int, vertical pixels per degree (ppd)
             .horizontal: int, horizontal pixels per degree (ppd)
             see validate_ppd
   :rtype: ppd NamedTuple, with two attributes




 