import unittest

import HTMLTestRunner_PY3

import app
from script.test_ihrm_employee_parameterized import TestIhrmEmployee
from script.test_ihrm_login_parameterized import TestIHRMLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIhrmEmployee))

report_name = app.BASE_PATH +"/" +"report/ihrm.html"

with open(report_name,"wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="IHRM接口测试报告",description="人力资源模块")
    runner.run(suite)

print("测试增加一行代码，jenkins会不会自动构建")