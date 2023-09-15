from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from stimupy.papers import modelfest
from stimupy.papers.modelfest import *  # noqa: F401,F403
from stimupy.utils import plot_comparison


def compare_by_name(stim_name, image_dir):
    """Compare current stimulus implementation against original image from file

    Parameters
    ----------
    stim_name : str
        name of the stimulus, which is both the `modelfest.<func_name>` and `<filename>.tif`
    image_dir : Path or str
        where to find the `.tif`

    Returns
    -------
    matplotlib.Figure
        comparison plot(s)

    See also
    --------
    stimupy.utils.plotting.plot_comparison
    """

    original_img_file = Path(image_dir) / f"{stim_name}.tif"
    original_img = np.array(Image.open(original_img_file))  # .astype(int)

    func = globals()[stim_name]
    new_img = func()["img"]
    new_img = (new_img * 255.0).round()

    original_img = original_img.astype(float) / 255.0
    new_img /= 255.0

    return plot_comparison(original_img, new_img)


def compare_all(image_dir):
    """Create comparisons for all ModelFest stimuli

    For each `modelfest.<stim>()`-function there has to be a corresponding `<stim>.tif`

    Parameters
    ----------
    image_dir : Path or str
        where to find the `.tif`s

    Returns
    -------
    None
        instead, saves all comparison plots in `<image_dir>/comparisons`
    """

    comparisons_dir = Path(image_dir) / "comparisons"

    if not comparisons_dir.exists():
        comparisons_dir.mkdir()

    for stim_name in modelfest.__all__:
        f = compare_by_name(stim_name, image_dir)

        plt.savefig(comparisons_dir / f"{stim_name}.png")
        plt.close(f)


if __name__ == "__main__":
    image_dir = Path(__file__).parent.resolve() / "modelfest"

    compare_all(image_dir=image_dir)
