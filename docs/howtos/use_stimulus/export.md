# Save & export stimuli

Stimuli created with `stimupy` should not be locked in
to any specific programming environment. 
As such, you can save and export stimuli to various formats.
Some formats support only saving the image-array
without any metadata --
others support saving the whole stimulus-`dict`.

```{contents}
```
## Fileformats

### Python `.pickle`
The Python standard library provides functionality for
saving Python objects to a binary file format called {py:mod}`pickle`.
This format is useful for quick, short-term storage of data,
although [there are some concerns](https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html)
about using it for long-term storage and sharing.
`stimupy` stimuli can be saved to this format,
either the whole stimulus-dict ({py:func}`stimupy.utils.export.to_pickle`)
or just the bare image-array ({py:func}`stimupy.utils.export.array_to_pickle`).

### Numpy `.npy`
The stimulus image-information of `stimupy` stimuli
are stored in {py:obj}`numpy.ndarray`s.
NumPy provides an efficient fileformat for saving these arrays:
[`.npy`](https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-save-and-load-numpy-objects).
`stimupy` stimuli can be saved to this format,
but only the bare image-array ({py:func}`stimupy.utils.export.array_to_npy`).

### JSON `.json`
[JavaScript Object Notation (JSON) files](https://www.wikiwand.com/en/JSON)
are a human- and machine-readable plain-text structured fileformat.
It is particularly well-suited for storing Python data structures
since JSON syntax is very similar to Python syntax for lists and dicts.
`stimupy` stimuli can be saved to this format,
as the whole stimulus-dict ({py:func}`stimupy.utils.export.to_json`)

### MATLAB `.mat`
To use stimuli in a MATLAB environment,
e.g., in a PsychToolBox-based experiment,
or a computational model that is (only) implemented in MATLAB,
the stimuli have to be exported to a format that MATLAB can interpret.
MATLAB does provide (some) support for JSON files
but `stimupy` can also export directly to MATLAB's native `.mat` fileformat.
`stimupy` stimuli can be saved to this format,
either the whole stimulus-dict ({py:func}`stimupy.utils.export.to_mat`)
or just the bare image-array ({py:func}`stimupy.utils.export.array_to_mat`).

### Image formats
For many uses, it can be convenient to just save the stimulus-array (or the mask) as an image.
Hence, `stimupy` provides a function to save/export bare image-arrays to common image formats (`.png`, `.jpeg`, etc).
Alternatively, there exist multiple image-processing libraries for Python which allow for further image processing and exporting,
e.g., [Pillow/PIL](https://pillow.readthedocs.io/en/stable/)
or [OpenCV](https://github.com/opencv/opencv-python)


## Exporting only parameters
In some cases, you may wish to save/export only the stimulus parameters
-- for a given version of `stimupy`,
these parameters should reproduce the exact same stimulus every time.
For stimuli created using just `stimupy` functions,
the output stimulus-`dict` contains not just the `img`-array
but also all parameters for creating that stimulus.
Thus, taking the `img` (and any `mask`s) out of this dict
creates a `dict` with just the parameters.
Since `dict`s can be _expanded_ in function calls,
this parameter-`dict` can then be used to recreate the stimulus:
```{code-block}
# Create a stimulus-dict
stim = stimuli.some_stim_func(...)

# 'strip' the dict of any key-value pairs that are not parameters to the given function
stim_params = utils.strip_dict(stim, stimuli.some_stim_func)

# reproduce the stimulus-dict by expanding stim_params
# reproduced_stim should be identical to stim
reproduced_stim = stimuli.some_stim_func(**stim_params)
```

To share only parameter values of an existing `stimupy` function
we recommend this approach of `strip`ping the `dict`
and then exporting this `strip`ed `dict` of params
to a `.json` file.

%% SOMETHING ABOUT HASHING IMGS