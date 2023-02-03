import pytest

from stimuli.components.circulars import resolve_circular_params


@pytest.mark.parametrize(
    "ppd, shape, visual_size, n_rings, ring_width, frequency",
    (
        ((32, 32), (1024, 1024), (32, 32), 8, 2, 1 / 4),
        ((32, 32), (1024, 1024), (32, 32), 4, 1, 1 / 2),
        ((32, 32), (1024, 1024), (32, 32), 8, None, 1 / 2),
        ((32, 32), (1024, 1024), (32, 32), None, 2, None),
        ((32, 32), (1024, 1024), (32, 32), None, None, 1 / 2),
        ((None, None), (1024, 1024), (32, 32), 8, 2, None),
        (None, (1024, 1024), (32, 32), 8, 2, None),
        (None, (1024, 1024), (32, 32), None, None, 1),
        (None, (1024, 1024), None, 8, None, 1),
    ),
)
def test_valid_params(ppd, shape, visual_size, n_rings, ring_width, frequency):
    resolve_circular_params(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        n_rings=n_rings,
        ring_width=ring_width,
        frequency=frequency,
    )
