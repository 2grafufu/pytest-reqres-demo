import pytest
import yaml
import os
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


# =====接口关联fixture：登录获取token，整个测试会话只执行一次登录=====
@pytest.fixture(scope="session")
def get_login_token(base_url):
    """前置登录，提取token，供其他用例做接口关联；演示yield前后置"""
    # ---------------- 前置：scope=session，所有用例执行前执行1次 ----------------
    login_url = f"{base_url}/login"
    login_body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    resp = requests.post(
        login_url,
        json=login_body,
        headers={},
        proxies={"http": None, "https": None}
    )
    # 断言登录成功
    assert resp.status_code == 200, "登录获取token失败"
    token = resp.json()["token"]
    print(f"\n====【fixture前置】获取token: {token}====")

    # 将token传给测试函数，在这里暂停，去跑所有测试用例
    yield token

    # ---------------- 后置：session范围内全部用例跑完之后，才执行这里 ----------------
    print("\n====【fixture后置】全部会话用例执行完成，模拟执行登出/资源清理====")
    # 真实业务场景这里可以写：调用登出接口、清理测试数据、关闭连接等逻辑



def read_yaml(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f.read())
