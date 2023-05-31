from testpage import RestTest
import logging


def test_step6(login, text1):
    logging.info("Test6 Starting")
    result = RestTest()
    assert text1 in result.get_someone_post(login)


def test_step7(login, checking_description):
    logging.info("Test7 Starting")
    result = RestTest()
    result.add_new_post(login)
    assert checking_description in result.get_my_post(login)
