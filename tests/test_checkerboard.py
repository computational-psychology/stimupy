import pytest
from stimuli.components.checkerboard import checkerboard, resolve_checkerboard_params


@pytest.mark.parametrize(
    "ppd, shape, visual_size, board_shape, check_visual_size",
    (
        ((32, 32), (1024, 1024), (32, 32), (16, 16), (2, 2)),
        ((32, 32), (1024, 1024), (32, 32), (16, 16), (None, None)),
        ((32, 32), (1024, 1024), (32, 32), (16, 16), None),
        ((32, 32), (1024, 1024), (32, 32), (None, None), (2, 2)),
        ((32, 32), (1024, 1024), (32, 32), None, (2, 2)),
        ((None, None), (1024, 1024), (32, 32), (16, 16), (2, 2)),
        (None, (1024, 1024), (32, 32), (16, 16), (2, 2)),
        (None, (1024, 1024), (32, 32), (16, 16), None),
    ),
)
def test_valid_params(ppd, shape, visual_size, board_shape, check_visual_size):
    resolve_checkerboard_params(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
    )


@pytest.mark.parametrize(
    "ppd, shape, visual_size, board_shape, check_visual_size",
    (
        (None, None, (32, 32), (16, 16), (2, 2)),
        (None, (1024, 1024), None, (16, 16), (2, 2)),
    ),
)
def test_too_many_unknowns(ppd, shape, visual_size, board_shape, check_visual_size):
    with pytest.raises(ValueError):
        resolve_checkerboard_params(
            ppd=ppd,
            shape=shape,
            visual_size=visual_size,
            board_shape=board_shape,
            check_visual_size=check_visual_size,
        )


def test_checkerboard():
    pass


def test_invalid_params():
    pass
