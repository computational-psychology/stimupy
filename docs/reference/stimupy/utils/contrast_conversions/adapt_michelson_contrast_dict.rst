
adapt_michelson_contrast_dict
=============================



.. py:function:: stimupy.utils.contrast_conversions.adapt_michelson_contrast_dict(stim, michelson_contrast, mean_luminance=None)


   Adapt Michelson contrast of image in dict

   :param stim: stimulus dictionary containing at least key "img"
   :type stim: dict
   :param michelson_contrast: desired Michelson contrast
   :type michelson_contrast: float
   :param mean_luminance: desired mean luminance; if None (default), dont change mean luminance
   :type mean_luminance: float

   :returns: dict with the stimulus (key: "img"),
             Michelson contrast (key: "michelson_contrast"),
             mean luminance ("mean_luminance")
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 