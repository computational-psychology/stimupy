
ellipse
=======


.. image:: /_static/generated_stimuli/components.shapes.ellipse.png
   :alt: ellipse stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/ellipse.html>`__





.. py:function:: stimupy.components.shapes.ellipse(visual_size=None, ppd=None, shape=None, radius=None, intensity_ellipse=1.0, intensity_background=0.0, rotation=0.0, origin='mean', restrict_size=True)


   Draw an ellipse

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radius: ellipse radius [ry, rx] in degrees visual angle
   :type radius: Sequence[Number, Number], Number or None (default)
   :param intensity_ellipse: intensity value for ellipse, by default 1.0
   :type intensity_ellipse: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"
   :param restrict_size: if False, allow ellipse to reach beyond image size (default: True)
   :type restrict_size: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "ellipse_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 