
validate_ppd
============



.. py:function:: stimupy.utils.resolution.validate_ppd(ppd)


   Put specification of ppd in canonical form, if possible

   :param ppd: if 2 elements: interpret as (vertical, horizontal)
               if 1 element: use as both vertical and horizontal
               if None: return (None, None)
               each element has to be of type that can be cast to int, or None.
   :type ppd: Sequence of length 1 or 2; or None

   :returns: .vertical: int, vertical pixels per degree (ppd)
             .horizontal: int, horizontal pixels per degree (ppd)
   :rtype: ppd NamedTuple, with two attributes

   :raises ValueError: if input does not have at least 1 element
   :raises TypeError: if input is not a Sequence(int, int) and cannot be cast to one
   :raises ValueError: if input has more than 2 elements




 