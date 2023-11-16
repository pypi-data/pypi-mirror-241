import re
import sys

def parse_xidl(file):
    with open(file, 'r') as f:
        content = f.read()

    classes = re.findall(r'class (\w+) \{(.*?)\}', content, re.DOTALL)
    interfaces = re.findall(r'interface (\w+) \{(.*?)\}', content, re.DOTALL)

    return classes, interfaces

def type_mapping(xidl_type):
    type_map = {
        'U8': 'int',
        'I8': 'int',
        'U16': 'int',
        'I16': 'int',
        'U32': 'int',
        'I32': 'int',
        'U64': 'int',
        'I64': 'int',
        'Bytes': 'bytes',
        'List': 'list',
        'Dict': 'dict',
        'Str': 'str',
        'Bool': 'bool'
    }

    if '<' in xidl_type and '>' in xidl_type:
        generic_type = re.search(r'<(.*)>', xidl_type).group(1)
        xidl_type = xidl_type.split('<')[0]
        return f'{type_map.get(xidl_type, xidl_type)}[{type_mapping(generic_type)}]'
    else:
        return type_map.get(xidl_type, xidl_type)

def generate_python(classes, interfaces):
    result = ''

    for class_name, class_body in classes:
        result += f'class {class_name}:\n'
        properties = re.findall(r'(.*?)(\w+) (\w+);', class_body, re.DOTALL)
        for prop_comment, prop_type, prop_name in properties:
            prop_comment = '\n'.join(['    #' + line.strip() for line in prop_comment.replace('/*', '').replace('*/', '').split('\n') if line.strip()])
            if prop_comment:
                result += f'{prop_comment}\n'
            result += f'    {prop_name}: {type_mapping(prop_type)} = None\n'
        result += '\n'

    for interface_name, interface_body in interfaces:
        result += f'class {interface_name}:\n'
        methods = re.findall(r'(.*?)(\w+) (\w+)\((.*?)\);', interface_body, re.DOTALL)
        for method_comment, method_return, method_name, method_params in methods:
            params = ', '.join([f'{param.split()[1]}: {type_mapping(param.split()[0])}' for param in method_params.split(', ')])
            method_comment = '\n'.join(['    #' + line.strip() for line in method_comment.replace('/*', '').replace('*/', '').split('\n') if line.strip()])
            if method_comment:
                result += f'{method_comment}\n'
            result += f'    def {method_name}(self, {params}) -> {type_mapping(method_return)}:\n'
            result += '        pass\n'
        result += '\n'

    return result

def main():
    xidl_file = sys.argv[1]
    target_lang = sys.argv[2]

    if target_lang != 'py':
        print('Only Python is supported currently.')
        return

    classes, interfaces = parse_xidl(xidl_file)
    python_code = generate_python(classes, interfaces)

    with open(xidl_file.replace('.xidl', '.py'), 'w') as f:
        f.write(python_code)

if __name__ == '__main__':
    main()