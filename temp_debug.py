import requests

url = "https://reqres.in/api/users/2"
resp = requests.get(url)
print("状态码", resp.status_code)
print("响应文本", resp.text)
print("请求头", resp.request.headers)
