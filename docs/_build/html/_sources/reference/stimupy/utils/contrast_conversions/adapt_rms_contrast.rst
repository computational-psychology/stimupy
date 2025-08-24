
adapt_rms_contrast
==================



.. py:function:: stimupy.utils.contrast_conversions.adapt_rms_contrast(img, rms_contrast, mean_luminance=None)


   Adapt rms contrast of image (std)

   :param img: stimulus array
   :type img: np.ndarray
   :param rms_contrast: desired rms contrast (std divided by mean intensity)
   :type rms_contrast: float
   :param mean_luminance: desired mean luminance; if None (default), dont change mean luminance
   :type mean_luminance: float

   :returns: **img** -- image with adapted rms contrast and mean luminance if passed
   :rtype: np.ndarray




 