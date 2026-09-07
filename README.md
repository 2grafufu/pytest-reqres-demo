# Pytest API Automation Demo

基于 **Python + Pytest + Requests + YAML + Allure** 实现的接口自动化测试 Demo。

项目使用免费公开的 ReqRes API 作为测试对象，实现了数据驱动、Fixture 前后置、接口关联、多业务模块测试以及 Allure 测试报告输出等功能。

---

## 一、项目功能

* YAML 数据驱动
* Pytest 参数化执行测试用例
* Fixture 前后置处理
* 登录接口获取 Token
* 接口关联
* 多业务模块测试
* GET / POST / PUT / DELETE 请求
* 正常场景与异常场景测试
* Allure 测试报告
* 请求参数、请求头、响应状态码、响应报文附件

---

## 二、技术栈

| 技术       | 作用          |
| -------- | ----------- |
| Python   | 自动化测试开发语言   |
| Pytest   | 测试框架        |
| Requests | HTTP 接口请求   |
| PyYAML   | YAML 测试数据读取 |
| Allure   | 测试报告        |
| Git      | 代码版本管理      |

---

## 三、项目结构

```text
pytest_api_demo/
│
├── data/
│   ├── login_case.yaml        # 登录模块测试数据
│   ├── user_case.yaml         # 用户模块测试数据
│   └── res_case.yaml          # 资源模块测试数据
│
├── test_case/
│   ├── __init__.py
│   ├── test_login.py          # 登录模块测试
│   ├── test_user.py           # 用户管理模块测试
│   ├── test_resources.py      # 资源、注册模块测试
│   └── test_relation_demo.py  # 接口关联测试
│
├── conftest.py                # Pytest Fixture及公共配置
├── pytest.ini                 # Pytest配置
├── .gitignore                 # git忽略文件
└── README.md
```

---

## 四、测试模块

### 1. 登录模块

测试登录接口的不同场景：

* 正常登录
* Password 参数缺失
* 账号为空

通过 YAML 文件维护测试数据，并使用 `pytest.mark.parametrize` 实现数据驱动执行。

登录成功后校验：

* HTTP 状态码
* 响应结果是否包含 Token

---

### 2. 用户管理模块

覆盖用户管理相关接口：

* 查询用户
* 查询不存在用户
* 创建用户
* 更新用户信息
* 删除用户

涉及接口方法：

```text
GET
POST
PUT
DELETE
```

---

### 3. 资源与注册模块

资源接口：

* 获取资源列表
* 获取指定资源
* 获取不存在资源

注册接口：

* 用户注册成功
* 缺少 Password 参数
* 非法邮箱注册

通过 YAML 维护不同请求方法、请求地址、请求参数和预期结果。

---

### 4. 接口关联模块

使用 Pytest Fixture 实现接口关联。

执行流程：

```text
登录接口
   ↓
获取 Token
   ↓
Fixture 返回 Token
   ↓
后续接口获取 Token
   ↓
组装 Authorization 请求头（代码注释保存示例）
   ↓
调用需要鉴权的接口
```

Token 请求头格式：

```text
Authorization: Bearer <token>
```

---



## 五、数据驱动

测试数据使用 YAML 文件维护。

示例：

```yaml
- case_name: 正常登录
  email: eve.holt@reqres.in
  password: cityslicka
  expect_status: 200
  expect_have_token: true
```

测试代码通过：

```python
@pytest.mark.parametrize("case", login_test_data)
```

读取多组测试数据，实现测试代码和测试数据分离。

---

## 六、Allure 测试报告

项目使用 Allure 生成测试报告。

测试过程中会记录：

* 请求地址
* 请求参数
* 请求头
* 响应状态码
* 响应报文

执行测试：

```bash
pytest
```

生成 Allure HTML 报告：

```bash
allure serve allure-results
```

---

## 七、运行项目

### 1. 克隆项目

```bash
git clone <your-repository-url>
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 执行测试

```bash
pytest
```

### 4. 查看 Allure 报告

```bash
allure serve allure-results
```

---

## 八、项目亮点

1. 使用 YAML + Pytest Parametrize 实现数据驱动。
2. 使用 Fixture 管理测试前置操作。
3. 演示接口关联，实现登录获取 Token，鉴权请求头作为示例注释保存。
4. 覆盖多个业务模块及多种 HTTP 请求方法。
5. 使用 Allure 输出可视化测试报告，并记录接口请求和响应信息。
6. 使用 Git 进行项目代码管理。

---



## 项目定位

本项目为个人学习和实践项目，主要用于学习 Pytest 接口自动化测试框架设计及软件测试工程化实践。
