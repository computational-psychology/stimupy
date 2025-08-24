
all_img_values
==============



.. py:function:: stimupy.utils.masks.all_img_values(img, mask)


   Isolate all image values/pixels, per target region specified in integer mask

   :param img: Image-array of pixel values to be masked
   :type img: numpy.ndarray
   :param mask: Array of same size as img.
                Each region-of-interest in mask is represented by an integer index.
                Each pixel inside this patch has this integer value.
                Patches do not need to be contiguous.
   :type mask: numpy.ndarray

   :returns: Each image/element of the list is a numpy.ndarray representing an image.
             There is one image for each target patch in the integer mask.
             In each image all values are set to NaN
             except the ones corresponding to the target values of the respective target patch.
   :rtype: list[numpy.arrays]

   .. seealso:: :obj:`img_values`




 