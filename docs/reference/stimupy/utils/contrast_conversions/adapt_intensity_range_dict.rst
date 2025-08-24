
adapt_intensity_range_dict
==========================



.. py:function:: stimupy.utils.contrast_conversions.adapt_intensity_range_dict(stim, intensity_min=0.0, intensity_max=1.0)


   Adapt intensity range of image

   :param stim: stimulus dictionary containing at least key "img"
   :type stim: dict
   :param intensity_min: new minimal intensity value
   :type intensity_min: float
   :param intensity_max: new maximal intensity value
   :type intensity_max: float

   :returns: dict with the stimulus (key: "img"),
             intensity range (key: "intensity_range"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 