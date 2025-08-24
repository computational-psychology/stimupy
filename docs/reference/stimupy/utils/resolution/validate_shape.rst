
validate_shape
==============



.. py:function:: stimupy.utils.resolution.validate_shape(shape)


   Put specification of shape (in pixels) in canonical form, if possible

   :param shape: if 2 elements: interpret as (height, width)
                 if 1 element: use as both height and width
                 if None: return (None, None)
                 each element has to be of type that can be cast to int, or None.
   :type shape: Sequence of length 1 or 2; or None

   :returns: .height: int, height in pixels
             .width: int, width in pixels
   :rtype: Shape NamedTuple, with two attributes

   :raises ValueError: if input does not have at least 1 element
   :raises TypeError: if input is not a Sequence(int, int) and cannot be cast to one
   :raises ValueError: if input has more than 2 elements




 