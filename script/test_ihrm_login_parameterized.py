import unittest
import logging
from parameterized import parameterized
import app
from api.login_api import LoginApi
from utiles import assert_comment, read_login_data


class TestIHRMLogin(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    filename = app.BASE_PATH + "/data/login_data.json"

    @parameterized.expand(read_login_data(filename))
    def test_login(self, case_name, data, http_code, code, success, message):
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(http_code, code, success, message, response, self)
