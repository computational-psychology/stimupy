# Integrate in experiments
`stimupy` is a package which is focused on generating stimuli,
separate from stimulus display, use, experimentation, etc.
Hence, `stimupy` is designed agnostic to how stimuli are used after stimulus generation,
which allows for a broad range of uses.
Principally, the stimulus image is stored
as a matrix of intensity values, in a bare {py:obj}`numpy.ndarray`.
Thus, using a `stimupy` stimulus in an application
just requires the possibility to input a `numpy.ndarray`.


## PsychoPy-based display
[PsychoPy](https://psychopy.org/) is a leading stimulus display
and experiment development package for the Python ecosystem.
It provides lots of functionality for running experiments, interfacing with hardware
and some stimulus-drawing capabilities.
Most of the stimulus-drawing is done using an OpenGL backend
directly in the screen buffer.
While this approach is very fast and accurate,
its difficult to create complex stimulus images, such as the ones implemented in `stimupy`.
For these kinds of stimuli,
PsychoPy can display predefined digital images as a static texture
using the [ImageStim](https://psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim) function:
```{code-block} python
stim = psychopy.visual.ImageStim(my_window, image=my_numpy_array)
```

To use `stimupy` stimuli in PyschoPy experiments, then, is quite straightforward
and requires no e.g. additional exporting of the stimulus:

1. Set up experiment using `PsychoPy`
   1. Set up the screen/window information
2. Generate the `stim` using `stimupy` code
3. Create the PsychoPy `ImageStim` from the `stim["img"]`-array
4. Display the `ImageStim` in the PsychoPy experiment.

```{warning}
`stimupy` is designed for flexibility, robustness, and ease of use -- not for speed.
Some of the quality-of-life features have some processing overhead,
e.g., automatic resolution resolving.
As a result, `stimupy` stimulus functions may be slower than generating
equivalent stimuli using OpenGL based rendering.
If speed is of the essence, you may want to pregenerate all your `stimupy` stimuli
before the experiment-loop,
such that displaying a stimulus is just a single lookup.
```

## PsychToolBox-based (MATLAB) display
[PsychToolBox (PTB)](http://psychtoolbox.org/) is the MATLAB progenitor of the PsychoPy.
It provides lots of functionality for running experiments, interfacing with hardware
and some stimulus-drawing capabilities.
Most of the stimulus-drawing is done using an OpenGL backend
directly in the screen buffer.
While this approach is very fast and accurate,
its difficult to create complex stimulus images, such as the ones implemented in `stimupy`.
For these kinds of stimuli,
PTB can convert a (predefined) digital image from an array to a static texture
and then display it,
using the [Screen('MakeTexture')](http://psychtoolbox.org/docs/Screen) function:
```{code-block} matlab
% Convert my_stim_array to a PTB texture
stim_texture = Screen('MakeTexture', my_window, my_stim_array);

% Put texture on screen
Screen('DrawTexture', my_window, stim_texture);
```

To use `stimupy` stimuli in PyschoPy experiments then
requires creating the stimuli in, and exporting them from Python,
and importing them into MATLAB for display:

1. Generate the `stim` using `stimupy` code (Python)
2. [Export the `stim`, e.g. to `.mat` file](./export.md) (Python)
3. Set up experiment using `PTB` (MATLAB)
   1. Set up the screen/window information
4. Import the `stim` in MATLAB, e.g.:
    ```{code-block} matlab
    % Load from .mat file into a struct
    my_stim = load('path_to_my_stim_file.mat');
    ```
5. Create the PTB texture from the `img`-array:
    ```{code-block} matlab
    % Convert my_stim_array to a PTB texture
    stim_texture = Screen('MakeTexture', my_window, my_stim.img);
    ```
6. Display the texture in the PTB experiment