
bandpass
========



.. py:function:: stimupy.utils.filters.bandpass(visual_size=None, ppd=None, shape=None, center_frequency=None, bandwidth=None)


   Function to create a 2d bandpass filter in the frequency domain

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param center_frequency: center frequency of filter in cpd
   :type center_frequency: float
   :param bandwidth: bandwidth of filter in octaves
   :type bandwidth: float

   :returns: dict with the filter (key: "img"),
             and additional keys containing filter parameters
   :rtype: dict[str, Any]




 