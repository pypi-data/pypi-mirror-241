# # 定义颜色常量
# class Colors:
#     RESET = '\033[0m'
#     RED = '\033[91m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     BLUE = '\033[94m'
#
# # 输出带有颜色的文本
# print(Colors.RED + '红色文本' + Colors.RESET)
# print(Colors.GREEN + '绿色文本' + Colors.RESET)
# print(Colors.YELLOW + '黄色文本' + Colors.RESET)
# print(Colors.BLUE + '蓝色文本' + Colors.RESET)

from colorama import init, Fore, Style

# 初始化 colorama
init()

# 输出带有颜色的文本
print(Fore.RED + '红色文本')
print(Fore.GREEN + '绿色文本')
print(Fore.YELLOW + '黄色文本')
print(Fore.BLUE + '蓝色文本')
print(111)

# 恢复默认的终端颜色
print(Style.RESET_ALL + '恢复默认颜色的文本')

a = Fore.RED + '红色' + Style.RESET_ALL + '默认' + Fore.GREEN + "绿色"
print(a)

from opendigger_cli.functions.common import print_util

print(print_util.yellow(text='1') + print_util.blue('2'))
print(3)