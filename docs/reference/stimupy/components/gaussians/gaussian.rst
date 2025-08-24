
gaussian
========


.. image:: /_static/generated_stimuli/components.gaussians.gaussian.png
   :alt: gaussian stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/gaussians/gaussian.html>`__





.. py:function:: stimupy.components.gaussians.gaussian(visual_size=None, ppd=None, shape=None, sigma=None, rotation=0.0, intensity_max=1.0, origin='mean')


   Create a Gaussian (envelop)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param sigma: Sigma auf Gaussian in degree visual angle (y, x)
   :type sigma: float or (float, float)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional
   :param intensity_max: Maximal intensity value of Gaussian
   :type intensity_max: float
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img")
             ellipse-like mask with sigma radius and integer index (key: "gaussian_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 