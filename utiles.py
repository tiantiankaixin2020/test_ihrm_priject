import json

import app


def assert_comment(statues_code, code, success, mseeage, response, self):
    self.assertEqual(statues_code, response.status_code)
    self.assertEqual(code, response.json().get("code"))
    self.assertEqual(success, response.json().get("success"))
    self.assertIn(mseeage, response.json().get("message"))


# 读取登录数据的函数
def read_login_data(filename):
    with open(filename, mode='r', encoding='utf=8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
        print(result_list)
    return result_list


if __name__ == '__main__':
    filename = app.BASE_PATH + "/data/login_data.json"
    read_login_data(filename)


# 定义员工增删改查的参数化函数
def read_emp_data(filename, name):
    result_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        emp_data = jsonData.get(name)
        result_list.append(tuple(emp_data.values()))
    print(result_list)
    return result_list


if __name__ == '__main__':
    filename = app.BASE_PATH + "/data/emp_data.json"
    read_emp_data(filename, 'add_emp')
    read_emp_data(filename, 'query_emp')
    read_emp_data(filename, 'modify_emp')
    read_emp_data(filename, 'delete_emp')
