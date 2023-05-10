# Share & distribute stimuli
A core principle of `stimupy` is sharing and reusing stimuli.
One part of this is the large number of existing stimuli already implement,
such that you can generate various parameterizations of these
without having to write any custom code.
The other part is that, hopefully, you will share the `stimupy`-stimuli
that you use in your work.


## What to share?
To accurately reproduce a stimulus,
a complete description of the parameters (size, geometry, radiometry)
should be enough.
However, in developing `stimupy` it has been our experience that
such descriptions are often incomplete and parameters can be easily overlooked.

Another option is to share the exact digital image (i.e., the matrix of pixel values)
of the stimulus.
While this allows that exact digital image to be reused,
any modifications may be hard to implement --
especially changing the [resolution](../topic_guides/resolution.md).
Moreover, sets of digital images can take up quite some storage space,
and are not ideal for easy and quick transfer.

Instead, we believe that the _code_ underlying stimulus creation should be shared,
alongside the parameters used to call that code.
The combination of the same exact code plus the same parameters should *always*
produce the exact same digital image.
Thus, you can share the code and parameters,
and a recipient can reproduce your exact stimulus.

This is why we distribute `stimupy`:
it contains lots of (generalized) code to generate lots of (parameterizable) stimuli.
When you use this to generate specific stimuli in your own work
there are several ways to share the require code and parameters,
depending on whether you "just" used specific parameterization of a function in `stimupy`,
or added some custom code (e.g., composition).

````{important}
In general, the following should be communicated / shared:

0. Platform and environment information
  - Operating System (and version)
  - Python version
  - versions of all other requisite packages:
    A full list of installed Python packages and their version numbers can be generated
    using (from outside Python):
    ```{code-block} bash
    pip freeze
    ```

1. exact `stimupy` version
   This version can be found using (from within Python):
   ```{code-block} python
   >>> import stimupy
   >>> stimupy.__version__
   '1.0.0'
   >>>
   ```
2. parameters for stimupy-stimuli
3. any custom code, e.g. for composition
````

## Existing stimulus, specific parameterization

If your work uses a stimulus as it is implemented in `stimupy`,
e.g., some {py:func}`gabor <stimupy.stimuli.gabors.gabor>`
or some parameterization of the {py:func}`Todorovic illusion <stimupy.stimuli.todorovics.cross>`,
without any additional customization / custom code (e.g., composition),
you only need to share the parameter-values for this stimulus.
All the code necessary to reproduce the stimulus from those values
is included in `stimupy`.
Thus, you'll need to:

- indicate which exact version of `stimupy` you used.
  A recipient can then install this version of `stimupy`
  and reproduce the exact stimulus from the provide parameter values.

- provide all parameter-values for this stimulus, ideally by [exporting them](export.md).
  For just sharing paramter-values, we recommend sharing the stimulus-`dict`
  without the `img` and `masks` to a [JSON file](./export.md).
  This because JSON files are both human-readable -- so that a non-stimupy / non-Python
  recipient can still evaluate the parameter values -- and safely machine-readable
  -- so that a Python / stimupy user can easily load and recreate the stimulus.

%% SOMETHING ABOUT HASHING

## Custom stimulus
If your stimulus is not just a parameterization of an existing `stimupy` function
and contains some custom code (e.g., composition),
you will also need to distribute your custom code.
This can be done in several ways.

If you are already sharing all the code
underlying the rest of your experiment or project (whether in PsychoPy or otherwise),
you can simply include your custom stimulus code in this as well.
You should also indicate which exact version of `stimupy` was used,
which is then an exactly versioned dependency of your code.

In this case, it is probably clearest to _modularize_
your (custom) stimulus-generating code by putting it in a separate code file,
e.g. `my_stimulus.py` (or `my_stim.m` for MATLAB)
-- which then gets used in the main experiment / project code.
This modularization of the stimulus makes it so that changes to the stimulus
can be isolated from changes to the rest of the project.
Additionally, if you or someone else wants to use the same stimulus
in a different experiment/project,
only that file needs to be shared (together with versioning and parameterization info).

If you are _not_ already sharing all the code
underlying the rest of your experiment or project,
firstly we highly encourage you to do so, in the spirit of the Open and FAIR science
that `stimupy` tries to contribute to.
However, if reasons preclude sharing the whole code
but you still wish to share & distribute your stimuli,
we also recommend modularizing your stimulus-generating code into a separate file.
This can then be shared, together with versioning and parameterization info.

```{important}
`stimupy` is focused on stimulus generation, not on code or data distribution.
If you wish to distribute your parameter-values and/or custom stimulus code,
we recommend code- and data-sharing platforms
such as [GitHub](https://www.github.com), [FigShare](https://www.figshare.com), and the [Open Science Framework](https://www.OSF.io)
```


## Stimulus-sets
`stimupy` contains both a wide range of generalized [stimulus-functions](stimupy.stimuli)
that can generate many parameterizated stimulus images.
Also included are several complete sets of stimuli
that all come from the same {py:mod}`paper <stimupy.papers>` (/ source).
The ones currently included span wide range of the stimuli implemented in `stimupy`
and have formed both the inspiration and a testing benchmark for development.

Development, organization and maintanance of these sets can be arduous,
and we are committed to providing a high-quality and well-tested suite of functions.
Thus, `stimupy` is a curated and maintained _library_ of stimuli
(stimulus-functions, to be precise),
not a _repository_ or platform for uploading stimuli.
We welcome contributions to this library of stimuli,
and stimulus sets, from the literature.
If you wish to contribute such a complete set of stimuli from a single paper,
please see our [contributing guide](../contributing/contribute.md).

