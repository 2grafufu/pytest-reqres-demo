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

    # 组装token鉴权请求头，完成接口关联：登录返回的token作为本接口header入参
    # 注意：reqres为mock接口，不支持鉴权，所以 demo 中将组装鉴权头的代码注释保存作为示例，不实际发送
    #headers = {
    #    "Authorization": f"Bearer {get_login_token}"
    #}
    headers={}


    #
    # 1.先创建用户
    #create_payload = {"name": "test", "job": "tester"}
    #resp_create = requests.post(f"{base_url}/users", json=create_payload)
    #new_id = resp_create.json()["id"]  # 拿到后端返回的id

    # 2.把上一步拿到的new_id拼到url，查询刚刚创建的用户
    #url = f"{base_url}/users/{new_id}"
    #resp_query = requests.get(url)


    #当前使用 reqres 模拟接口，它的数据不会持久化保存；调用创建用户接口之后，无法通过返回的 id 查询到刚刚新建的数据。
    #所以示例中暂时硬编码写死 id=2 做演示。如果是真实业务接口，需要拿到创建接口返回的 id，用变量拼接 url，完成真正接口关联。
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
