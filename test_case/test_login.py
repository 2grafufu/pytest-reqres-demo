import pytest
import requests
import allure
from conftest import read_yaml

login_test_data = read_yaml("data/login_case.yaml")


@allure.feature("登录模块")
@pytest.mark.parametrize("case", login_test_data)
def test_login_param(base_url, case):
    """yaml数据驱动登录接口"""
    allure.title(case["case_name"])



    payload = {"email": case["email"]}
    if case["password"] is not None:
        payload["password"] = case["password"]

    resp = requests.post(f"{base_url}/login", json=payload, headers={})

    allure.attach(f"请求payload：{payload}", name="请求参数", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应状态码：{resp.status_code}", name="响应状态码", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应结果：{resp.text}", name="接口返回报文", attachment_type=allure.attachment_type.TEXT)

    # 断言状态码
    assert resp.status_code == case["expect_status"], f"{case['case_name']} 状态码校验失败"
    resp_json = resp.json()

    if case["expect_have_token"]:
        assert "token" in resp_json
    else:
        assert "token" not in resp_json
