
img_values
==========



.. py:function:: stimupy.utils.masks.img_values(img, mask)


   Isolate only image pixels specified by a binary mask

   :param img: Image-array of pixel values to be masked
   :type img: numpy.ndarray
   :param mask: Array of same size as img.
                All non-zero pixels/values are treated as ones in a binary bit mask.
   :type mask: numpy.ndarray

   :returns: numpy.ndarray of same size as img.
             All bits corresponding to zero bits in the mask are set to NaN.
   :rtype: numpy.ndarray




 