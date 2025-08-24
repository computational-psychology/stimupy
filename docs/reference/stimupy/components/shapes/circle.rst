
circle
======


.. image:: /_static/generated_stimuli/components.shapes.circle.png
   :alt: circle stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/circle.html>`__





.. py:function:: stimupy.components.shapes.circle(visual_size=None, ppd=None, shape=None, radius=None, intensity_circle=1.0, intensity_background=0.0, origin='mean', restrict_size=True)


   Draw an ellipse

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radius: circle radius in degrees visual angle
   :type radius: Number or None (default)
   :param intensity_circle: intensity value for circle, by default 1.0
   :type intensity_circle: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"
   :param restrict_size: if False, allow circle to reach beyond image size (default: True)
   :type restrict_size: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "circle_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 