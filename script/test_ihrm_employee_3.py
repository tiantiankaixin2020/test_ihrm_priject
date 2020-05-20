# 创建测试类
# 编写测试函数
import logging
import unittest
import app
from api.employee_api import TestEmployeeApi
from api.login_api import LoginApi
from utiles import assert_comment


class TestIhrmEmployee3(unittest.TestCase):
    def setUp(self):
        self.emp_api = TestEmployeeApi()
        self.login_api = LoginApi()

    def test_01_login(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

        # 获取令牌
        token = response.json().get('data')

        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        app.HEADERS = headers


    def test_02_add_emp(self):
        response = self.emp_api.add_emp(app.HEADERS, "小偷家族77", "17512345677")
        logging.info("添加员工的结果是：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)
        emp_id = response.json().get("data").get("id")
        app.EMP_ID = emp_id


    def test_03_query_emp(self):
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询员工的结果是：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

    def test_04_mpdify_emp(self):
        response = self.emp_api.modify_emp(app.EMP_ID, app.HEADERS,"古力娜扎")
        logging.info("修改员工的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

    def test_05_delete_emp(self):
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除员工的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)
