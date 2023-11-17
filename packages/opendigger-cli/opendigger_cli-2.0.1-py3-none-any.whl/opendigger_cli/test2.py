import json

# 原始 JSON 数据
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# 解析 JSON 数据
data = json.loads(json_data)

# 以美化格式输出 JSON 变量
formatted_json = json.dumps(data, indent=4, sort_keys=True)

# 输出美化后的 JSON
print(formatted_json)
