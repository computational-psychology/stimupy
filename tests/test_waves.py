import pytest

from stimupy.components import waves


@pytest.mark.parametrize(
    "ppd, length, visual_angle, n_phases, phase_width, frequency",
    (
        (32, 1024, 32, 8, 2, 1 / 4),
        (32, 1024, 32, 4, 1, 1 / 2),
        (32, 1024, 32, 8, None, 1 / 2),
        (32, 1024, 32, None, 2, None),
        (32, 1024, 32, None, None, 1 / 2),
        (None, 1024, 32, 8, 2, None),
        (None, 1024, 32, 8, 2, None),
        (None, 1024, 32, None, None, 1),
        (None, 1024, None, 8, None, 1),
    ),
)
def test_valid_params(ppd, length, visual_angle, n_phases, phase_width, frequency):
    waves.resolve_grating_params(
        ppd=ppd,
        length=length,
        visual_angle=visual_angle,
        n_phases=n_phases,
        phase_width=phase_width,
        frequency=frequency,
    )


def test_rounding():
    ppd = 36
    visual_size = (1.0, 1.0)
    frequency = 2.80
    stim = waves.square(
        ppd=ppd,
        visual_size=visual_size,
        frequency=frequency,
        period="either",
        distance_metric="horizontal",
        phase_shift=0,
        origin="corner",
        round_phase_width=True,
    )


def test_overview():
    waves.overview()
