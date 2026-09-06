import pytest
import requests
import allure
from conftest import read_yaml

res_test_data = read_yaml("data/res_case.yaml")

@pytest.mark.resource
@allure.feature("资源&注册模块")
@pytest.mark.parametrize("case", res_test_data)
def test_resource_register(base_url, case):
    allure.title(case["case_name"])
    url = base_url + case["url"]
    method = case["method"]
    payload = case.get("payload", None)

    resp = requests.request(
        method,
        url,
        json=payload,
        headers={},
        proxies={"http": None, "https": None}
    )

    allure.attach(f"请求地址：{url}", name="请求地址", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"请求体：{payload}", name="请求参数", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应状态码：{resp.status_code}", name="状态码", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应报文：{resp.text}", name="返回报文", attachment_type=allure.attachment_type.TEXT)

    # 断言状态码
    assert resp.status_code == case["expect_status"], f"{case['case_name']} 状态码校验失败"

    # 校验资源id
    if "expect_resource_id" in case:
        resp_json = resp.json()
        assert resp_json["data"]["id"] == case["expect_resource_id"]
