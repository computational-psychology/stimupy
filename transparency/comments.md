23.03.2020 My Comments/ ToDo list:

- decide about how to import: make system module with setup.py (example is our hrl module)
- error: checkerboard_mask.png cannot be found.
- in README, add instructions to how to install requirements.
- in README example usage, make a one line comment describing what is happening in each step/line of code
- add plt.imshow() calls to the README example usage, to display the resulting images
- it's not luminosity but luminance. change accordingly in all documentation, also functions' parameters

In Checkerboard Factory

- find_checkerboard() algorithmus, to replace=True and without sample_repeat.
- find_checkerboard() gives error when n_checks^2 > len(reflectances)*sample_repeat. Maybe check that this is not the case, if it is, then increase sample_repeat to min required and warn user

- with Yiqun we added an additional constrain to the checkerboard sampling: all reflectance values have to be behind the transparency, the same ones but shuffled. Check code and add this option here with a switch to activate this restriction / or not.

- check consistency in indentation, it is mixed in checkerboard_factory.py.
- get_stacked() returns a tuple with the masks included.



In Texture Factory:
- in texture factor, get_image(), alpha is inverted. higher alpha -> more transmissive.
- TextureFactory missing the 'stacked' version. maybe both horizontal and vertical stacked?
