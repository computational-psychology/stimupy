"""Parameter classes for components.texts module."""

import param


class TextParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Text parameters
    text = param.String(default="Hello", doc="Text to display")
    font_size = param.Integer(default=50, bounds=(10, 100), doc="Font size")

    # Intensity parameters
    intensity_text = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Text intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "text": self.text,
            "fontsize": self.font_size,
            "intensity_text": self.intensity_text,
            "intensity_background": self.intensity_background,
        }


__all__ = ["TextParams"]
