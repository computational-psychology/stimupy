
strip_dict
==========



.. py:function:: stimupy.utils.strip_dict(dct, func)


   Create a dictionary by stripping it from all keys that are not also
   an argument to the provided function

   :param dct: dict which will be stripped
   :type dct: dict
   :param func: Get argument names from this function
   :type func: function

   :returns: same as input dict but stripped from all keys which are not also
             an argument to the provided function
   :rtype: dict[str, Any]




 