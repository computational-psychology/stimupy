
adapt_rms_contrast_dict
=======================



.. py:function:: stimupy.utils.contrast_conversions.adapt_rms_contrast_dict(stim, rms_contrast, mean_luminance=None)


   Adapt rms contrast of image (std)

   :param stim: stimulus dictionary containing at least key "img"
   :type stim: dict
   :param rms_contrast: desired rms contrast (std divided by mean intensity)
   :type rms_contrast: float
   :param mean_luminance: desired mean luminance; if None (default), dont change mean luminance
   :type mean_luminance: float

   :returns: dict with the stimulus (key: "img"),
             RMS contrast (key: "rms_contrast"),
             mean luminance ("mean_luminance")
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 