



utils
=====


.. py:module:: stimupy.utils









Modules
-------

.. autoapisummary::

   stimupy.utils.color_conversions
   stimupy.utils.contrast_conversions
   stimupy.utils.export
   stimupy.utils.filters
   stimupy.utils.masks
   stimupy.utils.pad
   stimupy.utils.plotting
   stimupy.utils.resolution
   stimupy.utils.utils



































Functions
---------


.. autosummary::
    luminance2munsell
    munsell2luminance
    transparency
    adapt_michelson_contrast
    adapt_rms_contrast
    adapt_normalized_rms_contrast
    adapt_intensity_range
    adapt_michelson_contrast_dict
    adapt_rms_contrast_dict
    adapt_normalized_rms_contrast_dict
    adapt_intensity_range_dict
    array_to_checksum
    array_to_image
    array_to_npy
    array_to_mat
    array_to_pickle
    arrays_to_checksum
    to_json
    to_mat
    to_pickle
    convolve
    bandpass
    avg_target_values
    avg_img_values
    all_img_values
    img_values
    add_padding
    remove_padding
    pad_by_visual_size
    pad_to_visual_size
    pad_by_shape
    pad_to_shape
    pad_dict_by_visual_size
    pad_dict_to_visual_size
    pad_dict_by_shape
    pad_dict_to_shape
    plot_stim
    plot_stimuli
    plot_comparison
    resolve
    resolve_1D
    resolve_dict
    visual_angle_from_length_ppd
    visual_angles_from_lengths_ppd
    visual_size_from_shape_ppd
    length_from_visual_angle_ppd
    lengths_from_visual_angles_ppd
    shape_from_visual_size_ppd
    ppd_from_shape_visual_size
    ppd_from_length_visual_angle
    compute_ppd
    validate_shape
    validate_ppd
    validate_visual_size
    valid_1D
    valid_resolution
    valid_dict
    round_to_vals
    int_factorize
    get_function_argument_names
    apply_bessel
    resize_array
    resize_dict
    stack_dicts
    rotate_dict
    flip_dict
    roll_dict
    strip_dict
    make_two_sided
    permutate_params
    create_stimspace_stimuli


.. _luminance2munsell:

.. autoapifunction:: luminance2munsell
.. _munsell2luminance:

.. autoapifunction:: munsell2luminance
.. _transparency:

.. autoapifunction:: transparency
.. _adapt_michelson_contrast:

.. autoapifunction:: adapt_michelson_contrast
.. _adapt_rms_contrast:

.. autoapifunction:: adapt_rms_contrast
.. _adapt_normalized_rms_contrast:

.. autoapifunction:: adapt_normalized_rms_contrast
.. _adapt_intensity_range:

.. autoapifunction:: adapt_intensity_range
.. _adapt_michelson_contrast_dict:

.. autoapifunction:: adapt_michelson_contrast_dict
.. _adapt_rms_contrast_dict:

.. autoapifunction:: adapt_rms_contrast_dict
.. _adapt_normalized_rms_contrast_dict:

.. autoapifunction:: adapt_normalized_rms_contrast_dict
.. _adapt_intensity_range_dict:

.. autoapifunction:: adapt_intensity_range_dict
.. _array_to_checksum:

.. autoapifunction:: array_to_checksum
.. _array_to_image:

.. autoapifunction:: array_to_image
.. _array_to_npy:

.. autoapifunction:: array_to_npy
.. _array_to_mat:

.. autoapifunction:: array_to_mat
.. _array_to_pickle:

.. autoapifunction:: array_to_pickle
.. _arrays_to_checksum:

.. autoapifunction:: arrays_to_checksum
.. _to_json:

.. autoapifunction:: to_json
.. _to_mat:

.. autoapifunction:: to_mat
.. _to_pickle:

.. autoapifunction:: to_pickle
.. _convolve:

.. autoapifunction:: convolve
.. _bandpass:

