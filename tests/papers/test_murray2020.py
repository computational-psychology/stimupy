import os.path
import pickle

import numpy as np
from stimuli.papers.murray2020 import *

data_dir = os.path.dirname(__file__)
picklefile = os.path.join(data_dir, "murray2020.pickle")
loaded = pickle.load(open(picklefile, "rb"))


def test_argyle():
    assert np.all(
        argyle()["img"] == loaded["argyle"]["img"]
    ), "argyle imgs are different"
    assert np.all(
        argyle()["mask"] == loaded["argyle"]["mask"]
    ), "argyle masks are different"


def test_argyle_control():
    assert np.all(
        argyle_control()["img"] == loaded["argyle_control"]["img"]
    ), "argyle_control imgs are different"
    assert np.all(
        argyle_control()["mask"] == loaded["argyle_control"]["mask"]
    ), "argyle_control masks are different"


def test_argyle_long():
    assert np.all(
        argyle_long()["img"] == loaded["argyle_long"]["img"]
    ), "argyle_long imgs are different"
    assert np.all(
        argyle_long()["mask"] == loaded["argyle_long"]["mask"]
    ), "argyle_long masks are different"


def test_snake():
    assert np.all(
        snake()["img"] == loaded["snake"]["img"]
    ), "snake imgs are different"
    assert np.all(
        snake()["mask"] == loaded["snake"]["mask"]
    ), "snake masks are different"


def test_snake_control():
    assert np.all(
        snake_control()["img"] == loaded["snake_control"]["img"]
    ), "snake_control imgs are different"
    assert np.all(
        snake_control()["mask"] == loaded["snake_control"]["mask"]
    ), "snake_control masks are different"


def test_koffka_adelson():
    assert np.all(
        koffka_adelson()["img"] == loaded["koffka_adelson"]["img"]
    ), "koffka_adelson imgs are different"
    assert np.all(
        koffka_adelson()["mask"] == loaded["koffka_adelson"]["mask"]
    ), "koffka_adelson masks are different"


def test_koffka_broken():
    assert np.all(
        koffka_adelson()["img"] == loaded["koffka_adelson"]["img"]
    ), "koffka_adelson imgs are different"
    assert np.all(
        koffka_adelson()["mask"] == loaded["koffka_adelson"]["mask"]
    ), "koffka_adelson masks are different"


def test_koffka_connected():
    assert np.all(
        koffka_connected()["img"] == loaded["koffka_connected"]["img"]
    ), "koffka_connected imgs are different"
    assert np.all(
        koffka_connected()["mask"] == loaded["koffka_connected"]["mask"]
    ), "koffka_connected masks are different"


def test_checkassim():
    assert np.all(
        checkassim()["img"] == loaded["checkassim"]["img"]
    ), "checkassim imgs are different"
    assert np.all(
        checkassim()["mask"] == loaded["checkassim"]["mask"]
    ), "checkassim masks are different"


def test_simcon():
    assert np.all(
        simcon()["img"] == loaded["simcon"]["img"]
    ), "simcon imgs are different"
    assert np.all(
        simcon()["mask"] == loaded["simcon"]["mask"]
    ), "simcon masks are different"


def test_simcon_articulated():
    assert np.all(
        simcon_articulated()["img"] == loaded["simcon_articulated"]["img"]
    ), "simcon_articulated imgs are different"
    assert np.all(
        simcon_articulated()["mask"] == loaded["simcon_articulated"]["mask"]
    ), "simcon_articulated masks are different"


def test_white():
    assert np.all(
        white()["img"] == loaded["white"]["img"]
    ), "white imgs are different"
    assert np.all(
        white()["mask"] == loaded["white"]["mask"]
    ), "white masks are different"
