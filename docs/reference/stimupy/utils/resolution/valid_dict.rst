
valid_dict
==========



.. py:function:: stimupy.utils.resolution.valid_dict(dct)


   Asserts that the combined specification of resolution in dict is geometrically valid.

   Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
   If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
   this function passes without output.
   If the specification does not make sense, raises a ResolutionError.

   Note that the resolution specification has to be fully resolved,
   i.e., none of the parameters can be/contain None

   :param dct: dictionary with at least the keys "shape", "ppd", "visual_size"
   :type dct: dict

   :raises ResolutionError: if resolution specification is invalid,
       i.e. (roughly), if int(visual_size * ppd) != shape




 