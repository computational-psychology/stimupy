
luminance2munsell
=================



.. py:function:: stimupy.utils.luminance2munsell(lum_values, reference_white)


   Transform luminance values into Munsell values.
   The luminance values do not have to correspond to specific units, as long
   as they are in the same unit as the reference white, because Munsell values
   are a perceptually uniform scale of relative luminances.

   :param lum_values:
   :type lum_values: numpy-array
   :param reference_white:
   :type reference_white: number

   :returns: * **munsell_values** (*numpy-array*)
             * **Reference** (*H. Pauli, "Proposed extension of the CIE recommendation*)
             * *on 'Uniform color spaces, color difference equations, and metric color*
             * *terms'," J. Opt. Soc. Am. 66, 866-867 (1976)*




 