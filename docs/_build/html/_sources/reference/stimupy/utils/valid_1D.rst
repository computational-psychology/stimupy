
valid_1D
========



.. py:function:: stimupy.utils.valid_1D(length, visual_angle, ppd)


   Asserts that the combined specification of resolution is geometrically valid.

   Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
   If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
   this function passes without output.
   If the specification does not make sense, raises a ResolutionError.

   Note that the resolution specification has to be fully resolved,
   i.e., none of the parameters can be None

   :param length:
   :type length: int, length in pixels
   :param visual_angle:
   :type visual_angle: float, size in degrees
   :param ppd:
   :type ppd: int, resolution in pixels-per-degree

   :raises ResolutionError: if resolution specification is invalid,
       i.e. (roughly), if int(visual_angle * ppd) != length




 