.. autoapifunction:: bandpass
.. _avg_target_values:

.. autoapifunction:: avg_target_values
.. _avg_img_values:

.. autoapifunction:: avg_img_values
.. _all_img_values:

.. autoapifunction:: all_img_values
.. _img_values:

.. autoapifunction:: img_values
.. _add_padding:

.. autoapifunction:: add_padding
.. _remove_padding:

.. autoapifunction:: remove_padding
.. _pad_by_visual_size:

.. autoapifunction:: pad_by_visual_size
.. _pad_to_visual_size:

.. autoapifunction:: pad_to_visual_size
.. _pad_by_shape:

.. autoapifunction:: pad_by_shape
.. _pad_to_shape:

.. autoapifunction:: pad_to_shape
.. _pad_dict_by_visual_size:

.. autoapifunction:: pad_dict_by_visual_size
.. _pad_dict_to_visual_size:

.. autoapifunction:: pad_dict_to_visual_size
.. _pad_dict_by_shape:

.. autoapifunction:: pad_dict_by_shape
.. _pad_dict_to_shape:

.. autoapifunction:: pad_dict_to_shape
.. _plot_stim:

.. autoapifunction:: plot_stim
.. _plot_stimuli:

.. autoapifunction:: plot_stimuli
.. _plot_comparison:

.. autoapifunction:: plot_comparison
.. _resolve:

.. autoapifunction:: resolve
.. _resolve_1D:

.. autoapifunction:: resolve_1D
.. _resolve_dict:

.. autoapifunction:: resolve_dict
.. _visual_angle_from_length_ppd:

.. autoapifunction:: visual_angle_from_length_ppd
.. _visual_angles_from_lengths_ppd:

.. autoapifunction:: visual_angles_from_lengths_ppd
.. _visual_size_from_shape_ppd:

.. autoapifunction:: visual_size_from_shape_ppd
.. _length_from_visual_angle_ppd:

.. autoapifunction:: length_from_visual_angle_ppd
.. _lengths_from_visual_angles_ppd:

.. autoapifunction:: lengths_from_visual_angles_ppd
.. _shape_from_visual_size_ppd:

.. autoapifunction:: shape_from_visual_size_ppd
.. _ppd_from_shape_visual_size:

.. autoapifunction:: ppd_from_shape_visual_size
.. _ppd_from_length_visual_angle:

.. autoapifunction:: ppd_from_length_visual_angle
.. _compute_ppd:

.. autoapifunction:: compute_ppd
.. _validate_shape:

.. autoapifunction:: validate_shape
.. _validate_ppd:

.. autoapifunction:: validate_ppd
.. _validate_visual_size:

.. autoapifunction:: validate_visual_size
.. _valid_1D:

.. autoapifunction:: valid_1D
.. _valid_resolution:

.. autoapifunction:: valid_resolution
.. _valid_dict:

.. autoapifunction:: valid_dict
.. _round_to_vals:

.. autoapifunction:: round_to_vals
.. _int_factorize:

.. autoapifunction:: int_factorize
.. _get_function_argument_names:

.. autoapifunction:: get_function_argument_names
.. _apply_bessel:

.. autoapifunction:: apply_bessel
.. _resize_array:

.. autoapifunction:: resize_array
.. _resize_dict:

.. autoapifunction:: resize_dict
.. _stack_dicts:

.. autoapifunction:: stack_dicts
.. _rotate_dict:

.. autoapifunction:: rotate_dict
.. _flip_dict:

.. autoapifunction:: flip_dict
.. _roll_dict:

.. autoapifunction:: roll_dict
.. _strip_dict:

.. autoapifunction:: strip_dict
.. _make_two_sided:

.. autoapifunction:: make_two_sided
.. _permutate_params:

.. autoapifunction:: permutate_params
.. _create_stimspace_stimuli:

.. autoapifunction:: create_stimspace_stimuli
















  