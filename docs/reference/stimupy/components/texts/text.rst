
text
====


.. image:: /_static/generated_stimuli/components.texts.text.png
   :alt: text stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/texts/text.html>`__





.. py:function:: stimupy.components.texts.text(text, visual_size=None, ppd=None, shape=None, intensity_text=0.0, intensity_background=0.5, fontsize=36, align='center')


   Draw given text into a (numpy) image-array

   If no shape is provided / can be resolved,
   tightly fits the bounding box of the drawn text.

   :param text: Text to draw
   :type text: str
   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param intensity_text: intensity of text in range (0.0; 1.0), by default 0.0
   :type intensity_text: float, optional
   :param intensity_background: intensity value of background in range (0.0; 1.0), by default 0.5
   :type intensity_background: float, optional
   :param fontsize: font size, by default 36
   :type fontsize: int, optional
   :param align: alignment of text, by default "center"
   :type align: "left", "center" (default), "right"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the text (key: "text_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 