
arrays_to_checksum
==================



.. py:function:: stimupy.utils.arrays_to_checksum(stim, keys=['img', 'mask'])


   Hash (md5) values of arrays specified in keys, and save only the hex

   :param stim: stimulus dictionary to export.
   :type stim: dict
   :param keys: keys of dict for which the hashing should be performed
   :type keys: str of list of str

   :returns: same as input dict but keys now only contain the hex
   :rtype: dict[str, Any]




 