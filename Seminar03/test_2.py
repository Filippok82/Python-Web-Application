import logging
from BaseApp import checkText


def test_step5(good, bad):
    logging.info("Test5 Starting")
    assert good in checkText(bad)
