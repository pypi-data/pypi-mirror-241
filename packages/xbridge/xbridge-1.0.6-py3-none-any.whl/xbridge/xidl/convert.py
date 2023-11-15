import sys
import re

def remove_comments(java_code):
    # 使用正则表达式删除单行注释
    java_code = re.sub(r'//.*', '', java_code)
    # 使用正则表达式删除多行注释
    java_code = re.sub(r'/\*.*?\*/', '', java_code, flags=re.DOTALL)
    # 删除空白行
    java_code = re.sub(r'\n\s*\n', '\n', java_code)
    # 删除行首的空白内容
    java_code = re.sub(r'^\s+', '', java_code, flags=re.MULTILINE)
    return java_code

def convert_java_to_python(java_code):
    # 将Java代码按行分割
    lines = java_code.split('\n')
    
    # 初始化转换后的Python代码
    python_code = ''
    
    # 遍历每一行Java代码
    for line in lines:
        # 忽略空行
        if not line.strip():
            continue
        # 如果行以"class"开头，则表示是类定义
        elif line.strip().startswith('class'):
            # 获取类名
            class_name = line.split(' ')[1].strip()
            # 将类名添加到Python代码中
            python_code += f'class {class_name}:\n'
        # 如果行以"interface"开头，则表示是接口定义
        elif line.strip().startswith('interface'):
            # 获取接口名
            interface_name = line.split(' ')[1].strip()
            # 将接口名添加到Python代码中
            python_code += f'class {interface_name}:\n'
        # 如果行包含变量定义，则表示是变量声明
        elif any(keyword in line for keyword in ['byte', 'short', 'int', 'long', 'float', 'double', 'char', 'boolean']):
            # 获取变量类型和变量名
            variable_type, variable_name = line.split(' ')
            # 去除多余的空格和分号
            variable_type = variable_type.strip()
            variable_name = variable_name.strip().rstrip(';')
            # 将变量类型和变量名添加到Python代码中
            python_code += f'    {variable_name}: {variable_type}\n'
        # 如果行以"return"开头，则表示是函数返回类型声明
        elif line.strip().startswith('return'):
            # 获取返回类型
            return_type = line.split(' ')[1].strip()
            # 将返回类型添加到Python代码中
            python_code += f'    -> {return_type}\n'
        # 如果行以"public"或"private"开头，则表示是函数定义
        elif any(keyword in line for keyword in ['public', 'private']):
            # 获取函数名和参数列表
            function_name, parameters = line.split('(')
            # 去除多余的空格和分号
            function_name = function_name.split(' ')[-1].strip()
            parameters = parameters.strip().rstrip(')')
            # 将函数名和参数列表添加到Python代码中
            python_code += f'    def {function_name}({parameters}):\n'
    
    return python_code

# 获取命令行参数
java_file = sys.argv[1]
target_language = sys.argv[2]

# 读取Java文件内容
with open(java_file, 'r') as file:
    java_code = file.read()

# 删除注释
java_code = remove_comments(java_code)
print("----")
print(java_code)
print("----")
# 根据目标语言进行转换
if target_language == 'py':
    python_code = convert_java_to_python(java_code)
    print(python_code)
else:
    print('Unsupported target language.')