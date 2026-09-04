import pytest
import requests
import allure
from conftest import read_yaml

user_test_data = read_yaml("data/user_case.yaml")


@allure.feature("用户管理模块")
@pytest.mark.parametrize("case", user_test_data)
def test_user_operate(base_url, case):
    allure.title(case["case_name"])
    url = base_url + case["url"]
    method = case["method"]
    payload = case.get("payload", None)

    # headers={} 强制清空全部额外请求头，避免混入Authorization导致401
    resp = requests.request(method, url, json=payload, headers={})

    allure.attach(f"请求地址：{url}", name="请求地址", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"请求体：{payload}", name="请求参数", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应状态码：{resp.status_code}", name="状态码", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应报文：{resp.text}", name="返回报文", attachment_type=allure.attachment_type.TEXT)

    # 断言状态码
    assert resp.status_code == case["expect_status"], f"{case['case_name']} 状态码校验失败"

    # 如果需要校验用户id
    if "expect_user_id" in case:
        resp_json = resp.json()
        assert resp_json["data"]["id"] == case["expect_user_id"]
