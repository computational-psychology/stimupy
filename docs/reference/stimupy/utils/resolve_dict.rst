
resolve_dict
============



.. py:function:: stimupy.utils.resolve_dict(dct)


   Resolves the full resolution ("shape", "ppd", "visual_size"), for 2
   givens and 1 unknown in the input dictionary

   A resolution consists of a visual size in degrees, a shape in pixels,
   and specification of the number of pixels per degree.
   Since there is a strict geometric relation between these,
   shape = visual_size * ppd,
   if two are given, the third can be calculated using this function.

   This function resolves the resolution in both dimensions.

   :param dct: dictionary with at least two out the three keys: "shape", "ppd", "visual_size"
   :type dct: dict

   :rtype: Resolved dict

   .. seealso:: :obj:`stimupy.utils.resolution`




 