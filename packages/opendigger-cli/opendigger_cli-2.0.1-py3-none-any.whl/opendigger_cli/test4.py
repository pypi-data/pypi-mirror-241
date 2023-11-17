from datetime import datetime

def is_valid_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m")
        return True
    except ValueError:
        return False

# 测试示例日期字符串
date1 = "2023-01"
date2 = "2023-13"
date3 = "2023/01"

# 检测日期格式
print(is_valid_date_format(date1))  # True
print(is_valid_date_format(date2))  # False
print(is_valid_date_format(date3))  # False