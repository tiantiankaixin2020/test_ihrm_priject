import requests


class TestEmployeeApi:

    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net/api/sys/user"

    def add_emp(self,headers,username,mobile):
        response = requests.post(url=self.emp_url,
                                 headers=headers,
                                 json={
                                     "username": username,
                                     "mobile": mobile,
                                     "timeOfEntry": "2020-05-05",
                                     "formOfEmployment": 1,
                                     "workNumber": "1234123",
                                     "departmentName": "测试部",
                                     "departmentId": "1063678149528784896",
                                     "correctionTime": "2020-05-17T16:00:00.000Z"
                                 })
        return response

    def query_emp(self,emp_id,headers):
        query_url = self.emp_url + "/" + emp_id
        response = requests.get(url=query_url, headers=headers)
        return response

    def modify_emp(self,emp_id,headers,username):
        modify_url = self.emp_url + "/" + emp_id
        response = requests.put(url=modify_url, headers=headers, json={"username": username })
        return response

    def delete_emp(self,emp_id,headers):
        delete_url = self.emp_url + "/" + emp_id
        response = requests.delete(url=delete_url, headers=headers)
        return response
