import re


fileName = 'SecurityEventExportResult.java'


def fix_java_entity_excel_index(fileName):
    assert fileName.endswith('.java'), 'File name must end with .java'
    # 读取txt文件内容
    with open(fileName, 'r', encoding='utf-8') as file:
        data = file.read()

    # 定义一个函数来处理index的值
    def update_index(match):
        # print(match)
        global index
        result = f'index = {index}'
        index += 1
        return result

    # 在正则表达式中查找ExcelProperty注解，并更新index值
    index = 0
    data = re.sub(r'index = \d+', update_index, data)
    # 将修改后的内容写入新文件
    with open(fileName + '_new', 'w', encoding='utf-8') as file:
        file.write(data)
    print('Index values updated successfully!')


