import os
import pytest

from utils.Requests_Util import Request

@pytest.fixture(scope='class')
def token():
    url = "https://kdtx-test.itheima.net/api/captchaImage"
    r = Request('=====前置条件（获取登录所需的uuid）========').get(url)
    uuid = r['body']["uuid"]

    url = "https://kdtx-test.itheima.net/api/login"
    data ={
        'username': "admin",
        'password': "HM_2023_test",
        'code': "2",
        'uuid': uuid}
    r = Request('=====前置条件（获取登录成功返回的token）=====').post(url, json=data)
    print(r['body']['token'])
    yield r['body']['token']




def pytest_sessionfinish():
    os.system("allure generate ./allure-results -o ./allure -c")
