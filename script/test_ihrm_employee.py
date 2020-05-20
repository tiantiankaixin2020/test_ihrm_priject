import unittest
import logging
from api.employee_api import TestEmployeeApi
from api.login_api import LoginApi
from utiles import assert_comment


class TestIHRMEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_api = TestEmployeeApi()
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    def test01_emp_mange(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        logging.info("登录的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

        # 获取令牌
        token = response.json().get('data')
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}

        response = self.emp_api.add_emp(headers, "小偷家族55", "17512345676")
        logging.info("添加员工的结果是：{}".format(response.json()))
        emp_id = response.json().get("data").get("id")  # 提取添加员工响应数据中的id

        response = self.emp_api.query_emp(emp_id, headers)
        logging.info("查询员工的结果是：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

        response = self.emp_api.modify_emp(emp_id, headers, "古力娜扎")
        logging.info("修改员工的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)

        response = self.emp_api.delete_emp(emp_id, headers)
        logging.info("删除员工的结果为：{}".format(response.json()))
        assert_comment(200, 10000, True, "操作成功", response, self)
