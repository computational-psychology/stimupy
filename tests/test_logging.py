import importlib
import logging
from io import StringIO

import pytest

import stimupy.papers

PAPERS_LIST = [f"stimupy.papers.{paper}" for paper in stimupy.papers.__all__]
MODULE_LIST = PAPERS_LIST + ["stimupy.components", "stimupy.noises", "stimupy.stimuli"]


@pytest.mark.parametrize("module_name", MODULE_LIST)
def test_no_logging_output_by_default(module_name):
    # Reload module
    module = importlib.import_module(module_name)
    importlib.reload(module)

    # Capture output: get logger, and attach new handler that we can capture and check
    logger = logging.getLogger(module_name)
    stream = StringIO()
    logger.addHandler(logging.StreamHandler(stream))

    # Should not emit anything at INFO level
    logger.info("Should not appear")
    output = stream.getvalue()
    assert output == ""

    stream.close()


@pytest.mark.parametrize("module_name", MODULE_LIST)
def test_global_logger_enables_output(module_name):
    # Set up global stimupy logger
    root_logger = logging.getLogger("stimupy")
    root_logger.setLevel(logging.DEBUG)
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    root_logger.addHandler(handler)

    # Reload module
    module = importlib.import_module(module_name)
    importlib.reload(module)

    # Log from submodule
    sub_logger = logging.getLogger(module_name)
    sub_logger.debug("Should appear")

    # Check output
    output = stream.getvalue()
    assert "Should appear" in output

    # Clean up
    root_logger.removeHandler(handler)
    stream.close()
