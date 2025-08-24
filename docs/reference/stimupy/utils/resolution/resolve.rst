
resolve
=======



.. py:function:: stimupy.utils.resolution.resolve(shape=None, visual_size=None, ppd=None)


   Resolves the full resolution, for 2 givens and 1 unknown

   A resolution consists of a visual size in degrees, a shape in pixels,
   and specification of the number of pixels per degree.
   Since there is a strict geometric relation between these,
   shape = visual_size * ppd,
   if two are given, the third can be calculated using this function.

   This function resolves the resolution in both dimensions.


   :param shape: shape [height, width] in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param visual_size: visual size [height, width] in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)

   :returns: * *Shape NamedTuple, with two attributes* -- .height: int, height in pixels
               .width: int, width in pixels
               See validate_shape
             * *Visual_size NamedTuple, with two attributes* -- .height: float, height in degrees visual angle
               .width: float, width in degrees visual angle
               See validate_visual_size
             * *ppd NamedTuple, with two attributes* -- .vertical: int, vertical pixels per degree (ppd)
               .horizontal: int, horizontal pixels per degree (ppd)
               see validate_ppd




 