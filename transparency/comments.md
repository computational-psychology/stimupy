23.03.2002 My Comments/ ToDo list:

- decide about how to import. checkerboard_mask.png cannot be found
- check consistency in indentation, in checkerboard_factory.py is mixed.
- in README, add instructions to how to install requirements.
- in example usage, make a one line comment what is happening in each step
- add plt.imshow() calls, to display the resulting images
- find_checkerboard() gives error when n_checks^2 > len(reflectances)*sample_repeat. Maybe check that this is not the case, if it is, then increase sample_repeat to min required and warn user
- get_stacked() returns a tuple with the masks included...
- with Yiqun with add an additional constrain to the checkerboard sampling: all reflectance values have to be behind the transparency, the same ones but shuffled. Check code and add this option here with a switch to activate this restriction / or not.
- it's not luminosity but luminance. change accordingly in all documentation, also fn parameters
- in texture factor, get_image(), alpha is inverted. higher alpha -> more transmissive.
- missing option of having a regular checkerboard with transparency on top... ?
- TextureFactory missing the 'stacked' version. maybe both horizontal and vertical stacked?