import os

# 获取当前工作目录
print(os.path.realpath(__file__))

# 获取当前上一级工作目录
print(os.path.dirname(os.path.realpath(__file__)))

# 获取当前上两级工作目录
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# os.path.join()地址路径联接