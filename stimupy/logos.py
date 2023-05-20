import copy

import numpy as np

import stimupy

np.random.seed(1)

__all__ = ["logo"]


def logo(
    ppd=128,
    intensity_background=0.5,
):
    """Generate stimupy logo

    Parameters
    ----------
    ppd : Number (default: 128)
        pixels per degree along the axis of grating
    intensity_background : Number
        intensity value of background (default: 0.5)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        and additional keys containing stimulus parameters
    """

    # Parameters
    res = {"visual_size": 11, "ppd": ppd}
    radius = 5

    segments = stimupy.waves.square_angular(**res, n_segments=8, rotation=-(360 / 16))
    circle = stimupy.components.shapes.circle(**res, radius=radius, intensity_background=0)
    pie = copy.deepcopy(segments)

    pie.update(
        img=np.where(circle["circle_mask"], segments["img"], intensity_background),
        mask=np.where(circle["circle_mask"], segments["grating_mask"], 0),
        radius=circle["radius"],
    )

    # Create stimuli for pies
    grating = stimupy.stimuli.waves.sine_linear(**res, frequency=1, rotation=(360 / 8))
    dotted = stimupy.stimuli.sbcs.dotted(
        **res, n_dots=10, dot_radius=0.25, distance=0.1, target_shape=2
    )
    dotted = stimupy.utils.roll_dict(dotted, shift=-dotted["shape"][0] / 4, axes=0)
    grid = stimupy.stimuli.hermanns.grid(**res, element_size=(0.5, 0.5, 0.07))
    whites = stimupy.stimuli.whites.radial(**res, target_indices=(7, 14), frequency=2)
    plaid = stimupy.stimuli.plaids.sine_waves(
        grating_parameters1={**res, "frequency": 2},
        grating_parameters2={**res, "frequency": 1, "rotation": 45},
    )
    mondrian = stimupy.mondrians.corrugated_mondrian(
        **res, intensities=np.random.rand(10, 10), depths=(0, 0, 0, 0, 0, 0, 0, 1, -1, 0)
    )
    noise = stimupy.noises.naturals.pink(**res)

    # Fill segments
    pie["img"] = np.where(pie["mask"] == 1, intensity_background, pie["img"])
    pie["img"] = np.where(pie["mask"] == 2, grating["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 3, dotted["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 4, grid["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 5, whites["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 6, plaid["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 7, mondrian["img"], pie["img"])
    pie["img"] = np.where(pie["mask"] == 8, noise["img"], pie["img"])

    # Create eye components
    lens = stimupy.components.lines.ellipse(**res, radius=radius, line_width=0.02)
    pupil = stimupy.components.shapes.ellipse(**res, radius=(radius - 1.8, radius - 0.6))
    pupilmask = stimupy.components.shapes.rectangle(
        **res, rectangle_size=(11, 3), rectangle_position=(0, 0)
    )
    pupil["img"] = pupil["img"] * pupilmask["rectangle_mask"]
    pupil["ellipse_mask"] = (pupil["ellipse_mask"] * pupilmask["rectangle_mask"]).astype(int)
    pupil = stimupy.utils.roll_dict(pupil, shift=-pupil["shape"][1] / 5, axes=1)
    pupil["ellipse_mask"] = np.where(
        (pupil["ellipse_mask"] * segments["grating_mask"] * circle["circle_mask"]) == 1,
        pupil["ellipse_mask"],
        0,
    )

    pie["img"] = np.where((segments["grating_mask"] * lens["line_mask"]) == 1, 0, pie["img"])
    pie["img"] = np.where(pupil["ellipse_mask"] == 1, 0, pie["img"])

    return pie


def qrcode(ppd=128):
    import qrcode
    from PIL import Image, ImageDraw
    from qrcode.image.styledpil import StyledPilImage

    arr = np.array(logo(ppd, intensity_background=1)["img"])
    arr *= 255

    imsize = arr.shape
    im_logo = Image.new("L", (imsize[1], imsize[0]))
    im_logo.putdata(arr.flatten())

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data("https://stimupy.readthedocs.io/")
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=qrcode.image.styles.moduledrawers.CircleModuleDrawer(),
        # eye_drawer=qrcode.image.styles.moduledrawers.CircleModuleDrawer(),
        embeded_image=im_logo,
    )

    ## Make "eyes" circular
    eye_size = 70  # default
    quiet_zone = 40  # default

    eyes_mask = Image.new("L", img.size, 0)

    eye_border = quiet_zone + eye_size

    draw = ImageDraw.Draw(eyes_mask)
    draw.rectangle((quiet_zone, quiet_zone, eye_border, eye_border), fill=255)
    draw.rectangle(
        (img.size[0] - eye_border, quiet_zone, img.size[0] - quiet_zone, eye_border), fill=255
    )
    draw.rectangle(
        (quiet_zone, img.size[0] - eye_border, eye_border, img.size[0] - quiet_zone), fill=255
    )

    draw.rectangle((58, 58, 92, 92), fill=0)
    draw.rectangle((img.size[0] - 58, 92, img.size[0] - 92, 58), fill=0)
    draw.rectangle((55, img.size[0] - 92, 92, img.size[0] - 58), fill=0)

    round_eyes = Image.new("L", img.size, 255)

    draw = ImageDraw.Draw(round_eyes)
    draw.ellipse((quiet_zone, quiet_zone, eye_border, eye_border), fill=None, outline=0, width=8)
    draw.ellipse(
        (img.size[0] - eye_border, quiet_zone, img.size[0] - quiet_zone, eye_border),
        fill=None,
        outline=0,
        width=8,
    )
    draw.ellipse(
        (quiet_zone, img.size[0] - eye_border, eye_border, img.size[0] - quiet_zone),
        fill=None,
        outline=0,
        width=8,
    )

    final = Image.composite(round_eyes, img, eyes_mask)

    return final


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """

    # fmt: off
    stimuli = {
        "logo": logo(),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
