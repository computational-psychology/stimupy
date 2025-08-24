
transparency
============



.. py:function:: stimupy.utils.contrast_conversions.transparency(img, mask=None, alpha=0.5, tau=0.2)


   Applies a transparency to image at specified (mask) location if provided

   :param img: image to which transparency will be applied
   :type img: np.array
   :param mask: if not None, transparency will be provided at non-zero locations
                provided in this mask
   :type mask: np.array or None (default)
   :param alpha: alpha of transparency (i.e. how transparent the medium is), default 0.2
   :type alpha: Number
   :param tau: tau of transparency (i.e. value of transparent medium), default 0.5
   :type tau: Number

   :rtype: img with the applied transparency




 