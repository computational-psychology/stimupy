
munsell2luminance
=================



.. py:function:: stimupy.utils.munsell2luminance(munsell_values, reference_white)


   Transform Munsell values to luminance values.
   The luminance values will be in the same unit as the reference white, which
   can be arbitrary as long as the scale is linear.

   :param munsell_values:
   :type munsell_values: numpy-array
   :param reference_white:
   :type reference_white: number

   :returns: * **lum_values** (*numpy-array*)
             * **Reference** (*H. Pauli, "Proposed extension of the CIE recommendation*)
             * *on 'Uniform color spaces, color difference equations, and metric color*
             * *terms'," J. Opt. Soc. Am. 66, 866-867 (1976)*




 