
compute_ppd
===========



.. py:function:: stimupy.utils.compute_ppd(screen_size, resolution, distance)


   Compute the pixels per degree in a presentation setup
   i.e., the number of pixels in the central one degree of visual angle

   :param screen_size: physical size, in whatever units you prefer, of the presentation screen
   :type screen_size: (float, float)
   :param resolution: screen resolution, in pixels,
                      in the same direction that screen size was measured in
   :type resolution: (float, float)
   :param distance: physical distance between the observer and the screen, in the same unit as screen_size
   :type distance: float

   :returns: ppd, the number of pixels in one degree of visual angle
   :rtype: float




 