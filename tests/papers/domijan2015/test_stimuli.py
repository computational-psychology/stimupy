import pytest
import numpy as np
import matplotlib.pyplot as plt

import ground_truth
import stimuli.papers.domijan2015
from stimuli.utils import compare_plots


def test_dungeon():
    original = ground_truth.get_dungeon()
    test = stimuli.papers.domijan2015.dungeon().img
    assert np.array_equal(original, test)


def test_cube():
    original = ground_truth.get_cube()
    test = stimuli.papers.domijan2015.cube().img
    assert np.array_equal(original, test)


def test_grating():
    original = ground_truth.get_grating()
    test = stimuli.papers.domijan2015.grating().img
    assert np.array_equal(original, test)


def test_ring():
    original = ground_truth.get_ring()
    test = stimuli.papers.domijan2015.rings().img
    assert np.array_equal(original, test)


def test_bullseye():
    original = ground_truth.get_bullseye()
    test = stimuli.papers.domijan2015.bullseye().img
    assert np.array_equal(original, test)


def test_sbc():
    original = ground_truth.get_sbc()
    test = stimuli.papers.domijan2015.simultaneous_brightness_contrast().img
    assert np.array_equal(original, test)


def test_white():
    original = ground_truth.get_white()
    test = stimuli.papers.domijan2015.white().img
    assert np.array_equal(original, test)


def test_benary():
    original = ground_truth.get_benary()
    test = stimuli.papers.domijan2015.benary().img
    assert np.array_equal(original, test)


def test_todorovic():
    original = ground_truth.get_todorovic()
    test = stimuli.papers.domijan2015.todorovic().img
    assert np.array_equal(original, test)


def test_checkerboard():
    original = ground_truth.get_checkerboard()
    test = stimuli.papers.domijan2015.checkerboard().img
    assert np.array_equal(original, test)


def test_checkerboard_extended():
    original = ground_truth.get_checkerboard_extended()
    test = stimuli.papers.domijan2015.checkerboard_extended().img
    assert np.array_equal(original, test)


def test_checkerboard_contrast_contrast():
    original = ground_truth.get_contrast_contrast()
    test = stimuli.papers.domijan2015.checkerboard_contrast_contrast().img
    assert np.array_equal(original, test)
