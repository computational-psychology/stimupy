
avg_target_values
=================



.. py:function:: stimupy.utils.masks.avg_target_values(stim, mask_key='target_mask', f_average=np.median)


   Average pixel value in each target region of stimulus

   :param stim: stimulus-dict with at least "img" and "mask"
                containing the stimulus image and integer-mask, respectively.
   :type stim: dict[str: Any]
   :param mask_key: string with mask-key name
   :type mask_key: str
   :param f_average: How to average/summarise the pixels in each target region
   :type f_average: function, default=numpy.median

   :returns: each entry in the list is the average value of pixels in target region,
             index in the list is the integer index in the mask
   :rtype: list[float]

   .. seealso:: :obj:`avg_img_values`




 