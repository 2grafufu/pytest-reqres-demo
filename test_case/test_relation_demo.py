import pytest
import requests
import allure


@allure.feature("接口关联演示模块")
def test_relation_query_user(base_url, get_login_token):
    """
    接口关联演示：
    1. fixture先执行登录拿到token（上一个接口）
    2. 将token放到请求头，调用查询用户接口（下一个接口）
    """
    allure.title("登录获取token，携带token查询用户信息【接口关联演示】")

    # 把上一步登录接口拿到的token组装请求头
    headers = {
        "Authorization": f"Bearer {get_login_token}"
    }

    url = f"{base_url}/users/2"
    resp = requests.request(
        method="GET",
        url=url,
        headers=headers,
        proxies={"http": None, "https": None}
    )

    allure.attach(f"请求头headers：{headers}", name="请求头(携带token)", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应状态码：{resp.status_code}", name="状态码", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"响应报文：{resp.text}", name="返回报文", attachment_type=allure.attachment_type.TEXT)

    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["data"]["id"] == 2
