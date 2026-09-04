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
    """前置登录，提取token，供其他用例做接口关联"""
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
    print(f"\n====fixture获取token: {token}====")
    return token


def read_yaml(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f.read())
