# Image size and resolution

## Shape in pixels
Digital images, such as stimuli, on a computer screen are drawn
with a certain `shape` in _pixels_.
The screen itself has a certain _resolution_,
e.g. $1024 \times 768$ pixels (width $\times$ height),
and a stimulus-images will take up some portion of that.
`stimupy` stimuli are produced and stored as 2-dimensional `numpy.ndarray`s
where each array-entry corresponds to the intensity of a single pixel.
In line with `numpy` convention,
`stimupy` refers to the `shape` of the stimulus in pixels,
which is the corresponding `.shape`-attribute of the `numpy.ndarray`.

## Visual size, in degrees visual angle
The proximal visual size of a stimulus as it reaches an observer
is not just based on the physical size (in cm, in, or pix) of the stimulus,
but also on the distance between the distal stimulus and the observer.
A physically large distal stimulus, will still appear small to an observer,
if it is far away -- and vice versa.
To take this into account, when specifying stimuli
we use the `visual_size`, expressed in _degrees of visual angle_.
This is an unambiguous specification of the size of the proximal stimulus
(as it arrives at the observer's eye),
regardless of the physical size of the (distal) image and its distance.

All size-parameters in `stimupy` are expressed in degrees visual angle.

## Resolution, in pixels per degree visual angle
To draw a stimulus of a given `visual_size`
as an image with a `shape` composed of discrete pixels,
a _resolution_ that maps between the two has to be provided as well.
This is measured in _pixels per degree_  -- `ppd` for short --
the amount of pixels that comprise a single degree of visual angle.

For stimuli presented on a screen to an observer,
the `ppd` can be calculated from
the resolution of the screen (in pixels),
the physical size of the screen (in cm, in),
and the distance between observer and screen.
In other words, the `ppd` depends on the display setup
and is not a property of the stimulus.
However, the `ppd` is _necessary_ to take
a specification of a stimulus defined in "natural" units of `visual_size`
an implement it as a digital image in pixels.


## Specifying size & resolution
`stimupy` stimulus-functions take these three size & resolution parameters:
`shape` in pixels, `visual_size` in degrees of visual angle, and `ppd`.
However, these three parameters are inter-dependent:
the `shape` can be calculated from `visual_size` and `ppd`;
a specification with given `visual_size` and `shape` requires a specific `ppd`.

Thus, not all combinations are valid resolutions,
e.g., if the `visual_size` $\times$ `ppd` does not match the given `shape`.
`stimupy` functions will raise a ResolutionException in these cases.
The {py:func}`stimupy.utils.valid_resolution <stimupy.utils.resolution.valid_resolution>`
function performs this assertion, and can be used to check that a resolution is valid.

This interdependence also means that
specifying all three parameters is not strictly necessary; 
if two are specified, the third can always be calculated.
In `stimupy`, functions that receive only two out of three resolution parameters,
or where one is explicitly set to `None`, will automatically resolve the resolution:
```{code-block} python
rectangle(visual_size=10, ppd=10, shape=None)
# or implicit None:
rectangle(visual_size=10, ppd=10)
```
This resolving is done using {py:func}`stimupy.utils.resolution.resolve`.
% ## Additional aspects

% ### Plot units
% ### Origin

% ### 1D vs. 2D