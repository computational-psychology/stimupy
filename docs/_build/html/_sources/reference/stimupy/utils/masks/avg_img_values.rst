
avg_img_values
==============



.. py:function:: stimupy.utils.masks.avg_img_values(image, mask, f_average=np.median)


   Average values of pixels in image, per target region in integer mask

   Values are calculated as means or medians, depending on the mode.

   :param image: 2D numpy array containing pixel values of the image
   :type image: 2D numpy array
   :param mask: 2D numpy array of same size as image. Each target patch has an integer value.
                Each pixel inside this patch has this integer value.
                Patches do not need to be continuous.
   :type mask: 2D numpy array
   :param f_average: How to average/summarise the pixels in each target region
   :type f_average: function, default=numpy.median

   :returns: each entry in the list is the average value of pixels in target region,
             index in the list is the integer index in the mask
   :rtype: list[float]

   .. seealso:: :obj:`all_img_values`




 