
resolve_1D
==========



.. py:function:: stimupy.utils.resolve_1D(length=None, visual_angle=None, ppd=None, round=True)


   Resolves the full resolution, for 2 givens and 1 unknown

   A resolution consists of a visual size in degrees, a shape in pixels,
   and specification of the number of pixels per degree.
   Since there is a strict geometric relation between these,
   shape = visual_size * ppd,
   if two are given, the third can be calculated using this function.

   This function resolves the resolution in a single dimension.


   :param length:
   :type length: Number, length in pixels, or None (default)
   :param visual_angle:
   :type visual_angle: Number, length in degrees, or None (default)
   :param ppd:
   :type ppd: Number, pixels per degree, or None (default)

   :returns: * **length** (*int, length in pixels*)
             * **visual_angle** (*float, length in degrees*)
             * **ppd** (*float, pixels per degree*)




 