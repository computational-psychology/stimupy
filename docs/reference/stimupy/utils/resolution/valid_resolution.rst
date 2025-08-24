
valid_resolution
================



.. py:function:: stimupy.utils.resolution.valid_resolution(shape, visual_size, ppd)


   Asserts that the combined specification of resolution is geometrically valid.

   Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
   If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
   this function passes without output.
   If the specification does not make sense, raises a ResolutionError.

   Note that the resolution specification has to be fully resolved,
   i.e., none of the parameters can be/contain None

   :param shape:
   :type shape: 2-tuple (height, width), or something that can be cast (see validate_shape)
   :param visual_size:
   :type visual_size: 2-tuple (height, width), or something that can be cast (see validate_visual_size)
   :param ppd:
   :type ppd: 2-tuple (vertical, horizontal), or something that can be cast (see validate_ppd)

   :raises ResolutionError: if resolution specification is invalid,
       i.e. (roughly), if int(visual_size * ppd) != shape




 