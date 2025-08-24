
validate_visual_size
====================



.. py:function:: stimupy.utils.resolution.validate_visual_size(visual_size)


   Put specification of visual size in canonical form, if possible

   :param visual_size: if 2 elements: interpret as (height, width)
                       if 1 element: use as both height and width
                       if None: return (None, None)
                       each element has to be of type that can be cast to float, or None.
   :type visual_size: Sequence of length 1 or 2; or None

   :returns: .height: float, height in degrees visual angle
             .width: float, width in degrees visual angle
   :rtype: Visual_size NamedTuple, with two attributes

   :raises ValueError: if input does not have at least 1 element
   :raises TypeError: if input is not a Sequence(float, float) and cannot be cast to one
   :raises ValueError: if input has more than 2 elements




 