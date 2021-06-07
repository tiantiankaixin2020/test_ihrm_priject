import unittest
import logging
from api.login_api import LoginApi
from utiles import assert_comment


class TestIHRMLogin(unittest.TestCase):
#111111
    def setUp(self):
        self.login_api = LoginApi()

求别覆盖

    def tearDown(self):
        # 注释
        pass
        
    def test01_login_success22(self):
        data1 = 1

    def test01_login_success(self):
        data = {"mobile": "13800000002", "password": "123456"}1
        headers = {"Content-Type": "application/json"}1
        response = self.login_api.login(data, headers)1
        logging.info("登222录的111111结果为：{}".format(response.json()))1
        assert_comment(200, 10000, True, "操作成功", response, self)  # 调用函数 进行断言1

    def test02_mobile_is_not_exist(self):
        data = {"mobile": "13900000002", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test03_password_error(self):
        data = {"mobile": "13800000002", "password": "12344456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test04_mobile_empty(self):
        data = {"mobile": "", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test05_password_empty(self):
        data = {"mobile": "13800000002", "password": ""}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test06_mobile_special_char(self):
        data = {"mobile": "138000(0002", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test07_more_params(self):
        data = {"mobile": "13800000002", "password": "123456","more_params":"1"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

    def test08_less_password(self):
        data = {"mobile": "13800000002"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test09_less_mobile(self):
        data = {"paasword": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test10_null_params(self):
        data = {}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test11_wrong_params(self):
        data = {"mobile": "13800000002", "paasssword": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 20001, False, "用户名或密码错误", response, self)

    def test12_input_none(self):
        data = None
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(data, headers)
        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 99999, False, "抱歉，系统繁忙，请稍后重试！", response, self)


